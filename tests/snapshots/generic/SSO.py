# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from pyredox import sso
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _SSO(GenericEventTypeAbstractModel):
    _redox_module = sso


class SignOn(_SSO):
    EmailAddress_: Union[str, None] = Field(None, alias="EmailAddress")
    Expiration_: str = Field(..., alias="Expiration")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    IssuedAt_: str = Field(..., alias="IssuedAt")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Locale_: Union[str, None] = Field(None, alias="Locale")
    Meta_: generic.Meta = Field(..., alias="Meta")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    Name_: Union[str, None] = Field(None, alias="Name")
    Order_: generic.Order = Field(None, alias="Order")
    Patient_: generic.Patient = Field(None, alias="Patient")
    PhoneNumber_: generic.PhoneNumber = Field(None, alias="PhoneNumber")
    ProviderSpecialty_: Union[str, None] = Field(None, alias="ProviderSpecialty")
    Subject_: str = Field(..., alias="Subject")
    TimeZone_: Union[str, None] = Field(None, alias="TimeZone")
    UserId_: Union[str, None] = Field(None, alias="UserId")
    Visit_: generic.Visit = Field(None, alias="Visit")
