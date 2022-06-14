# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):

    Media: "NewMedia" = Field(...)
    Meta: "NewMeta" = Field(...)
    Orders: List["NewOrder"] = Field(None)
    Patient: "NewPatient" = Field(...)
    Visit: "NewVisit" = Field(None)


class NewMedia(RedoxAbstractModel):

    Authenticated: Union[str, None] = Field(None)
    Authenticator: "NewMediaAuthenticator" = Field(None)
    Availability: str = Field(...)
    CreationDateTime: Union[str, None] = Field(None)
    DirectAddressFrom: Union[str, None] = Field(None)
    DirectAddressTo: Union[str, None] = Field(None)
    DocumentDescription: Union[str, None] = Field(None)
    DocumentID: str = Field(...)
    DocumentType: str = Field(...)
    FileContents: str = Field(...)
    FileName: str = Field(...)
    FileType: str = Field(...)
    Notifications: List["NewMediaNotification"] = Field(None)
    Provider: "NewMediaProvider" = Field(...)
    ServiceDateTime: Union[str, None] = Field(None)


class NewMediaAuthenticator(RedoxAbstractModel):

    Address: "NewMediaAuthenticatorAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewMediaAuthenticatorLocation" = Field(None)
    PhoneNumber: "NewMediaAuthenticatorPhoneNumber" = Field(None)


class NewMediaAuthenticatorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewMediaAuthenticatorLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewMediaAuthenticatorPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewMediaNotification(RedoxAbstractModel):

    Address: "NewMediaNotificationAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewMediaNotificationLocation" = Field(None)
    PhoneNumber: "NewMediaNotificationPhoneNumber" = Field(None)


class NewMediaNotificationAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewMediaNotificationLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewMediaNotificationPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewMediaProvider(RedoxAbstractModel):

    Address: "NewMediaProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: str = Field(...)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewMediaProviderLocation" = Field(None)
    PhoneNumber: "NewMediaProviderPhoneNumber" = Field(None)


class NewMediaProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewMediaProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewMediaProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["NewMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NewMetaLog"] = Field(None)
    Message: "NewMetaMessage" = Field(None)
    Source: "NewMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NewMetaTransmission" = Field(None)


class NewMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NewMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewOrder(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatient(RedoxAbstractModel):

    Demographics: "NewPatientDemographics" = Field(None)
    Identifiers: List["NewPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class NewPatientDemographics(RedoxAbstractModel):

    Address: "NewPatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class NewPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class NewVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    Location: "NewVisitLocation" = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class NewVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


New.update_forward_refs()
NewMedia.update_forward_refs()
NewMediaAuthenticator.update_forward_refs()
NewMediaNotification.update_forward_refs()
NewMediaProvider.update_forward_refs()
NewMeta.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewVisit.update_forward_refs()
