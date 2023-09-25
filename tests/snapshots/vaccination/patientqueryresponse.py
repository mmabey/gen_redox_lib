# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class PatientQueryResponse(EventTypeAbstractModel):
    Meta_: PatientQueryResponseMeta = Field(..., alias="Meta")
    Patient_: PatientQueryResponsePatient = Field(None, alias="Patient")
    PotentialMatches_: List[PatientQueryResponsePotentialMatch] = Field(
        None, alias="PotentialMatches"
    )


class PatientQueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[PatientQueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[PatientQueryResponseMetaLog] = Field(None, alias="Logs")
    Message_: PatientQueryResponseMetaMessage = Field(None, alias="Message")
    Source_: PatientQueryResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: PatientQueryResponseMetaTransmission = Field(
        None, alias="Transmission"
    )


class PatientQueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PatientQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class PatientQueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PatientQueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PatientQueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PatientQueryResponsePatient(RedoxAbstractModel):
    Contacts_: List[PatientQueryResponsePatientContact] = Field(None, alias="Contacts")
    Demographics_: PatientQueryResponsePatientDemographics = Field(
        None, alias="Demographics"
    )
    Identifiers_: List[PatientQueryResponsePatientIdentifier] = Field(
        None, alias="Identifiers"
    )
    Notes_: List[str] = Field(None, alias="Notes")
    PCP_: PatientQueryResponsePatientPCP = Field(None, alias="PCP")
    Vaccinations_: List[PatientQueryResponsePatientVaccination] = Field(
        None, alias="Vaccinations"
    )


class PatientQueryResponsePatientContact(RedoxAbstractModel):
    Address_: PatientQueryResponsePatientContactAddress = Field(None, alias="Address")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: PatientQueryResponsePatientContactPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class PatientQueryResponsePatientContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePatientContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePatientDemographics(RedoxAbstractModel):
    Address_: PatientQueryResponsePatientDemographicsAddress = Field(
        None, alias="Address"
    )
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
    PhoneNumber_: PatientQueryResponsePatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class PatientQueryResponsePatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientPCP(RedoxAbstractModel):
    Address_: PatientQueryResponsePatientPCPAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PatientQueryResponsePatientPCPLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: PatientQueryResponsePatientPCPPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PatientQueryResponsePatientPCPAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePatientPCPLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PatientQueryResponsePatientPCPLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PatientQueryResponsePatientPCPLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PatientQueryResponsePatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientPCPPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePatientVaccination(RedoxAbstractModel):
    ClinicalInfo_: List[PatientQueryResponsePatientVaccinationClinicalInfo] = Field(
        None, alias="ClinicalInfo"
    )
    DateTime_: Union[str, None] = Field(None, alias="DateTime")
    Dose_: PatientQueryResponsePatientVaccinationDose = Field(None, alias="Dose")
    Location_: PatientQueryResponsePatientVaccinationLocation = Field(
        None, alias="Location"
    )
    Notes_: List[str] = Field(None, alias="Notes")
    Order_: PatientQueryResponsePatientVaccinationOrder = Field(None, alias="Order")
    Product_: PatientQueryResponsePatientVaccinationProduct = Field(
        None, alias="Product"
    )
    Provider_: PatientQueryResponsePatientVaccinationProvider = Field(
        None, alias="Provider"
    )
    RefusalReason_: Union[str, None] = Field(None, alias="RefusalReason")
    Route_: PatientQueryResponsePatientVaccinationRoute = Field(None, alias="Route")
    Site_: PatientQueryResponsePatientVaccinationSite = Field(None, alias="Site")


class PatientQueryResponsePatientVaccinationClinicalInfo(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    CompletionDateTime_: Union[str, None] = Field(None, alias="CompletionDateTime")
    Description_: Union[str, None] = Field(None, alias="Description")
    Notes_: List[str] = Field(None, alias="Notes")
    RelatedGroupID_: Union[str, None] = Field(None, alias="RelatedGroupID")
    Units_: Union[str, None] = Field(None, alias="Units")
    Value_: Union[str, None] = Field(None, alias="Value")
    ValueType_: Union[str, None] = Field(None, alias="ValueType")


class PatientQueryResponsePatientVaccinationDose(RedoxAbstractModel):
    Quantity_: Union[str, None] = Field(None, alias="Quantity")
    Units_: Union[str, None] = Field(None, alias="Units")


class PatientQueryResponsePatientVaccinationLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PatientQueryResponsePatientVaccinationLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PatientQueryResponsePatientVaccinationLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PatientQueryResponsePatientVaccinationLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationOrder(RedoxAbstractModel):
    EHRID_: Union[str, None] = Field(None, alias="EHRID")
    ID_: Union[str, None] = Field(None, alias="ID")
    Provider_: PatientQueryResponsePatientVaccinationOrderProvider = Field(
        None, alias="Provider"
    )


class PatientQueryResponsePatientVaccinationOrderProvider(RedoxAbstractModel):
    Address_: PatientQueryResponsePatientVaccinationOrderProviderAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PatientQueryResponsePatientVaccinationOrderProviderLocation = Field(
        None, alias="Location"
    )
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: PatientQueryResponsePatientVaccinationOrderProviderPhoneNumber = (
        Field(None, alias="PhoneNumber")
    )


class PatientQueryResponsePatientVaccinationOrderProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePatientVaccinationOrderProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PatientQueryResponsePatientVaccinationOrderProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PatientQueryResponsePatientVaccinationOrderProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PatientQueryResponsePatientVaccinationOrderProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationOrderProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationOrderProviderPhoneNumber(
    RedoxAbstractModel
):
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePatientVaccinationProduct(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    LotNumber_: Union[str, None] = Field(None, alias="LotNumber")
    Manufacturer_: PatientQueryResponsePatientVaccinationProductManufacturer = Field(
        None, alias="Manufacturer"
    )


class PatientQueryResponsePatientVaccinationProductManufacturer(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PatientQueryResponsePatientVaccinationProvider(RedoxAbstractModel):
    Address_: PatientQueryResponsePatientVaccinationProviderAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PatientQueryResponsePatientVaccinationProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: PatientQueryResponsePatientVaccinationProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PatientQueryResponsePatientVaccinationProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePatientVaccinationProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PatientQueryResponsePatientVaccinationProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PatientQueryResponsePatientVaccinationProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PatientQueryResponsePatientVaccinationProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePatientVaccinationProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePatientVaccinationRoute(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PatientQueryResponsePatientVaccinationSite(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class PatientQueryResponsePotentialMatch(RedoxAbstractModel):
    Contacts_: List[PatientQueryResponsePotentialMatchContact] = Field(
        None, alias="Contacts"
    )
    Demographics_: PatientQueryResponsePotentialMatchDemographics = Field(
        None, alias="Demographics"
    )
    Identifiers_: List[PatientQueryResponsePotentialMatchIdentifier] = Field(
        None, alias="Identifiers"
    )
    Notes_: List[str] = Field(None, alias="Notes")
    PCP_: PatientQueryResponsePotentialMatchPCP = Field(None, alias="PCP")


class PatientQueryResponsePotentialMatchContact(RedoxAbstractModel):
    Address_: PatientQueryResponsePotentialMatchContactAddress = Field(
        None, alias="Address"
    )
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: PatientQueryResponsePotentialMatchContactPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class PatientQueryResponsePotentialMatchContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePotentialMatchContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePotentialMatchDemographics(RedoxAbstractModel):
    Address_: PatientQueryResponsePotentialMatchDemographicsAddress = Field(
        None, alias="Address"
    )
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
    PhoneNumber_: PatientQueryResponsePotentialMatchDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class PatientQueryResponsePotentialMatchDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePotentialMatchDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PatientQueryResponsePotentialMatchIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePotentialMatchPCP(RedoxAbstractModel):
    Address_: PatientQueryResponsePotentialMatchPCPAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: PatientQueryResponsePotentialMatchPCPLocation = Field(
        None, alias="Location"
    )
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: PatientQueryResponsePotentialMatchPCPPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PatientQueryResponsePotentialMatchPCPAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PatientQueryResponsePotentialMatchPCPLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        PatientQueryResponsePotentialMatchPCPLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        PatientQueryResponsePotentialMatchPCPLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class PatientQueryResponsePotentialMatchPCPLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePotentialMatchPCPLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PatientQueryResponsePotentialMatchPCPPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


PatientQueryResponse.model_rebuild()
PatientQueryResponseMeta.model_rebuild()
PatientQueryResponsePatient.model_rebuild()
PatientQueryResponsePatientContact.model_rebuild()
PatientQueryResponsePatientDemographics.model_rebuild()
PatientQueryResponsePatientPCP.model_rebuild()
PatientQueryResponsePatientPCPLocation.model_rebuild()
PatientQueryResponsePatientVaccination.model_rebuild()
PatientQueryResponsePatientVaccinationLocation.model_rebuild()
PatientQueryResponsePatientVaccinationOrder.model_rebuild()
PatientQueryResponsePatientVaccinationOrderProvider.model_rebuild()
PatientQueryResponsePatientVaccinationOrderProviderLocation.model_rebuild()
PatientQueryResponsePatientVaccinationProduct.model_rebuild()
PatientQueryResponsePatientVaccinationProvider.model_rebuild()
PatientQueryResponsePatientVaccinationProviderLocation.model_rebuild()
PatientQueryResponsePotentialMatch.model_rebuild()
PatientQueryResponsePotentialMatchContact.model_rebuild()
PatientQueryResponsePotentialMatchDemographics.model_rebuild()
PatientQueryResponsePotentialMatchPCP.model_rebuild()
PatientQueryResponsePotentialMatchPCPLocation.model_rebuild()
