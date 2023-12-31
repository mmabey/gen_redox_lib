# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List

from pydantic import Field

from redox import media
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _Media(GenericEventTypeAbstractModel):
    _redox_module = media


class Delete(_Media):
    Media_: generic.Media = Field(..., alias="Media")
    Meta_: generic.Meta = Field(..., alias="Meta")
    Orders_: List[generic.Order] = Field(None, alias="Orders")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Visit_: generic.Visit = Field(None, alias="Visit")


class New(_Media):
    Media_: generic.Media = Field(..., alias="Media")
    Meta_: generic.Meta = Field(..., alias="Meta")
    Orders_: List[generic.Order] = Field(None, alias="Orders")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Visit_: generic.Visit = Field(None, alias="Visit")


class Query(_Media):
    DocumentIDs_: List[str] = Field(None, alias="DocumentIDs")
    DocumentTypes_: List[str] = Field(None, alias="DocumentTypes")
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patients_: List[generic.Patient] = Field(None, alias="Patients")
    VisitNumbers_: List[str] = Field(None, alias="VisitNumbers")


class QueryResponse(_Media):
    Media_: List[generic.Medium] = Field(None, alias="Media")
    Meta_: generic.Meta = Field(..., alias="Meta")


class Replace(_Media):
    Media_: generic.Media = Field(..., alias="Media")
    Meta_: generic.Meta = Field(..., alias="Meta")
    Orders_: List[generic.Order] = Field(None, alias="Orders")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Visit_: generic.Visit = Field(None, alias="Visit")
