# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class ProviderQueryResponse(EventTypeAbstractModel):
    Meta_: ProviderQueryResponseMeta = Field(..., alias="Meta")
    Providers_: List[ProviderQueryResponseProvider] = Field(..., alias="Providers")


class ProviderQueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[ProviderQueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[ProviderQueryResponseMetaLog] = Field(None, alias="Logs")
    Message_: ProviderQueryResponseMetaMessage = Field(None, alias="Message")
    Source_: ProviderQueryResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: ProviderQueryResponseMetaTransmission = Field(
        None, alias="Transmission"
    )


class ProviderQueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class ProviderQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class ProviderQueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class ProviderQueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class ProviderQueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class ProviderQueryResponseProvider(RedoxAbstractModel):
    Demographics_: ProviderQueryResponseProviderDemographics = Field(
        None, alias="Demographics"
    )
    Identifiers_: List[ProviderQueryResponseProviderIdentifier] = Field(
        ..., alias="Identifiers"
    )
    IsActive_: bool = Field(..., alias="IsActive")
    Qualifications_: List[ProviderQueryResponseProviderQualification] = Field(
        None, alias="Qualifications"
    )
    Roles_: List[ProviderQueryResponseProviderRole] = Field(None, alias="Roles")


class ProviderQueryResponseProviderDemographics(RedoxAbstractModel):
    Addresses_: List[ProviderQueryResponseProviderDemographicsAddress] = Field(
        None, alias="Addresses"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Languages_: List[str] = Field(None, alias="Languages")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: ProviderQueryResponseProviderDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Sex_: Union[str, None] = Field(None, alias="Sex")


class ProviderQueryResponseProviderDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    Use_: Union[str, None] = Field(None, alias="Use")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ProviderQueryResponseProviderDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class ProviderQueryResponseProviderIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderQualification(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    Identifiers_: List[ProviderQueryResponseProviderQualificationIdentifier] = Field(
        None, alias="Identifiers"
    )
    StartDate_: Union[str, None] = Field(None, alias="StartDate")


class ProviderQueryResponseProviderQualificationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderRole(RedoxAbstractModel):
    Availability_: List[ProviderQueryResponseProviderRoleAvailability] = Field(
        None, alias="Availability"
    )
    Identifiers_: List[ProviderQueryResponseProviderRoleIdentifier] = Field(
        None, alias="Identifiers"
    )
    Locations_: List[ProviderQueryResponseProviderRoleLocation] = Field(
        None, alias="Locations"
    )
    Organization_: ProviderQueryResponseProviderRoleOrganization = Field(
        None, alias="Organization"
    )
    Services_: List[ProviderQueryResponseProviderRoleService] = Field(
        None, alias="Services"
    )
    Specialties_: List[ProviderQueryResponseProviderRoleSpecialty] = Field(
        None, alias="Specialties"
    )


class ProviderQueryResponseProviderRoleAvailability(RedoxAbstractModel):
    AvailableEndTime_: Union[str, None] = Field(None, alias="AvailableEndTime")
    AvailableStartTime_: Union[str, None] = Field(None, alias="AvailableStartTime")
    Days_: List[str] = Field(None, alias="Days")


class ProviderQueryResponseProviderRoleIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderRoleLocation(RedoxAbstractModel):
    Address_: ProviderQueryResponseProviderRoleLocationAddress = Field(
        None, alias="Address"
    )
    Description_: Union[str, None] = Field(None, alias="Description")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Identifiers_: List[ProviderQueryResponseProviderRoleLocationIdentifier] = Field(
        None, alias="Identifiers"
    )
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: ProviderQueryResponseProviderRoleLocationPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Status_: Union[str, None] = Field(None, alias="Status")


class ProviderQueryResponseProviderRoleLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ProviderQueryResponseProviderRoleLocationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderRoleLocationPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class ProviderQueryResponseProviderRoleOrganization(RedoxAbstractModel):
    Address_: ProviderQueryResponseProviderRoleOrganizationAddress = Field(
        None, alias="Address"
    )
    Identifiers_: List[ProviderQueryResponseProviderRoleOrganizationIdentifier] = Field(
        None, alias="Identifiers"
    )
    IsActive_: Union[str, None] = Field(None, alias="IsActive")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class ProviderQueryResponseProviderRoleOrganizationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ProviderQueryResponseProviderRoleOrganizationIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderRoleService(RedoxAbstractModel):
    Description_: Union[str, None] = Field(None, alias="Description")
    Identifiers_: List[ProviderQueryResponseProviderRoleServiceIdentifier] = Field(
        None, alias="Identifiers"
    )
    PhoneNumber_: ProviderQueryResponseProviderRoleServicePhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Type_: Union[str, None] = Field(None, alias="Type")


class ProviderQueryResponseProviderRoleServiceIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class ProviderQueryResponseProviderRoleServicePhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class ProviderQueryResponseProviderRoleSpecialty(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


ProviderQueryResponse.model_rebuild()
ProviderQueryResponseMeta.model_rebuild()
ProviderQueryResponseProvider.model_rebuild()
ProviderQueryResponseProviderDemographics.model_rebuild()
ProviderQueryResponseProviderQualification.model_rebuild()
ProviderQueryResponseProviderRole.model_rebuild()
ProviderQueryResponseProviderRoleLocation.model_rebuild()
ProviderQueryResponseProviderRoleOrganization.model_rebuild()
ProviderQueryResponseProviderRoleService.model_rebuild()
