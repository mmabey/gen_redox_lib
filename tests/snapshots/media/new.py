# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class New(EventTypeAbstractModel):
    Media_: NewMedia = Field(..., alias="Media")
    Meta_: NewMeta = Field(..., alias="Meta")
    Orders_: List[NewOrder] = Field(None, alias="Orders")
    Patient_: NewPatient = Field(..., alias="Patient")
    Visit_: NewVisit = Field(None, alias="Visit")


class NewMedia(RedoxAbstractModel):
    Authenticated_: Union[str, None] = Field(None, alias="Authenticated")
    Authenticator_: NewMediaAuthenticator = Field(None, alias="Authenticator")
    Availability_: str = Field(..., alias="Availability")
    CreationDateTime_: Union[str, None] = Field(None, alias="CreationDateTime")
    DirectAddressFrom_: Union[str, None] = Field(None, alias="DirectAddressFrom")
    DirectAddressTo_: Union[str, None] = Field(None, alias="DirectAddressTo")
    DocumentDescription_: Union[str, None] = Field(None, alias="DocumentDescription")
    DocumentID_: str = Field(..., alias="DocumentID")
    DocumentType_: str = Field(..., alias="DocumentType")
    FileContents_: str = Field(..., alias="FileContents")
    FileName_: str = Field(..., alias="FileName")
    FileType_: str = Field(..., alias="FileType")
    Notifications_: List[NewMediaNotification] = Field(None, alias="Notifications")
    Provider_: NewMediaProvider = Field(..., alias="Provider")
    ServiceDateTime_: Union[str, None] = Field(None, alias="ServiceDateTime")


class NewMediaAuthenticator(RedoxAbstractModel):
    Address_: NewMediaAuthenticatorAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewMediaAuthenticatorLocation = Field(None, alias="Location")
    PhoneNumber_: NewMediaAuthenticatorPhoneNumber = Field(None, alias="PhoneNumber")


class NewMediaAuthenticatorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewMediaAuthenticatorLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewMediaAuthenticatorLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewMediaAuthenticatorLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewMediaAuthenticatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaAuthenticatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaAuthenticatorPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewMediaNotification(RedoxAbstractModel):
    Address_: NewMediaNotificationAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewMediaNotificationLocation = Field(None, alias="Location")
    PhoneNumber_: NewMediaNotificationPhoneNumber = Field(None, alias="PhoneNumber")


class NewMediaNotificationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewMediaNotificationLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewMediaNotificationLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewMediaNotificationLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewMediaNotificationLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaNotificationLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaNotificationPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewMediaProvider(RedoxAbstractModel):
    Address_: NewMediaProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: str = Field(..., alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewMediaProviderLocation = Field(None, alias="Location")
    PhoneNumber_: NewMediaProviderPhoneNumber = Field(None, alias="PhoneNumber")


class NewMediaProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewMediaProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[NewMediaProviderLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewMediaProviderLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewMediaProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewMediaProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[NewMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[NewMetaLog] = Field(None, alias="Logs")
    Message_: NewMetaMessage = Field(None, alias="Message")
    Source_: NewMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: NewMetaTransmission = Field(None, alias="Transmission")


class NewMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class NewMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NewMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NewOrder(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatient(RedoxAbstractModel):
    Demographics_: NewPatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[NewPatientIdentifier] = Field(..., alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")


class NewPatientDemographics(RedoxAbstractModel):
    Address_: NewPatientDemographicsAddress = Field(None, alias="Address")
    Citizenship_: List[str] = Field(None, alias="Citizenship")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    DeathDateTime_: Union[str, None] = Field(None, alias="DeathDateTime")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    IsDeceased_: Union[bool, None] = Field(None, alias="IsDeceased")
    IsHispanic_: Union[bool, None] = Field(None, alias="IsHispanic")
    Language_: Union[str, None] = Field(None, alias="Language")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MaritalStatus_: Union[str, None] = Field(None, alias="MaritalStatus")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: NewPatientDemographicsPhoneNumber = Field(None, alias="PhoneNumber")
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class NewPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class NewPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class NewVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    Location_: NewVisitLocation = Field(None, alias="Location")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class NewVisitLocation(RedoxAbstractModel):
    Bed_: Union[str, None] = Field(None, alias="Bed")
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[NewVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


New.model_rebuild()
NewMedia.model_rebuild()
NewMediaAuthenticator.model_rebuild()
NewMediaAuthenticatorLocation.model_rebuild()
NewMediaNotification.model_rebuild()
NewMediaNotificationLocation.model_rebuild()
NewMediaProvider.model_rebuild()
NewMediaProviderLocation.model_rebuild()
NewMeta.model_rebuild()
NewPatient.model_rebuild()
NewPatientDemographics.model_rebuild()
NewVisit.model_rebuild()
NewVisitLocation.model_rebuild()
