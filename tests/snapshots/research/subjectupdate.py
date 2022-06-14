# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class SubjectUpdate(EventTypeAbstractModel):

    Enrollment: "SubjectUpdateEnrollment" = Field(None)
    Meta: "SubjectUpdateMeta" = Field(...)
    Patient: "SubjectUpdatePatient" = Field(None)
    Study: "SubjectUpdateStudy" = Field(None)


class SubjectUpdateEnrollment(RedoxAbstractModel):

    Coordinators: List["SubjectUpdateEnrollmentCoordinator"] = Field(None)
    EndDateTime: Union[str, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)
    SubjectStatus: Union[str, None] = Field(None)


class SubjectUpdateEnrollmentCoordinator(RedoxAbstractModel):

    Address: "SubjectUpdateEnrollmentCoordinatorAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "SubjectUpdateEnrollmentCoordinatorLocation" = Field(None)
    PhoneNumber: "SubjectUpdateEnrollmentCoordinatorPhoneNumber" = Field(None)


class SubjectUpdateEnrollmentCoordinatorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubjectUpdateEnrollmentCoordinatorLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubjectUpdateEnrollmentCoordinatorPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class SubjectUpdateMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["SubjectUpdateMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["SubjectUpdateMetaLog"] = Field(None)
    Message: "SubjectUpdateMetaMessage" = Field(None)
    Source: "SubjectUpdateMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "SubjectUpdateMetaTransmission" = Field(None)


class SubjectUpdateMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SubjectUpdateMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class SubjectUpdateMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class SubjectUpdateMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SubjectUpdateMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class SubjectUpdatePatient(RedoxAbstractModel):

    Demographics: "SubjectUpdatePatientDemographics" = Field(None)
    Identifiers: List["SubjectUpdatePatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class SubjectUpdatePatientDemographics(RedoxAbstractModel):

    Address: "SubjectUpdatePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "SubjectUpdatePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class SubjectUpdatePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubjectUpdatePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SubjectUpdatePatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubjectUpdateStudy(RedoxAbstractModel):

    Identifiers: List["SubjectUpdateStudyIdentifier"] = Field(None)
    Title: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubjectUpdateStudyIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


SubjectUpdate.update_forward_refs()
SubjectUpdateEnrollment.update_forward_refs()
SubjectUpdateEnrollmentCoordinator.update_forward_refs()
SubjectUpdateMeta.update_forward_refs()
SubjectUpdatePatient.update_forward_refs()
SubjectUpdatePatientDemographics.update_forward_refs()
SubjectUpdateStudy.update_forward_refs()
