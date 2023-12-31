# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class NewPatient(EventTypeAbstractModel):
    Meta_: NewPatientMeta = Field(..., alias="Meta")
    Patient_: NewPatientPatient = Field(..., alias="Patient")


class NewPatientMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[NewPatientMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[NewPatientMetaLog] = Field(None, alias="Logs")
    Message_: NewPatientMetaMessage = Field(None, alias="Message")
    Source_: NewPatientMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: NewPatientMetaTransmission = Field(None, alias="Transmission")


class NewPatientMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class NewPatientMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NewPatientMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class NewPatientPatient(RedoxAbstractModel):
    Allergies_: List[NewPatientPatientAllergy] = Field(None, alias="Allergies")
    Contacts_: List[NewPatientPatientContact] = Field(None, alias="Contacts")
    Demographics_: NewPatientPatientDemographics = Field(None, alias="Demographics")
    Guarantor_: NewPatientPatientGuarantor = Field(None, alias="Guarantor")
    Identifiers_: List[NewPatientPatientIdentifier] = Field(..., alias="Identifiers")
    Insurances_: List[NewPatientPatientInsurance] = Field(None, alias="Insurances")
    Notes_: List[str] = Field(None, alias="Notes")
    PCP_: NewPatientPatientPCP = Field(None, alias="PCP")


class NewPatientPatientAllergy(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")
    OnsetDateTime_: Union[str, None] = Field(None, alias="OnsetDateTime")
    Reaction_: List[NewPatientPatientAllergyReaction] = Field(None, alias="Reaction")
    Severity_: NewPatientPatientAllergySeverity = Field(None, alias="Severity")
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: NewPatientPatientAllergyType = Field(None, alias="Type")


class NewPatientPatientAllergyReaction(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientPatientAllergySeverity(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientPatientAllergyType(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientPatientContact(RedoxAbstractModel):
    Address_: NewPatientPatientContactAddress = Field(None, alias="Address")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: NewPatientPatientContactPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class NewPatientPatientContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class NewPatientPatientDemographics(RedoxAbstractModel):
    Address_: NewPatientPatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: NewPatientPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class NewPatientPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class NewPatientPatientGuarantor(RedoxAbstractModel):
    Address_: NewPatientPatientGuarantorAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Employer_: NewPatientPatientGuarantorEmployer = Field(None, alias="Employer")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Number_: Union[str, None] = Field(None, alias="Number")
    PhoneNumber_: NewPatientPatientGuarantorPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")
    Spouse_: NewPatientPatientGuarantorSpouse = Field(None, alias="Spouse")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewPatientPatientGuarantorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientGuarantorEmployer(RedoxAbstractModel):
    Address_: NewPatientPatientGuarantorEmployerAddress = Field(None, alias="Address")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class NewPatientPatientGuarantorEmployerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientGuarantorPhoneNumber(RedoxAbstractModel):
    Business_: Union[str, None] = Field(None, alias="Business")
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")


class NewPatientPatientGuarantorSpouse(RedoxAbstractModel):
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")


class NewPatientPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class NewPatientPatientInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: NewPatientPatientInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: NewPatientPatientInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: NewPatientPatientInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class NewPatientPatientInsuranceCompany(RedoxAbstractModel):
    Address_: NewPatientPatientInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class NewPatientPatientInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientInsuranceInsured(RedoxAbstractModel):
    Address_: NewPatientPatientInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[NewPatientPatientInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class NewPatientPatientInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewPatientPatientInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewPatientPatientPCP(RedoxAbstractModel):
    Address_: NewPatientPatientPCPAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewPatientPatientPCPLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: NewPatientPatientPCPPhoneNumber = Field(None, alias="PhoneNumber")


class NewPatientPatientPCPAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewPatientPatientPCPLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewPatientPatientPCPLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewPatientPatientPCPLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewPatientPatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewPatientPatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewPatientPatientPCPPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


NewPatient.model_rebuild()
NewPatientMeta.model_rebuild()
NewPatientPatient.model_rebuild()
NewPatientPatientAllergy.model_rebuild()
NewPatientPatientContact.model_rebuild()
NewPatientPatientDemographics.model_rebuild()
NewPatientPatientGuarantor.model_rebuild()
NewPatientPatientGuarantorEmployer.model_rebuild()
NewPatientPatientInsurance.model_rebuild()
NewPatientPatientInsuranceCompany.model_rebuild()
NewPatientPatientInsuranceInsured.model_rebuild()
NewPatientPatientPCP.model_rebuild()
NewPatientPatientPCPLocation.model_rebuild()
