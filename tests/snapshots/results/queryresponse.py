# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class QueryResponse(EventTypeAbstractModel):
    Meta_: QueryResponseMeta = Field(..., alias="Meta")
    Orders_: List[QueryResponseOrder] = Field(None, alias="Orders")


class QueryResponseMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[QueryResponseMetaDestination] = Field(
        None, alias="Destinations"
    )
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[QueryResponseMetaLog] = Field(None, alias="Logs")
    Message_: QueryResponseMetaMessage = Field(None, alias="Message")
    Source_: QueryResponseMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: QueryResponseMetaTransmission = Field(None, alias="Transmission")


class QueryResponseMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class QueryResponseMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class QueryResponseMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class QueryResponseMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class QueryResponseMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class QueryResponseOrder(RedoxAbstractModel):
    ApplicationOrderID_: Union[str, None] = Field(None, alias="ApplicationOrderID")
    CollectionDateTime_: Union[str, None] = Field(None, alias="CollectionDateTime")
    CompletionDateTime_: Union[str, None] = Field(None, alias="CompletionDateTime")
    ID_: Union[str, None] = Field(None, alias="ID")
    LastUpdated_: Union[str, None] = Field(None, alias="LastUpdated")
    Notes_: List[str] = Field(None, alias="Notes")
    Patient_: QueryResponseOrderPatient = Field(None, alias="Patient")
    Priority_: Union[str, None] = Field(None, alias="Priority")
    Procedure_: QueryResponseOrderProcedure = Field(None, alias="Procedure")
    Provider_: QueryResponseOrderProvider = Field(None, alias="Provider")
    ResponseFlag_: Union[str, None] = Field(None, alias="ResponseFlag")
    ResultCopyProviders_: List[QueryResponseOrderResultCopyProvider] = Field(
        None, alias="ResultCopyProviders"
    )
    Results_: List[QueryResponseOrderResult] = Field(None, alias="Results")
    ResultsStatus_: Union[str, None] = Field(None, alias="ResultsStatus")
    Status_: Union[str, None] = Field(None, alias="Status")
    TransactionDateTime_: Union[str, None] = Field(None, alias="TransactionDateTime")
    Visit_: QueryResponseOrderVisit = Field(None, alias="Visit")


class QueryResponseOrderPatient(RedoxAbstractModel):
    Identifiers_: List[QueryResponseOrderPatientIdentifier] = Field(
        None, alias="Identifiers"
    )


class QueryResponseOrderPatientIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class QueryResponseOrderProvider(RedoxAbstractModel):
    Address_: QueryResponseOrderProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: QueryResponseOrderProviderLocation = Field(None, alias="Location")
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: QueryResponseOrderProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class QueryResponseOrderProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrderProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        QueryResponseOrderProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        QueryResponseOrderProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class QueryResponseOrderProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class QueryResponseOrderResult(RedoxAbstractModel):
    AbnormalFlag_: Union[str, None] = Field(None, alias="AbnormalFlag")
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    CompletionDateTime_: Union[str, None] = Field(None, alias="CompletionDateTime")
    Description_: Union[str, None] = Field(None, alias="Description")
    FileType_: Union[str, None] = Field(None, alias="FileType")
    Notes_: List[str] = Field(None, alias="Notes")
    ObservationMethod_: QueryResponseOrderResultObservationMethod = Field(
        None, alias="ObservationMethod"
    )
    Performer_: QueryResponseOrderResultPerformer = Field(None, alias="Performer")
    PrimaryResultsInterpreter_: QueryResponseOrderResultPrimaryResultsInterpreter = (
        Field(None, alias="PrimaryResultsInterpreter")
    )
    Producer_: QueryResponseOrderResultProducer = Field(None, alias="Producer")
    ReferenceRange_: QueryResponseOrderResultReferenceRange = Field(
        None, alias="ReferenceRange"
    )
    RelatedGroupID_: Union[str, None] = Field(None, alias="RelatedGroupID")
    Specimen_: QueryResponseOrderResultSpecimen = Field(None, alias="Specimen")
    Status_: Union[str, None] = Field(None, alias="Status")
    Units_: Union[str, None] = Field(None, alias="Units")
    Value_: Union[str, None] = Field(None, alias="Value")
    ValueType_: Union[str, None] = Field(None, alias="ValueType")


class QueryResponseOrderResultCopyProvider(RedoxAbstractModel):
    Address_: QueryResponseOrderResultCopyProviderAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: QueryResponseOrderResultCopyProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: QueryResponseOrderResultCopyProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class QueryResponseOrderResultCopyProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrderResultCopyProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        QueryResponseOrderResultCopyProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        QueryResponseOrderResultCopyProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class QueryResponseOrderResultCopyProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultCopyProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultCopyProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class QueryResponseOrderResultObservationMethod(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")


class QueryResponseOrderResultPerformer(RedoxAbstractModel):
    Address_: QueryResponseOrderResultPerformerAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: QueryResponseOrderResultPerformerLocation = Field(None, alias="Location")
    PhoneNumber_: QueryResponseOrderResultPerformerPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class QueryResponseOrderResultPerformerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrderResultPerformerLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        QueryResponseOrderResultPerformerLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        QueryResponseOrderResultPerformerLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class QueryResponseOrderResultPerformerLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultPerformerLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultPerformerPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class QueryResponseOrderResultPrimaryResultsInterpreter(RedoxAbstractModel):
    Address_: QueryResponseOrderResultPrimaryResultsInterpreterAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: QueryResponseOrderResultPrimaryResultsInterpreterLocation = Field(
        None, alias="Location"
    )
    NPI_: Union[str, None] = Field(None, alias="NPI")
    PhoneNumber_: QueryResponseOrderResultPrimaryResultsInterpreterPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class QueryResponseOrderResultPrimaryResultsInterpreterAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrderResultPrimaryResultsInterpreterLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        QueryResponseOrderResultPrimaryResultsInterpreterLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        QueryResponseOrderResultPrimaryResultsInterpreterLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class QueryResponseOrderResultPrimaryResultsInterpreterLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultPrimaryResultsInterpreterLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class QueryResponseOrderResultPrimaryResultsInterpreterPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class QueryResponseOrderResultProducer(RedoxAbstractModel):
    Address_: QueryResponseOrderResultProducerAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")


class QueryResponseOrderResultProducerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class QueryResponseOrderResultReferenceRange(RedoxAbstractModel):
    High_: Union[float, None] = Field(None, alias="High")
    Low_: Union[float, None] = Field(None, alias="Low")
    Text_: Union[str, None] = Field(None, alias="Text")


class QueryResponseOrderResultSpecimen(RedoxAbstractModel):
    BodySite_: Union[str, None] = Field(None, alias="BodySite")
    ID_: Union[str, None] = Field(None, alias="ID")
    Source_: Union[str, None] = Field(None, alias="Source")


class QueryResponseOrderVisit(RedoxAbstractModel):
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


QueryResponse.model_rebuild()
QueryResponseMeta.model_rebuild()
QueryResponseOrder.model_rebuild()
QueryResponseOrderPatient.model_rebuild()
QueryResponseOrderProvider.model_rebuild()
QueryResponseOrderProviderLocation.model_rebuild()
QueryResponseOrderResult.model_rebuild()
QueryResponseOrderResultCopyProvider.model_rebuild()
QueryResponseOrderResultCopyProviderLocation.model_rebuild()
QueryResponseOrderResultPerformer.model_rebuild()
QueryResponseOrderResultPerformerLocation.model_rebuild()
QueryResponseOrderResultPrimaryResultsInterpreter.model_rebuild()
QueryResponseOrderResultPrimaryResultsInterpreterLocation.model_rebuild()
QueryResponseOrderResultProducer.model_rebuild()
