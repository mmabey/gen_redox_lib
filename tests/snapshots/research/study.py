# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Study(EventTypeAbstractModel):
    Meta_: StudyMeta = Field(..., alias="Meta")
    Protocols_: List[StudyProtocol] = Field(None, alias="Protocols")
    Study_: StudyStudy = Field(None, alias="Study")


class StudyMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[StudyMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[StudyMetaLog] = Field(None, alias="Logs")
    Message_: StudyMetaMessage = Field(None, alias="Message")
    Source_: StudyMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: StudyMetaTransmission = Field(None, alias="Transmission")


class StudyMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class StudyMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class StudyMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class StudyMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class StudyMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class StudyProtocol(RedoxAbstractModel):
    Cycles_: List[StudyProtocolCycle] = Field(None, alias="Cycles")
    Description_: Union[str, None] = Field(None, alias="Description")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyProtocolCycle(RedoxAbstractModel):
    Days_: List[StudyProtocolCycleDay] = Field(None, alias="Days")
    Description_: Union[str, None] = Field(None, alias="Description")
    EndDate_: Union[str, None] = Field(None, alias="EndDate")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    StartDate_: Union[str, None] = Field(None, alias="StartDate")


class StudyProtocolCycleDay(RedoxAbstractModel):
    ActivityDateTime_: Union[str, None] = Field(None, alias="ActivityDateTime")
    Description_: Union[str, None] = Field(None, alias="Description")
    EarliestDateTime_: Union[str, None] = Field(None, alias="EarliestDateTime")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LatestDateTime_: Union[str, None] = Field(None, alias="LatestDateTime")
    Procedures_: List[StudyProtocolCycleDayProcedure] = Field(None, alias="Procedures")


class StudyProtocolCycleDayProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSet_: Union[str, None] = Field(None, alias="CodeSet")
    Description_: Union[str, None] = Field(None, alias="Description")
    Modifiers_: List[str] = Field(None, alias="Modifiers")


class StudyStudy(RedoxAbstractModel):
    Conditions_: List[StudyStudyCondition] = Field(None, alias="Conditions")
    Coordinators_: List[StudyStudyCoordinator] = Field(None, alias="Coordinators")
    Description_: Union[str, None] = Field(None, alias="Description")
    Design_: StudyStudyDesign = Field(None, alias="Design")
    Eligibility_: StudyStudyEligibility = Field(None, alias="Eligibility")
    Identifiers_: List[StudyStudyIdentifier] = Field(None, alias="Identifiers")
    Location_: StudyStudyLocation = Field(None, alias="Location")
    PrincipalInvestigator_: StudyStudyPrincipalInvestigator = Field(
        None, alias="PrincipalInvestigator"
    )
    Sponsor_: StudyStudySponsor = Field(None, alias="Sponsor")
    StartDateTime_: Union[str, None] = Field(None, alias="StartDateTime")
    Status_: Union[str, None] = Field(None, alias="Status")
    Title_: Union[str, None] = Field(None, alias="Title")
    Type_: Union[str, None] = Field(None, alias="Type")


class StudyStudyCondition(RedoxAbstractModel):
    AltCodes_: List[StudyStudyConditionAltCode] = Field(None, alias="AltCodes")
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class StudyStudyConditionAltCode(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSystem_: Union[str, None] = Field(None, alias="CodeSystem")
    CodeSystemName_: Union[str, None] = Field(None, alias="CodeSystemName")
    Name_: Union[str, None] = Field(None, alias="Name")


class StudyStudyCoordinator(RedoxAbstractModel):
    Address_: StudyStudyCoordinatorAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: StudyStudyCoordinatorLocation = Field(None, alias="Location")
    PhoneNumber_: StudyStudyCoordinatorPhoneNumber = Field(None, alias="PhoneNumber")


class StudyStudyCoordinatorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class StudyStudyCoordinatorLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        StudyStudyCoordinatorLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[StudyStudyCoordinatorLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class StudyStudyCoordinatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyCoordinatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyCoordinatorPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class StudyStudyDesign(RedoxAbstractModel):
    Phase_: Union[str, None] = Field(None, alias="Phase")
    Purpose_: Union[str, None] = Field(None, alias="Purpose")


class StudyStudyEligibility(RedoxAbstractModel):
    Gender_: Union[str, None] = Field(None, alias="Gender")
    MaximumAge_: Union[float, None] = Field(None, alias="MaximumAge")
    MinimumAge_: Union[float, None] = Field(None, alias="MinimumAge")


class StudyStudyIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyLocation(RedoxAbstractModel):
    Address_: StudyStudyLocationAddress = Field(None, alias="Address")
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[StudyStudyLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[StudyStudyLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class StudyStudyLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class StudyStudyLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyPrincipalInvestigator(RedoxAbstractModel):
    Address_: StudyStudyPrincipalInvestigatorAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: StudyStudyPrincipalInvestigatorLocation = Field(None, alias="Location")
    PhoneNumber_: StudyStudyPrincipalInvestigatorPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class StudyStudyPrincipalInvestigatorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class StudyStudyPrincipalInvestigatorLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        StudyStudyPrincipalInvestigatorLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        StudyStudyPrincipalInvestigatorLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class StudyStudyPrincipalInvestigatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyPrincipalInvestigatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class StudyStudyPrincipalInvestigatorPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class StudyStudySponsor(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


Study.model_rebuild()
StudyMeta.model_rebuild()
StudyProtocol.model_rebuild()
StudyProtocolCycle.model_rebuild()
StudyProtocolCycleDay.model_rebuild()
StudyStudy.model_rebuild()
StudyStudyCondition.model_rebuild()
StudyStudyCoordinator.model_rebuild()
StudyStudyCoordinatorLocation.model_rebuild()
StudyStudyLocation.model_rebuild()
StudyStudyPrincipalInvestigator.model_rebuild()
StudyStudyPrincipalInvestigatorLocation.model_rebuild()
