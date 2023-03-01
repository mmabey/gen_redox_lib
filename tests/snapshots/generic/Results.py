# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import results
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Results(GenericEventTypeAbstractModel):
    _redox_module = results


class New(_Results):
    Meta: generic.Meta = Field(...)
    Orders: List[generic.Order] = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class NewUnsolicited(_Results):
    Meta: generic.Meta = Field(...)
    Orders: List[generic.Order] = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Query(_Results):
    Completion: generic.Completion = Field(None)
    LastUpdated: generic.LastUpdated = Field(None)
    Location: generic.Location = Field(None)
    Meta: generic.Meta = Field(...)
    OrderIDs: List[str] = Field(None)
    Patients: List[generic.Patient] = Field(None)
    Procedures: List[generic.Procedure] = Field(None)
    ResultStatuses: List[str] = Field(None)


class QueryResponse(_Results):
    Meta: generic.Meta = Field(...)
    Orders: List[generic.Order] = Field(None)
