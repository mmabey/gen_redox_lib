# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class New(EventTypeAbstractModel):
    Meta_: NewMeta = Field(..., alias="Meta")
    Order_: NewOrder = Field(..., alias="Order")
    Patient_: NewPatient = Field(..., alias="Patient")
    Visit_: NewVisit = Field(None, alias="Visit")


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
    EnteredBy_: NewOrderEnteredBy = Field(None, alias="EnteredBy")
    ID_: str = Field(..., alias="ID")
    Indications_: List[NewOrderIndication] = Field(None, alias="Indications")
    Medication_: NewOrderMedication = Field(..., alias="Medication")
    Notes_: List[str] = Field(None, alias="Notes")
    Pharmacy_: NewOrderPharmacy = Field(None, alias="Pharmacy")
    Priority_: Union[str, None] = Field(None, alias="Priority")
    Provider_: NewOrderProvider = Field(None, alias="Provider")
    VerifiedBy_: NewOrderVerifiedBy = Field(None, alias="VerifiedBy")


class NewOrderEnteredBy(RedoxAbstractModel):
    Address_: NewOrderEnteredByAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewOrderEnteredByLocation = Field(None, alias="Location")
    PhoneNumber_: NewOrderEnteredByPhoneNumber = Field(None, alias="PhoneNumber")


class NewOrderEnteredByAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewOrderEnteredByLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[NewOrderEnteredByLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewOrderEnteredByLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewOrderEnteredByLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderEnteredByLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderEnteredByPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewOrderIndication(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class NewOrderMedication(RedoxAbstractModel):
    Components_: List[NewOrderMedicationComponent] = Field(None, alias="Components")
    Dispense_: NewOrderMedicationDispense = Field(None, alias="Dispense")
    Dose_: NewOrderMedicationDose = Field(None, alias="Dose")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    FreeTextSig_: Union[str, None] = Field(None, alias="FreeTextSig")
    Frequency_: NewOrderMedicationFrequency = Field(None, alias="Frequency")
    IsPRN_: Union[bool, None] = Field(None, alias="IsPRN")
    NumberOfRefillsRemaining_: Union[float, None] = Field(
        None, alias="NumberOfRefillsRemaining"
    )
    Product_: NewOrderMedicationProduct = Field(..., alias="Product")
    Rate_: NewOrderMedicationRate = Field(None, alias="Rate")
    Route_: NewOrderMedicationRoute = Field(None, alias="Route")
    StartDate_: Union[str, None] = Field(None, alias="StartDate")


class NewOrderMedicationComponent(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Dose_: NewOrderMedicationComponentDose = Field(None, alias="Dose")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewOrderMedicationComponentDose(RedoxAbstractModel):
    Quantity_: Union[float, None] = Field(None, alias="Quantity")
    Units_: Union[str, None] = Field(None, alias="Units")


class NewOrderMedicationDispense(RedoxAbstractModel):
    Amount_: Union[float, None] = Field(None, alias="Amount")
    Units_: Union[str, None] = Field(None, alias="Units")


class NewOrderMedicationDose(RedoxAbstractModel):
    Quantity_: Union[float, None] = Field(None, alias="Quantity")
    Units_: Union[str, None] = Field(None, alias="Units")


class NewOrderMedicationFrequency(RedoxAbstractModel):
    Period_: Union[float, None] = Field(None, alias="Period")
    Unit_: Union[str, None] = Field(None, alias="Unit")


class NewOrderMedicationProduct(RedoxAbstractModel):
    AltCodes_: List[NewOrderMedicationProductAltCode] = Field(None, alias="AltCodes")
    Code_: str = Field(..., alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewOrderMedicationProductAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewOrderMedicationRate(RedoxAbstractModel):
    Quantity_: Union[float, None] = Field(None, alias="Quantity")
    Units_: Union[str, None] = Field(None, alias="Units")


class NewOrderMedicationRoute(RedoxAbstractModel):
    AltCodes_: List[NewOrderMedicationRouteAltCode] = Field(None, alias="AltCodes")
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewOrderMedicationRouteAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewOrderPharmacy(RedoxAbstractModel):
    Address_: NewOrderPharmacyAddress = Field(None, alias="Address")
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    PhoneNumber_: NewOrderPharmacyPhoneNumber = Field(None, alias="PhoneNumber")


class NewOrderPharmacyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewOrderPharmacyPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewOrderProvider(RedoxAbstractModel):
    Address_: NewOrderProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewOrderProviderLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: NewOrderProviderPhoneNumber = Field(None, alias="PhoneNumber")


class NewOrderProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewOrderProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[NewOrderProviderLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewOrderProviderLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewOrderProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewOrderVerifiedBy(RedoxAbstractModel):
    Address_: NewOrderVerifiedByAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewOrderVerifiedByLocation = Field(None, alias="Location")
    PhoneNumber_: NewOrderVerifiedByPhoneNumber = Field(None, alias="PhoneNumber")


class NewOrderVerifiedByAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewOrderVerifiedByLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewOrderVerifiedByLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[NewOrderVerifiedByLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewOrderVerifiedByLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderVerifiedByLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewOrderVerifiedByPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewPatient(RedoxAbstractModel):
    Allergies_: List[NewPatientAllergy] = Field(None, alias="Allergies")
    Demographics_: NewPatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[NewPatientIdentifier] = Field(..., alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")


class NewPatientAllergy(RedoxAbstractModel):
    AltCodes_: List[NewPatientAllergyAltCode] = Field(None, alias="AltCodes")
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Comment_: Union[str, None] = Field(None, alias="Comment")
    Criticality_: NewPatientAllergyCriticality = Field(None, alias="Criticality")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    Name_: Union[str, None] = Field(None, alias="Name")
    Reaction_: List[NewPatientAllergyReaction] = Field(None, alias="Reaction")
    Severity_: NewPatientAllergySeverity = Field(None, alias="Severity")
    StartDate_: Union[str, None] = Field(None, alias="StartDate")
    Status_: NewPatientAllergyStatus = Field(None, alias="Status")
    Substance_: NewPatientAllergySubstance = Field(None, alias="Substance")


class NewPatientAllergyAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergyCriticality(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergyReaction(RedoxAbstractModel):
    AltCodes_: List[NewPatientAllergyReactionAltCode] = Field(None, alias="AltCodes")
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")
    Severity_: NewPatientAllergyReactionSeverity = Field(None, alias="Severity")
    Text_: Union[str, None] = Field(None, alias="Text")


class NewPatientAllergyReactionAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergyReactionSeverity(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergySeverity(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergyStatus(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergySubstance(RedoxAbstractModel):
    AltCodes_: List[NewPatientAllergySubstanceAltCode] = Field(None, alias="AltCodes")
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class NewPatientAllergySubstanceAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


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
    AttendingProvider_: NewVisitAttendingProvider = Field(
        None, alias="AttendingProvider"
    )
    Insurances_: List[NewVisitInsurance] = Field(None, alias="Insurances")
    Location_: NewVisitLocation = Field(None, alias="Location")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    ReferringProvider_: NewVisitReferringProvider = Field(
        None, alias="ReferringProvider"
    )
    VisitDateTime_: Union[str, None] = Field(None, alias="VisitDateTime")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class NewVisitAttendingProvider(RedoxAbstractModel):
    Address_: NewVisitAttendingProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewVisitAttendingProviderLocation = Field(None, alias="Location")
    PhoneNumber_: NewVisitAttendingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class NewVisitAttendingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewVisitAttendingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewVisitAttendingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        NewVisitAttendingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class NewVisitInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: NewVisitInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: NewVisitInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: NewVisitInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class NewVisitInsuranceCompany(RedoxAbstractModel):
    Address_: NewVisitInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class NewVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewVisitInsuranceInsured(RedoxAbstractModel):
    Address_: NewVisitInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[NewVisitInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class NewVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


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


class NewVisitReferringProvider(RedoxAbstractModel):
    Address_: NewVisitReferringProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: NewVisitReferringProviderLocation = Field(None, alias="Location")
    PhoneNumber_: NewVisitReferringProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class NewVisitReferringProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class NewVisitReferringProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        NewVisitReferringProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        NewVisitReferringProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class NewVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class NewVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


New.model_rebuild()
NewMeta.model_rebuild()
NewOrder.model_rebuild()
NewOrderEnteredBy.model_rebuild()
NewOrderEnteredByLocation.model_rebuild()
NewOrderMedication.model_rebuild()
NewOrderMedicationComponent.model_rebuild()
NewOrderMedicationProduct.model_rebuild()
NewOrderMedicationRoute.model_rebuild()
NewOrderPharmacy.model_rebuild()
NewOrderProvider.model_rebuild()
NewOrderProviderLocation.model_rebuild()
NewOrderVerifiedBy.model_rebuild()
NewOrderVerifiedByLocation.model_rebuild()
NewPatient.model_rebuild()
NewPatientAllergy.model_rebuild()
NewPatientAllergyReaction.model_rebuild()
NewPatientAllergySubstance.model_rebuild()
NewPatientDemographics.model_rebuild()
NewVisit.model_rebuild()
NewVisitAttendingProvider.model_rebuild()
NewVisitAttendingProviderLocation.model_rebuild()
NewVisitInsurance.model_rebuild()
NewVisitInsuranceCompany.model_rebuild()
NewVisitInsuranceInsured.model_rebuild()
NewVisitLocation.model_rebuild()
NewVisitReferringProvider.model_rebuild()
NewVisitReferringProviderLocation.model_rebuild()
