# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Reschedule(EventTypeAbstractModel):
    AppointmentInfo_: List[RescheduleAppointmentInfo] = Field(
        None, alias="AppointmentInfo"
    )
    Meta_: RescheduleMeta = Field(..., alias="Meta")
    Patient_: ReschedulePatient = Field(None, alias="Patient")
    Visit_: RescheduleVisit = Field(..., alias="Visit")


class RescheduleAppointmentInfo(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Value_: Union[str, None] = Field(None, alias="Value")


class RescheduleMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[RescheduleMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[RescheduleMetaLog] = Field(None, alias="Logs")
    Message_: RescheduleMetaMessage = Field(None, alias="Message")
    Source_: RescheduleMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: RescheduleMetaTransmission = Field(None, alias="Transmission")


class RescheduleMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class RescheduleMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class RescheduleMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class RescheduleMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class RescheduleMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class ReschedulePatient(RedoxAbstractModel):
    Demographics_: ReschedulePatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[ReschedulePatientIdentifier] = Field(None, alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")


class ReschedulePatientDemographics(RedoxAbstractModel):
    Address_: ReschedulePatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: ReschedulePatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class ReschedulePatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class ReschedulePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class ReschedulePatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    AdditionalStaff_: List[RescheduleVisitAdditionalStaff] = Field(
        None, alias="AdditionalStaff"
    )
    AttendingProvider_: RescheduleVisitAttendingProvider = Field(
        None, alias="AttendingProvider"
    )
    ConsultingProvider_: RescheduleVisitConsultingProvider = Field(
        None, alias="ConsultingProvider"
    )
    Diagnoses_: List[RescheduleVisitDiagnosis] = Field(None, alias="Diagnoses")
    Duration_: float = Field(..., alias="Duration")
    Equipment_: List[RescheduleVisitEquipment] = Field(None, alias="Equipment")
    Instructions_: List[str] = Field(None, alias="Instructions")
    Location_: RescheduleVisitLocation = Field(..., alias="Location")
    OldDateTime_: Union[str, None] = Field(None, alias="OldDateTime")
    OldVisitNumber_: Union[str, None] = Field(None, alias="OldVisitNumber")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    ReferringProvider_: RescheduleVisitReferringProvider = Field(
        None, alias="ReferringProvider"
    )
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: Union[str, None] = Field(None, alias="Type")
    VisitDateTime_: str = Field(..., alias="VisitDateTime")
    VisitNumber_: str = Field(..., alias="VisitNumber")
    VisitProvider_: RescheduleVisitVisitProvider = Field(None, alias="VisitProvider")


class RescheduleVisitAdditionalStaff(RedoxAbstractModel):
    Address_: RescheduleVisitAdditionalStaffAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    Duration_: Union[float, None] = Field(None, alias="Duration")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: RescheduleVisitAdditionalStaffLocation = Field(None, alias="Location")
    PhoneNumber_: RescheduleVisitAdditionalStaffPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Role_: RescheduleVisitAdditionalStaffRole = Field(None, alias="Role")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")


class RescheduleVisitAdditionalStaffAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class RescheduleVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        RescheduleVisitAdditionalStaffLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        RescheduleVisitAdditionalStaffLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitAdditionalStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class RescheduleVisitAdditionalStaffRole(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class RescheduleVisitAttendingProvider(RedoxAbstractModel):
    Address_: RescheduleVisitAttendingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: RescheduleVisitAttendingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: RescheduleVisitAttendingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class RescheduleVisitAttendingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class RescheduleVisitAttendingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        RescheduleVisitAttendingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        RescheduleVisitAttendingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class RescheduleVisitConsultingProvider(RedoxAbstractModel):
    Address_: RescheduleVisitConsultingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: RescheduleVisitConsultingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: RescheduleVisitConsultingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class RescheduleVisitConsultingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class RescheduleVisitConsultingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        RescheduleVisitConsultingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        RescheduleVisitConsultingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitConsultingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitConsultingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class RescheduleVisitDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitEquipment(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Duration_: Union[float, None] = Field(None, alias="Duration")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")


class RescheduleVisitLocation(RedoxAbstractModel):
    Department_: str = Field(..., alias="Department")
    DepartmentIdentifiers_: List[RescheduleVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[RescheduleVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitReferringProvider(RedoxAbstractModel):
    Address_: RescheduleVisitReferringProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: RescheduleVisitReferringProviderLocation = Field(None, alias="Location")
    PhoneNumber_: RescheduleVisitReferringProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class RescheduleVisitReferringProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class RescheduleVisitReferringProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        RescheduleVisitReferringProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        RescheduleVisitReferringProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class RescheduleVisitVisitProvider(RedoxAbstractModel):
    Address_: RescheduleVisitVisitProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: RescheduleVisitVisitProviderLocation = Field(None, alias="Location")
    PhoneNumber_: RescheduleVisitVisitProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class RescheduleVisitVisitProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class RescheduleVisitVisitProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        RescheduleVisitVisitProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        RescheduleVisitVisitProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class RescheduleVisitVisitProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitVisitProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class RescheduleVisitVisitProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


Reschedule.model_rebuild()
RescheduleMeta.model_rebuild()
ReschedulePatient.model_rebuild()
ReschedulePatientDemographics.model_rebuild()
RescheduleVisit.model_rebuild()
RescheduleVisitAdditionalStaff.model_rebuild()
RescheduleVisitAdditionalStaffLocation.model_rebuild()
RescheduleVisitAttendingProvider.model_rebuild()
RescheduleVisitAttendingProviderLocation.model_rebuild()
RescheduleVisitConsultingProvider.model_rebuild()
RescheduleVisitConsultingProviderLocation.model_rebuild()
RescheduleVisitLocation.model_rebuild()
RescheduleVisitReferringProvider.model_rebuild()
RescheduleVisitReferringProviderLocation.model_rebuild()
RescheduleVisitVisitProvider.model_rebuild()
RescheduleVisitVisitProviderLocation.model_rebuild()
