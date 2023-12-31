# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class PreAdmit(EventTypeAbstractModel):
    Meta_: PreAdmitMeta = Field(..., alias="Meta")
    Patient_: PreAdmitPatient = Field(..., alias="Patient")
    Visit_: PreAdmitVisit = Field(None, alias="Visit")


class PreAdmitMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[PreAdmitMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[PreAdmitMetaLog] = Field(None, alias="Logs")
    Message_: PreAdmitMetaMessage = Field(None, alias="Message")
    Source_: PreAdmitMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: PreAdmitMetaTransmission = Field(None, alias="Transmission")


class PreAdmitMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PreAdmitMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class PreAdmitMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PreAdmitMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PreAdmitMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PreAdmitPatient(RedoxAbstractModel):
    Allergies_: List[PreAdmitPatientAllergy] = Field(None, alias="Allergies")
    Contacts_: List[PreAdmitPatientContact] = Field(None, alias="Contacts")
    Demographics_: PreAdmitPatientDemographics = Field(None, alias="Demographics")
    Diagnoses_: List[PreAdmitPatientDiagnosis] = Field(None, alias="Diagnoses")
    Identifiers_: List[PreAdmitPatientIdentifier] = Field(..., alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")
    PCP_: PreAdmitPatientPCP = Field(None, alias="PCP")


class PreAdmitPatientAllergy(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")
    OnsetDateTime_: Union[str, None] = Field(None, alias="OnsetDateTime")
    Reaction_: List[PreAdmitPatientAllergyReaction] = Field(None, alias="Reaction")
    Severity_: PreAdmitPatientAllergySeverity = Field(None, alias="Severity")
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: PreAdmitPatientAllergyType = Field(None, alias="Type")


class PreAdmitPatientAllergyReaction(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PreAdmitPatientAllergySeverity(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PreAdmitPatientAllergyType(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PreAdmitPatientContact(RedoxAbstractModel):
    Address_: PreAdmitPatientContactAddress = Field(None, alias="Address")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: PreAdmitPatientContactPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class PreAdmitPatientContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitPatientContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitPatientDemographics(RedoxAbstractModel):
    Address_: PreAdmitPatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: PreAdmitPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class PreAdmitPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitPatientDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class PreAdmitPatientPCP(RedoxAbstractModel):
    Address_: PreAdmitPatientPCPAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitPatientPCPLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: PreAdmitPatientPCPPhoneNumber = Field(None, alias="PhoneNumber")


class PreAdmitPatientPCPAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitPatientPCPLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitPatientPCPLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[PreAdmitPatientPCPLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitPatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitPatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitPatientPCPPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    AdditionalStaff_: List[PreAdmitVisitAdditionalStaff] = Field(
        None, alias="AdditionalStaff"
    )
    AdmittingProvider_: PreAdmitVisitAdmittingProvider = Field(
        None, alias="AdmittingProvider"
    )
    AttendingProvider_: PreAdmitVisitAttendingProvider = Field(
        None, alias="AttendingProvider"
    )
    Balance_: Union[float, None] = Field(None, alias="Balance")
    ConsultingProvider_: PreAdmitVisitConsultingProvider = Field(
        None, alias="ConsultingProvider"
    )
    DiagnosisRelatedGroup_: Union[float, None] = Field(
        None, alias="DiagnosisRelatedGroup"
    )
    DiagnosisRelatedGroupType_: Union[float, None] = Field(
        None, alias="DiagnosisRelatedGroupType"
    )
    Duration_: Union[float, None] = Field(None, alias="Duration")
    Guarantor_: PreAdmitVisitGuarantor = Field(None, alias="Guarantor")
    Instructions_: List[str] = Field(None, alias="Instructions")
    Insurances_: List[PreAdmitVisitInsurance] = Field(None, alias="Insurances")
    Location_: PreAdmitVisitLocation = Field(None, alias="Location")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    ReferringProvider_: PreAdmitVisitReferringProvider = Field(
        None, alias="ReferringProvider"
    )
    VisitDateTime_: Union[str, None] = Field(None, alias="VisitDateTime")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class PreAdmitVisitAdditionalStaff(RedoxAbstractModel):
    Address_: PreAdmitVisitAdditionalStaffAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitVisitAdditionalStaffLocation = Field(None, alias="Location")
    PhoneNumber_: PreAdmitVisitAdditionalStaffPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Role_: PreAdmitVisitAdditionalStaffRole = Field(None, alias="Role")


class PreAdmitVisitAdditionalStaffAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitVisitAdditionalStaffLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PreAdmitVisitAdditionalStaffLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitAdditionalStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitVisitAdditionalStaffRole(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class PreAdmitVisitAdmittingProvider(RedoxAbstractModel):
    Address_: PreAdmitVisitAdmittingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitVisitAdmittingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: PreAdmitVisitAdmittingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PreAdmitVisitAdmittingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitAdmittingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitVisitAdmittingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PreAdmitVisitAdmittingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitAdmittingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAdmittingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAdmittingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitVisitAttendingProvider(RedoxAbstractModel):
    Address_: PreAdmitVisitAttendingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitVisitAttendingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: PreAdmitVisitAttendingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PreAdmitVisitAttendingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitAttendingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitVisitAttendingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PreAdmitVisitAttendingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitVisitConsultingProvider(RedoxAbstractModel):
    Address_: PreAdmitVisitConsultingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitVisitConsultingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: PreAdmitVisitConsultingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PreAdmitVisitConsultingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitConsultingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitVisitConsultingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PreAdmitVisitConsultingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitConsultingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitConsultingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PreAdmitVisitGuarantor(RedoxAbstractModel):
    Address_: PreAdmitVisitGuarantorAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Employer_: PreAdmitVisitGuarantorEmployer = Field(None, alias="Employer")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Number_: Union[str, None] = Field(None, alias="Number")
    PhoneNumber_: PreAdmitVisitGuarantorPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")
    Spouse_: PreAdmitVisitGuarantorSpouse = Field(None, alias="Spouse")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitGuarantorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitGuarantorEmployer(RedoxAbstractModel):
    Address_: PreAdmitVisitGuarantorEmployerAddress = Field(None, alias="Address")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class PreAdmitVisitGuarantorEmployerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitGuarantorPhoneNumber(RedoxAbstractModel):
    Business_: Union[str, None] = Field(None, alias="Business")
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")


class PreAdmitVisitGuarantorSpouse(RedoxAbstractModel):
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")


class PreAdmitVisitInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: PreAdmitVisitInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: PreAdmitVisitInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: PreAdmitVisitInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class PreAdmitVisitInsuranceCompany(RedoxAbstractModel):
    Address_: PreAdmitVisitInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class PreAdmitVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitInsuranceInsured(RedoxAbstractModel):
    Address_: PreAdmitVisitInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[PreAdmitVisitInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class PreAdmitVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitLocation(RedoxAbstractModel):
    Address_: PreAdmitVisitLocationAddress = Field(None, alias="Address")
    Bed_: Union[str, None] = Field(None, alias="Bed")
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[PreAdmitVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[PreAdmitVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitReferringProvider(RedoxAbstractModel):
    Address_: PreAdmitVisitReferringProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PreAdmitVisitReferringProviderLocation = Field(None, alias="Location")
    PhoneNumber_: PreAdmitVisitReferringProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PreAdmitVisitReferringProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PreAdmitVisitReferringProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PreAdmitVisitReferringProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PreAdmitVisitReferringProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PreAdmitVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PreAdmitVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


PreAdmit.model_rebuild()
PreAdmitMeta.model_rebuild()
PreAdmitPatient.model_rebuild()
PreAdmitPatientAllergy.model_rebuild()
PreAdmitPatientContact.model_rebuild()
PreAdmitPatientDemographics.model_rebuild()
PreAdmitPatientPCP.model_rebuild()
PreAdmitPatientPCPLocation.model_rebuild()
PreAdmitVisit.model_rebuild()
PreAdmitVisitAdditionalStaff.model_rebuild()
PreAdmitVisitAdditionalStaffLocation.model_rebuild()
PreAdmitVisitAdmittingProvider.model_rebuild()
PreAdmitVisitAdmittingProviderLocation.model_rebuild()
PreAdmitVisitAttendingProvider.model_rebuild()
PreAdmitVisitAttendingProviderLocation.model_rebuild()
PreAdmitVisitConsultingProvider.model_rebuild()
PreAdmitVisitConsultingProviderLocation.model_rebuild()
PreAdmitVisitGuarantor.model_rebuild()
PreAdmitVisitGuarantorEmployer.model_rebuild()
PreAdmitVisitInsurance.model_rebuild()
PreAdmitVisitInsuranceCompany.model_rebuild()
PreAdmitVisitInsuranceInsured.model_rebuild()
PreAdmitVisitLocation.model_rebuild()
PreAdmitVisitReferringProvider.model_rebuild()
PreAdmitVisitReferringProviderLocation.model_rebuild()
