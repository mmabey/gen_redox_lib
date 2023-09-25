# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from pyredox import provider
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _Provider(GenericEventTypeAbstractModel):
    _redox_module = provider


class Activate(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Providers_: List[generic.Provider] = Field(..., alias="Providers")


class Deactivate(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Providers_: List[generic.Provider] = Field(..., alias="Providers")


class New(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Providers_: List[generic.Provider] = Field(..., alias="Providers")


class ProviderQuery(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Provider_: generic.Provider = Field(None, alias="Provider")


class ProviderQueryResponse(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Providers_: List[generic.Provider] = Field(..., alias="Providers")


class Update(_Provider):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Providers_: List[generic.Provider] = Field(..., alias="Providers")
