# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class DocumentGetResponse(EventTypeAbstractModel):
    Data: str = Field(...)
    Document: "DocumentGetResponseDocument" = Field(...)
    FileType: str = Field(...)
    Meta: "DocumentGetResponseMeta" = Field(...)


class DocumentGetResponseDocument(RedoxAbstractModel):
    ID: str = Field(...)


class DocumentGetResponseMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["DocumentGetResponseMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["DocumentGetResponseMetaLog"] = Field(None)
    Message: "DocumentGetResponseMetaMessage" = Field(None)
    Source: "DocumentGetResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "DocumentGetResponseMetaTransmission" = Field(None)


class DocumentGetResponseMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DocumentGetResponseMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class DocumentGetResponseMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class DocumentGetResponseMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DocumentGetResponseMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


DocumentGetResponse.update_forward_refs()
DocumentGetResponseMeta.update_forward_refs()
