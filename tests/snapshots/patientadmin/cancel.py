# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Cancel(EventTypeAbstractModel):
    Meta_: CancelMeta = Field(..., alias="Meta")
    Patient_: CancelPatient = Field(..., alias="Patient")
    Visit_: CancelVisit = Field(None, alias="Visit")


class CancelMeta(RedoxAbstractModel):
    CanceledEvent_: Union[str, None] = Field(None, alias="CanceledEvent")
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[CancelMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[CancelMetaLog] = Field(None, alias="Logs")
    Message_: CancelMetaMessage = Field(None, alias="Message")
    Source_: CancelMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: CancelMetaTransmission = Field(None, alias="Transmission")


class CancelMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class CancelMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class CancelMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class CancelPatient(RedoxAbstractModel):
    Allergies_: List[CancelPatientAllergy] = Field(None, alias="Allergies")
    Contacts_: List[CancelPatientContact] = Field(None, alias="Contacts")
    Demographics_: CancelPatientDemographics = Field(None, alias="Demographics")
    Diagnoses_: List[CancelPatientDiagnosis] = Field(None, alias="Diagnoses")
    Identifiers_: List[CancelPatientIdentifier] = Field(..., alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")
    PCP_: CancelPatientPCP = Field(None, alias="PCP")


class CancelPatientAllergy(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")
    OnsetDateTime_: Union[str, None] = Field(None, alias="OnsetDateTime")
    Reaction_: List[CancelPatientAllergyReaction] = Field(None, alias="Reaction")
    Severity_: CancelPatientAllergySeverity = Field(None, alias="Severity")
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: CancelPatientAllergyType = Field(None, alias="Type")


class CancelPatientAllergyReaction(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelPatientAllergySeverity(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelPatientAllergyType(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelPatientContact(RedoxAbstractModel):
    Address_: CancelPatientContactAddress = Field(None, alias="Address")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: CancelPatientContactPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class CancelPatientContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelPatientDemographics(RedoxAbstractModel):
    Address_: CancelPatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: CancelPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class CancelPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelPatientDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class CancelPatientPCP(RedoxAbstractModel):
    Address_: CancelPatientPCPAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelPatientPCPLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: CancelPatientPCPPhoneNumber = Field(None, alias="PhoneNumber")


class CancelPatientPCPAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientPCPLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[CancelPatientPCPLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[CancelPatientPCPLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelPatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelPatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelPatientPCPPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    AdditionalStaff_: List[CancelVisitAdditionalStaff] = Field(
        None, alias="AdditionalStaff"
    )
    AdmittingProvider_: CancelVisitAdmittingProvider = Field(
        None, alias="AdmittingProvider"
    )
    AttendingProvider_: CancelVisitAttendingProvider = Field(
        None, alias="AttendingProvider"
    )
    Balance_: Union[float, None] = Field(None, alias="Balance")
    ConsultingProvider_: CancelVisitConsultingProvider = Field(
        None, alias="ConsultingProvider"
    )
    DiagnosisRelatedGroup_: Union[float, None] = Field(
        None, alias="DiagnosisRelatedGroup"
    )
    DiagnosisRelatedGroupType_: Union[float, None] = Field(
        None, alias="DiagnosisRelatedGroupType"
    )
    Duration_: Union[float, None] = Field(None, alias="Duration")
    Guarantor_: CancelVisitGuarantor = Field(None, alias="Guarantor")
    Instructions_: List[str] = Field(None, alias="Instructions")
    Insurances_: List[CancelVisitInsurance] = Field(None, alias="Insurances")
    Location_: CancelVisitLocation = Field(None, alias="Location")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    ReferringProvider_: CancelVisitReferringProvider = Field(
        None, alias="ReferringProvider"
    )
    VisitDateTime_: Union[str, None] = Field(None, alias="VisitDateTime")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class CancelVisitAdditionalStaff(RedoxAbstractModel):
    Address_: CancelVisitAdditionalStaffAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelVisitAdditionalStaffLocation = Field(None, alias="Location")
    PhoneNumber_: CancelVisitAdditionalStaffPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Role_: CancelVisitAdditionalStaffRole = Field(None, alias="Role")


class CancelVisitAdditionalStaffAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelVisitAdditionalStaffLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelVisitAdditionalStaffLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitAdditionalStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelVisitAdditionalStaffRole(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class CancelVisitAdmittingProvider(RedoxAbstractModel):
    Address_: CancelVisitAdmittingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelVisitAdmittingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: CancelVisitAdmittingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class CancelVisitAdmittingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitAdmittingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelVisitAdmittingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelVisitAdmittingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitAdmittingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAdmittingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAdmittingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelVisitAttendingProvider(RedoxAbstractModel):
    Address_: CancelVisitAttendingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelVisitAttendingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: CancelVisitAttendingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class CancelVisitAttendingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitAttendingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelVisitAttendingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelVisitAttendingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelVisitConsultingProvider(RedoxAbstractModel):
    Address_: CancelVisitConsultingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelVisitConsultingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: CancelVisitConsultingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class CancelVisitConsultingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitConsultingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelVisitConsultingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelVisitConsultingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitConsultingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitConsultingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelVisitGuarantor(RedoxAbstractModel):
    Address_: CancelVisitGuarantorAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Employer_: CancelVisitGuarantorEmployer = Field(None, alias="Employer")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Number_: Union[str, None] = Field(None, alias="Number")
    PhoneNumber_: CancelVisitGuarantorPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")
    Spouse_: CancelVisitGuarantorSpouse = Field(None, alias="Spouse")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitGuarantorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitGuarantorEmployer(RedoxAbstractModel):
    Address_: CancelVisitGuarantorEmployerAddress = Field(None, alias="Address")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class CancelVisitGuarantorEmployerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitGuarantorPhoneNumber(RedoxAbstractModel):
    Business_: Union[str, None] = Field(None, alias="Business")
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")


class CancelVisitGuarantorSpouse(RedoxAbstractModel):
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")


class CancelVisitInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: CancelVisitInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: CancelVisitInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: CancelVisitInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class CancelVisitInsuranceCompany(RedoxAbstractModel):
    Address_: CancelVisitInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class CancelVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitInsuranceInsured(RedoxAbstractModel):
    Address_: CancelVisitInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[CancelVisitInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class CancelVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitLocation(RedoxAbstractModel):
    Address_: CancelVisitLocationAddress = Field(None, alias="Address")
    Bed_: Union[str, None] = Field(None, alias="Bed")
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[CancelVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[CancelVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitReferringProvider(RedoxAbstractModel):
    Address_: CancelVisitReferringProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelVisitReferringProviderLocation = Field(None, alias="Location")
    PhoneNumber_: CancelVisitReferringProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class CancelVisitReferringProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelVisitReferringProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelVisitReferringProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelVisitReferringProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


Cancel.model_rebuild()
CancelMeta.model_rebuild()
CancelPatient.model_rebuild()
CancelPatientAllergy.model_rebuild()
CancelPatientContact.model_rebuild()
CancelPatientDemographics.model_rebuild()
CancelPatientPCP.model_rebuild()
CancelPatientPCPLocation.model_rebuild()
CancelVisit.model_rebuild()
CancelVisitAdditionalStaff.model_rebuild()
CancelVisitAdditionalStaffLocation.model_rebuild()
CancelVisitAdmittingProvider.model_rebuild()
CancelVisitAdmittingProviderLocation.model_rebuild()
CancelVisitAttendingProvider.model_rebuild()
CancelVisitAttendingProviderLocation.model_rebuild()
CancelVisitConsultingProvider.model_rebuild()
CancelVisitConsultingProviderLocation.model_rebuild()
CancelVisitGuarantor.model_rebuild()
CancelVisitGuarantorEmployer.model_rebuild()
CancelVisitInsurance.model_rebuild()
CancelVisitInsuranceCompany.model_rebuild()
CancelVisitInsuranceInsured.model_rebuild()
CancelVisitLocation.model_rebuild()
CancelVisitReferringProvider.model_rebuild()
CancelVisitReferringProviderLocation.model_rebuild()
