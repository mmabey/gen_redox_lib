# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Callable, Generator, List, Optional

import click
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape

from .common_klasses import CommonKlassKeeper
from .parse_spec import parse_and_build_models
from .types import TemplateInfo


def process_files(
    extracted_folder: Path, dst: Path, directories: List[str], template_dir: Path
):

    # Create the Jinja environment and template
    jinja_env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = jinja_env.get_template("template-resource.jinja2")

    commons = CommonKlassKeeper()

    # Count the number of files we'll be processing so click can make a progressbar
    num_files = sum(len(list((extracted_folder / d).iterdir())) for d in directories)

    # Create the progressbar and an updater function
    with click.progressbar(
        length=num_files, label="Generating Python files", item_show_func=lambda f: f
    ) as bar:

        def update_bar(file_name: str):
            bar.update(1, file_name)

        for directory in directories:
            # Make sure the destination dir exists and contains an __init__.py
            (dst / directory).mkdir()

            parsed_generator = parse_and_build_models(
                spec_dir=extracted_folder / directory
            )
            write_py_files(
                lib_dest_dir=dst,
                template=template,
                progressbar_updater=update_bar,
                template_info_generator=commons.store_and_yield_templates(
                    parsed_generator
                ),
            )

    click.echo(f"Generating common types file in {commons.template_filename}")
    write_py_files(
        lib_dest_dir=dst, template=template, template_info_generator=commons.template
    )

    click.echo("Done")
    click.echo(f"pyredox files generated at {dst}")


def write_py_files(
    lib_dest_dir: Path,
    template: Template,
    template_info_generator: Generator[TemplateInfo, None, None],
    progressbar_updater: Optional[Callable] = lambda _: None,
):
    """Write the generated files for a single directory.

    :param lib_dest_dir: The directory where the generated library Python files
        will be written.
    :param template: The Jinja2 template to use for generating the Python files.
    :param template_info_generator:
    :param progressbar_updater: A function for updating the progress on writing
        the generated files. Should take a filename string as the only argument.
    """

    for template_info in template_info_generator:
        with open(
            lib_dest_dir / template_info.dir_name / template_info.file_name, "w"
        ) as model_file:

            model_file.write(template.render(**template_info.as_dict()))

        progressbar_updater(template_info.file_name)

        # Add all event type classes as imports in the __init__.py for easier importing
        init_path = lib_dest_dir / template_info.dir_name / "__init__.py"
        if not init_path.exists():
            # Start the file with a flake8 ignore command
            with open(init_path, "w") as init_file:
                init_file.write("# flake8: noqa: F01\n")
        with open(init_path, "a") as init_file:
            for event_class in template_info.event_type_classes:
                # Don't worry too much about the formatting here since isort will clean
                # it up for us.
                init_file.write(
                    f"from .{template_info.file_name.rsplit('.', 1)[0]} "
                    f"import {event_class.full_name}\n"
                )