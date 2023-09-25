# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class VisitQuery(EventTypeAbstractModel):
    Meta_: VisitQueryMeta = Field(..., alias="Meta")
    Patient_: VisitQueryPatient = Field(..., alias="Patient")
    Visit_: VisitQueryVisit = Field(None, alias="Visit")


class VisitQueryMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[VisitQueryMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[VisitQueryMetaLog] = Field(None, alias="Logs")
    Message_: VisitQueryMetaMessage = Field(None, alias="Message")
    Source_: VisitQueryMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: VisitQueryMetaTransmission = Field(None, alias="Transmission")


class VisitQueryMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class VisitQueryMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class VisitQueryMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class VisitQueryMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class VisitQueryMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class VisitQueryPatient(RedoxAbstractModel):
    Identifiers_: List[VisitQueryPatientIdentifier] = Field(..., alias="Identifiers")


class VisitQueryPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class VisitQueryVisit(RedoxAbstractModel):
    EndDateTime_: Union[str, None] = Field(None, alias="EndDateTime")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


VisitQuery.model_rebuild()
VisitQueryMeta.model_rebuild()
VisitQueryPatient.model_rebuild()
