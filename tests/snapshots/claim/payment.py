# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Payment(EventTypeAbstractModel):
    Meta_: PaymentMeta = Field(..., alias="Meta")
    Payee_: PaymentPayee = Field(None, alias="Payee")
    Payer_: PaymentPayer = Field(None, alias="Payer")
    Payments_: List[PaymentPayment] = Field(..., alias="Payments")
    Transaction_: PaymentTransaction = Field(None, alias="Transaction")


class PaymentMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[PaymentMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[PaymentMetaLog] = Field(None, alias="Logs")
    Message_: PaymentMetaMessage = Field(None, alias="Message")
    Source_: PaymentMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: PaymentMetaTransmission = Field(None, alias="Transmission")


class PaymentMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PaymentMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class PaymentMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PaymentMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class PaymentMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class PaymentPayee(RedoxAbstractModel):
    Address_: PaymentPayeeAddress = Field(None, alias="Address")
    EmailAddress_: Union[str, None] = Field(None, alias="EmailAddress")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: PaymentPayeePhoneNumber = Field(None, alias="PhoneNumber")


class PaymentPayeeAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PaymentPayeePhoneNumber(RedoxAbstractModel):
    Fax_: Union[str, None] = Field(None, alias="Fax")
    Office_: Union[str, None] = Field(None, alias="Office")


class PaymentPayer(RedoxAbstractModel):
    Address_: PaymentPayerAddress = Field(None, alias="Address")
    EmailAddress_: Union[str, None] = Field(None, alias="EmailAddress")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: PaymentPayerPhoneNumber = Field(None, alias="PhoneNumber")


class PaymentPayerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PaymentPayerPhoneNumber(RedoxAbstractModel):
    Fax_: Union[str, None] = Field(None, alias="Fax")
    Office_: Union[str, None] = Field(None, alias="Office")


class PaymentPayment(RedoxAbstractModel):
    Claim_: PaymentPaymentClaim = Field(None, alias="Claim")
    DateTime_: Union[str, None] = Field(None, alias="DateTime")
    Patient_: PaymentPaymentPatient = Field(..., alias="Patient")


class PaymentPaymentClaim(RedoxAbstractModel):
    Adjustments_: List[PaymentPaymentClaimAdjustment] = Field(None, alias="Adjustments")
    ChargedAmount_: Union[str, None] = Field(None, alias="ChargedAmount")
    Number_: Union[str, None] = Field(None, alias="Number")
    PatientResponsibilityAmount_: Union[str, None] = Field(
        None, alias="PatientResponsibilityAmount"
    )
    PaymentAmount_: Union[str, None] = Field(None, alias="PaymentAmount")
    ReceivedDate_: Union[str, None] = Field(None, alias="ReceivedDate")
    ReferenceNumbers_: List[PaymentPaymentClaimReferenceNumber] = Field(
        None, alias="ReferenceNumbers"
    )
    ServiceDateTime_: Union[str, None] = Field(None, alias="ServiceDateTime")
    ServiceEndDateTime_: Union[str, None] = Field(None, alias="ServiceEndDateTime")
    Services_: List[PaymentPaymentClaimService] = Field(None, alias="Services")
    Status_: Union[str, None] = Field(None, alias="Status")
    SubmissionNumber_: Union[str, None] = Field(None, alias="SubmissionNumber")


class PaymentPaymentClaimAdjustment(RedoxAbstractModel):
    Amount_: Union[str, None] = Field(None, alias="Amount")
    Quantity_: Union[str, None] = Field(None, alias="Quantity")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    ReasonGroup_: Union[str, None] = Field(None, alias="ReasonGroup")


class PaymentPaymentClaimReferenceNumber(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PaymentPaymentClaimService(RedoxAbstractModel):
    AdjudicatedProcedure_: PaymentPaymentClaimServiceAdjudicatedProcedure = Field(
        None, alias="AdjudicatedProcedure"
    )
    AllowedAmount_: Union[str, None] = Field(None, alias="AllowedAmount")
    ChargedAmount_: Union[str, None] = Field(None, alias="ChargedAmount")
    ChargedUnits_: Union[str, None] = Field(None, alias="ChargedUnits")
    DeductibleAmount_: Union[str, None] = Field(None, alias="DeductibleAmount")
    PaymentAmount_: Union[str, None] = Field(None, alias="PaymentAmount")
    PaymentUnits_: Union[str, None] = Field(None, alias="PaymentUnits")
    ReferenceNumbers_: List[PaymentPaymentClaimServiceReferenceNumber] = Field(
        None, alias="ReferenceNumbers"
    )
    ServiceDateTime_: Union[str, None] = Field(None, alias="ServiceDateTime")
    ServiceEndDateTime_: Union[str, None] = Field(None, alias="ServiceEndDateTime")
    SubmittedProcedure_: PaymentPaymentClaimServiceSubmittedProcedure = Field(
        None, alias="SubmittedProcedure"
    )


class PaymentPaymentClaimServiceAdjudicatedProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSet_: Union[str, None] = Field(None, alias="CodeSet")
    Modifiers_: List[str] = Field(None, alias="Modifiers")
    Name_: Union[str, None] = Field(None, alias="Name")


class PaymentPaymentClaimServiceReferenceNumber(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class PaymentPaymentClaimServiceSubmittedProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    CodeSet_: Union[str, None] = Field(None, alias="CodeSet")
    Modifiers_: List[str] = Field(None, alias="Modifiers")
    Name_: Union[str, None] = Field(None, alias="Name")


class PaymentPaymentPatient(RedoxAbstractModel):
    Demographics_: PaymentPaymentPatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[PaymentPaymentPatientIdentifier] = Field(
        ..., alias="Identifiers"
    )
    Notes_: List[str] = Field(None, alias="Notes")


class PaymentPaymentPatientDemographics(RedoxAbstractModel):
    Address_: PaymentPaymentPatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: PaymentPaymentPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class PaymentPaymentPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class PaymentPaymentPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class PaymentPaymentPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class PaymentTransaction(RedoxAbstractModel):
    CreditOrDebit_: Union[str, None] = Field(None, alias="CreditOrDebit")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    PaymentDateTime_: Union[str, None] = Field(None, alias="PaymentDateTime")
    PaymentMethod_: Union[str, None] = Field(None, alias="PaymentMethod")
    Receiver_: PaymentTransactionReceiver = Field(None, alias="Receiver")
    Submitter_: PaymentTransactionSubmitter = Field(None, alias="Submitter")
    TotalPaymentAmount_: Union[str, None] = Field(None, alias="TotalPaymentAmount")
    TrackingNumber_: Union[str, None] = Field(None, alias="TrackingNumber")
    Type_: Union[str, None] = Field(None, alias="Type")


class PaymentTransactionReceiver(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")


class PaymentTransactionSubmitter(RedoxAbstractModel):
    EmailAddress_: Union[str, None] = Field(None, alias="EmailAddress")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: PaymentTransactionSubmitterPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class PaymentTransactionSubmitterPhoneNumber(RedoxAbstractModel):
    Fax_: Union[str, None] = Field(None, alias="Fax")
    Office_: Union[str, None] = Field(None, alias="Office")


Payment.model_rebuild()
PaymentMeta.model_rebuild()
PaymentPayee.model_rebuild()
PaymentPayer.model_rebuild()
PaymentPayment.model_rebuild()
PaymentPaymentClaim.model_rebuild()
PaymentPaymentClaimService.model_rebuild()
PaymentPaymentPatient.model_rebuild()
PaymentPaymentPatientDemographics.model_rebuild()
PaymentTransaction.model_rebuild()
PaymentTransactionSubmitter.model_rebuild()
