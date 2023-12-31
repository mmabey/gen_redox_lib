# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List

from pydantic import Field

from redox import surgicalscheduling
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _SurgicalScheduling(GenericEventTypeAbstractModel):
    _redox_module = surgicalscheduling


class Cancel(_SurgicalScheduling):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Procedures_: List[generic.Procedure] = Field(..., alias="Procedures")
    SurgeryStaff_: List[generic.SurgeryStaff] = Field(None, alias="SurgeryStaff")
    SurgicalCase_: generic.SurgicalCase = Field(None, alias="SurgicalCase")
    SurgicalInfo_: List[generic.SurgicalInfo] = Field(None, alias="SurgicalInfo")
    Visit_: generic.Visit = Field(..., alias="Visit")


class Modification(_SurgicalScheduling):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Procedures_: List[generic.Procedure] = Field(..., alias="Procedures")
    SurgeryStaff_: List[generic.SurgeryStaff] = Field(None, alias="SurgeryStaff")
    SurgicalCase_: generic.SurgicalCase = Field(None, alias="SurgicalCase")
    SurgicalInfo_: List[generic.SurgicalInfo] = Field(None, alias="SurgicalInfo")
    Visit_: generic.Visit = Field(..., alias="Visit")


class New(_SurgicalScheduling):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Procedures_: List[generic.Procedure] = Field(..., alias="Procedures")
    SurgeryStaff_: List[generic.SurgeryStaff] = Field(None, alias="SurgeryStaff")
    SurgicalCase_: generic.SurgicalCase = Field(None, alias="SurgicalCase")
    SurgicalInfo_: List[generic.SurgicalInfo] = Field(None, alias="SurgicalInfo")
    Visit_: generic.Visit = Field(..., alias="Visit")


class NoShow(_SurgicalScheduling):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Procedures_: List[generic.Procedure] = Field(..., alias="Procedures")
    SurgeryStaff_: List[generic.SurgeryStaff] = Field(None, alias="SurgeryStaff")
    SurgicalCase_: generic.SurgicalCase = Field(None, alias="SurgicalCase")
    SurgicalInfo_: List[generic.SurgicalInfo] = Field(None, alias="SurgicalInfo")
    Visit_: generic.Visit = Field(..., alias="Visit")


class Reschedule(_SurgicalScheduling):
    Meta_: generic.Meta = Field(..., alias="Meta")
    Patient_: generic.Patient = Field(..., alias="Patient")
    Procedures_: List[generic.Procedure] = Field(..., alias="Procedures")
    SurgeryStaff_: List[generic.SurgeryStaff] = Field(None, alias="SurgeryStaff")
    SurgicalCase_: generic.SurgicalCase = Field(None, alias="SurgicalCase")
    SurgicalInfo_: List[generic.SurgicalInfo] = Field(None, alias="SurgicalInfo")
    Visit_: generic.Visit = Field(..., alias="Visit")
