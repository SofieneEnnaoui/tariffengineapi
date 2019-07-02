from typing import List, Dict

from pydantic import BaseModel
from fastapi import Body


class Car(BaseModel):
    Age: int
    CarRisk: float


class Driver(BaseModel):
    Age: int
    BonusMalus: float


class Zone(BaseModel):
    Zipcode: str
    GeoRisk: float


class InputDarwin(BaseModel):
    CorrelationId: str
    FirstCar: Car
    FirstDriver: Driver
    ResidencyZone: Zone


input_darwin_example = Body(
    ...,
    example={
        "CorrelationId": "0f377fa1-c7ad-4824-8b70-842fc196209d",
        "FirstCar": {
            "Age": 10,
            "CarRisk": 0.125
        },
        "FirstDriver": {
            "Age": 25,
            "BonusMalus": 0.5
        },
        "ResidencyZone": {
            "Zipcode": "75001",
            "GeoRisk": 0.235
        }
    }
)


class Coverage(BaseModel):
    GrossAmount: float
    NetAmount: float
    Type: str


class Period(BaseModel):
    Name: str
    PremiumInclTaxes: float
    PremiumLoaded: float


class Pack(BaseModel):
    Name: str
    Periods: List[Period]


class Formula(BaseModel):
    Name: str
    Packs: List[Pack]


class OutputDarwin(BaseModel):
    CorrelationId: str
    Coverages: List[Coverage]
    Formulas: List[Formula]


class Attribute(BaseModel):
    Name: str
    Current: str = None
    Old: str = None
    Last: str = None


class InputAPI(BaseModel):
    CorrelationId: str
    EngineVersion: str
    PreviousEngineVersion: str
    ProductInterfaceStorageId: int
    Attributes: List[Attribute]


class OutputAPI(BaseModel):
    CorrelationId: str
    EngineVersion: str
    PreviousEngineVersion: str
    ProductInterfaceStorageId: int
    Attributes: List[Attribute]


input_api_example = Body(
    ...,
    example={
        "CorrelationId": "00000000-0000-0000-0000-000000000000",
        "EngineVersion": "FR_TA_V2",
        "PreviousEngineVersion": "FR_TA_V1",
        "ProductInterfaceStorageId": -1,
        "Attributes":
            [
                {'Name': 'ClaimInfo.NumberInYear', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ClaimInfo.NumberInYearMinus1', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ClaimInfo.NumberInYearMinus2', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor1In', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor2In', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor3In', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor4In', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.QuoteCalculationMode', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.RealSelectedPackage', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[DeductibleUpgrade].SelectedLevel', 'Current': '3.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[GroupProtection].SelectedLevel', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[GroupSerenity].SelectedLevel', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[GroupTranquility].SelectedLevel', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[LoanOption].SelectedLevel', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'EndorsementFees.SelectedLevel', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'EndorsementFees.SelectedLevelNotOverruled', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'IsRefactoringCalculationActivated', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].AccelerationRatio', 'Current': '15.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].BodyTypeId', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].BrandId', 'Current': '8.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaAge', 'Current': '26.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaAgeAtPurchase', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaRetentionYears', 'Current': '23.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaRiskClassTheftSpecific', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].FinancingTypeId', 'Current': '6.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].FiscalPower', 'Current': '7.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].FuelFeedSystemId', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].FuelId', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].GearBoxId', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].GreenOfferExtendedActivationPeriodEndDate', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].GreenOfferPeriodActivated', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlass_F', 'Current': '11.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlass_S', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlobal_Density', 'Current': '113.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlobal_Rain', 'Current': '161.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlobal_Temperature', 'Current': '17.1', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskGlobal_Unemployment', 'Current': '0.06', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskOwnDamage_F', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskOwnDamage_S', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskOwnDamageV2_F', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskOwnDamageV2_S', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTheft', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTPL', 'Current': '3.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTPLBI_F', 'Current': '106.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTPLBI_LL_F', 'Current': '106.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTPLBI_LL_S', 'Current': '106.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].HomeParkingGeoRiskTPLM_F', 'Current': '3.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].IsHighRisk', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].KindId', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].LateralFrontAirBagId', 'Current': '-1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].LateralRearAirBagId', 'Current': '-1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].ModelId', 'Current': '16.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].PowerGroupId', 'Current': '32.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].PowerHP', 'Current': '100.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].PriceGroupId', 'Current': '12.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].RepairGroupId', 'Current': '14.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].RiskClassRadar', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].RiskClassTheft', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].Segment1', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].SpeedLimit', 'Current': '195.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].TransmissionId', 'Current': '3.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].UsageId', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].UsualParkingTypeId', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].Weight', 'Current': '1190.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.ABTestVariable', 'Current': '8142137.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CopyPolicyReasonId', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CopyPolicyTypeId', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CorrectivePremiumCalculated', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaAdditionalDeclaredNumber', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaAverageNumberOfKmAYear', 'Current': '10000.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaClaimHistoryTypeId', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaClaimsNumberPriorToInsuring', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaClaimsNumberSinceInsured', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaCorrectivePremium', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaD2Age', 'Current': '51.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaD2DrivingLicenceAge', 'Current': '33.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaDepartment', 'Current': '31.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaGlassNumberAtSubscription', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaIncrement_Car_PowerGroup', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaIncrement_Car_PriceGroup', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaIncrement_CarAge', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaPaymentIncidentsNumberInYear', 'Current': '-1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaPaymentIncidentsNumberInYearMinus1', 'Current': '-1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaPaymentIncidentsNumberInYearMinus2', 'Current': '-1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CriteriaRejection', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.CriteriaTheftNumberAtSubscription', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlass_F', 'Current': '11.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlass_S', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_Density', 'Current': '113.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_F', 'Current': '7.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_S', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_Temperature', 'Current': '17.1', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_Unemployment', 'Current': '0.06', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskGlobal_WorkingDistance', 'Current': '125.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskOwnDamage_F', 'Current': '7.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskOwnDamage_S', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskOwnDamageV2_F', 'Current': '6.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskOwnDamageV2_S', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskTheft', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskTPL', 'Current': '8.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskTPLBI_F', 'Current': '106.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GeoRiskTPLM_F', 'Current': '9.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOfferEligibleForF1', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOfferEligibleForF2', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOfferEligibleForF3', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOfferEligibleForF4', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.InsuringReasonId', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.IsInReinstatementAndRenewal', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.IsTelematics', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.MonthlyDerogationCoeffId', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.OrientationScoreToPartnerGarage', 'Current': '3.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.OriginalIsTelematics', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.PolicyEventId', 'Current': '13.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.PolicyStateId', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.TodayDate', 'Current': '43523.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.YearsInForce', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared1].BirthDate', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared1].DrivingLearningMethodId', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared2].BirthDate', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared2].DrivingLearningMethodId', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].Age', 'Current': '51.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].AgeAtDrivingLicenceObtention', 'Current': '18.67', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].CalculatedBonusMalusStep', 'Current': '50.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].CalculatedYearsAtMaxBonus', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].ChildrenSegment', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaCommercialBonusMalusStep', 'Current': '50.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaMaritalStatusId', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaOccupationId', 'Current': '17.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaPreviousInsuranceHistory', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaTotalCarsInHouseHOld', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].DriverPreviousInsCancellation2ReasonId', 'Current': '4.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].DrivingLicenceAge', 'Current': '32.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].FlashQuoteAge', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].FlashQuoteHasBonusMalus50', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].FlashQuotePreviousInsuranceHistoryId', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].HasBonusMalusToBeFastlyImproved', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].HasMaxBonusForever', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].HasMultipleWorkLocations', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D1].OccupationId', 'Current': '12.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[D2].RelationshipToFirstDriverId', 'Current': '13.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[Conquest].CalculationTypeId', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[Conquest].CalculationValue', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[Conquest].IsSelected', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[EmployeeAdvantage].CalculationValue', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[EmployeeAdvantage].IsSelected', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectOffer[NewDriver].IsSelected', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPolicyHOlder.CreditScore', 'Current': '647.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPolicyHOlder.CriteriaDependentChildrenNumber', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPolicyHOlder.IsEmployee', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPolicyHOlder.IsMontlyFrequencyAllowed', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPolicyHOlder.SubCancelationScoreMonthly.LastValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPolicyHOlder.SubCancelationScoreYearly.LastValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPortfolioProtection.ActionId', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.CalculationStep', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.CriteriaClaimHistoryTypeId', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPortfolioProtection.FactorIn', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.GlobalFactor', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.InitialStartDate', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.PremiumPackageNetOfTax', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPortfolioProtection.SubscriptionFactor', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectPortfolioProtection.YearsInForce', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectProcess.AccessMode', 'Current': '2.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectProcess.GFCalculationStep', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectProcess.IsMigrationInProgress', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.CapCurrent', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.CapNewBusinessPremiumCurrent', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.FloorCurrent', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.IntermediaryFactorIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.NewBusinessFactorAtRenewalIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumBeforeMigrationNetOfTax', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumIntermediaryInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumIntermediaryNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumNewBusinessInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumNewBusinessNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalAutInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalAutNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisAutInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisAutNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalInclTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalNetOfTaxIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.RenewalStep', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectThermometer.IsLongLifeOfferAccepted', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectThermometer.LongLifeCurrentAmount', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectThermometer.LongLifeInitialAmountIn', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'ObjectThermometer.LongLifeNotUsingGlobalFactorAmountIn', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectThermometer.LongLifeUsingGlobalFactorAmountIn', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'PaymentPeriod', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'SelectedPackage', 'Current': '111.0', 'Old': None, 'Last': None},
                {'Name': 'TaxAmountTA', 'Current': '5.9', 'Old': None, 'Last': None},
                {'Name': 'TaxRateCFG_TPL', 'Current': '0.02', 'Old': None, 'Last': None},
                {'Name': 'TaxRateCSS_TPL', 'Current': '0.15', 'Old': None, 'Last': None},
                {'Name': 'TaxRateTCAA', 'Current': '0.18', 'Old': None, 'Last': None},
                {'Name': 'TaxRateTCAA_TPL', 'Current': '0.18', 'Old': None, 'Last': None},
                {'Name': 'TaxRateTCAP', 'Current': '0.09', 'Old': None, 'Last': None},
                {'Name': 'TaxRateTCAP_LP', 'Current': '0.134', 'Old': None, 'Last': None},
                {'Name': 'TaxRateVAT', 'Current': '0.2', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.PremiumIncOptionsInclTaxes.OldValue', 'Current': '250.49', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo.PremiumIncOptionsTaxes.OldValue', 'Current': '47.35', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.PremiumPackageInclTaxes.OldValue', 'Current': '157.18', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[CourtesyCar].PremiumMarket.OldValue', 'Current': '15.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[DeductibleUpgrade].PremiumMarket.OldValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[DriverProtection].PremiumMarket.OldValue', 'Current': '17.79', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[DriverProtectionUpgrade].PremiumMarket.OldValue', 'Current': '47.07', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[FireExplosion].PremiumMarket.OldValue', 'Current': '0.93', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[Glass].PremiumMarket.OldValue', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[HandlingCosts].PremiumMarket.OldValue', 'Current': '34.98', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[LegalProtection].PremiumMarket.OldValue', 'Current': '0.93', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[Loyalty].PremiumMarket.OldValue', 'Current': '', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[NaturalCatastrophy].PremiumMarket.OldValue', 'Current': '0.11', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[Nature].PremiumMarket.OldValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[OwnDamage].PremiumMarket.OldValue', 'Current': '6.55', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[Recovery].PremiumMarket.OldValue', 'Current': '3.81', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[RoadsideAssistanceBasic].PremiumMarket.OldValue', 'Current': '5.72', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[RoadsideAssistanceUpgrade].PremiumMarket.OldValue', 'Current': '20.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[TechnicalCatastrophy].PremiumMarket.OldValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[Theft].PremiumMarket.OldValue', 'Current': '0.93', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[TPLMandatoryBodyInjury].PremiumMarket.OldValue', 'Current': '29.91', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[TPLMandatoryMaterial].PremiumMarket.OldValue', 'Current': '15.41', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaAge.OldValue', 'Current': '26.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaPreviousCarRetentionYears.OldValue', 'Current': '11.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectCar[C1].CriteriaRetentionYears.OldValue', 'Current': '23.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].PowerGroupId.OldValue', 'Current': '32.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectCar[C1].PriceGroupId.OldValue', 'Current': '12.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclared1Coefficient.OldValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclared2Coefficient.OldValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclaredDriversCoeff.OldValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.GlobalFactor.OldValue', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOfferSelected.OldValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GreenOffferCoefficient.OldValue', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared1].BirthDate.OldValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared2].BirthDate.OldValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].CalculatedBonusMalusStep.OldValue', 'Current': '50.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[D1].CriteriaCommercialBonusMalusStep.OldValue', 'Current': '50.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectThermometer.LongLifeLast1GlobalFactorTheo.OldValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'PaymentPeriod.OldValue', 'Current': '4.0', 'Old': None, 'Last': None},
                {'Name': 'SelectedPackage.OldValue', 'Current': '111.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor1.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor2.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor3.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.GFTheoFactor4.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo.PremiumBeforeRenewalIncOptionsInclTaxes.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo.PremiumBeforeRenewalIncOptionsNetOfTax.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[GroupSerenity].SelectedLevel.LastValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'CoverInfo[LoanOption].IsAvailable.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[Loyalty].SelectedLevel.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'CoverInfo[TerroristAttack].Tax[TA].Amount.LastValue', 'Current': '5.9', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclared1Coefficient.LastValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclared2Coefficient.LastValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.AdditionalDeclaredDriversCoeff.LastValue', 'Current': '1.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectContract.CarChangeFactor.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.GlobalFactor.LastValue', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.PolicyStateId.LastValue', 'Current': '5.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectContract.SubscriptionFactor.LastValue', 'Current': '1.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared1].BirthDate.LastValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectDriver[AdditionalDeclared2].BirthDate.LastValue', 'Current': '', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectPortfolioProtection.CloseTarifTheoreticalFactor.LastValue', 'Current': '-1.0',
                 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.CapCalculated.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.FloorCalculated.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.IntermediaryFactorOut.LastValue', 'Current': '0.0', 'Old': None, 'Last': None},
                {'Name': 'ObjectRenewal.NewBusinessFactorAtRenewalOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumIntermediaryInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumIntermediaryNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumNewBusinessInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumNewBusinessNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalAutInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalAutNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisAutInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisAutNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalBisNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalInclTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectRenewal.PremiumTheoreticalNetOfTaxOut.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'ObjectThermometer.IsLongLifeOfferAccepted.LastValue', 'Current': '0.0', 'Old': None,
                 'Last': None},
                {'Name': 'SelectedPackage.LastValue', 'Current': '111.0', 'Old': None, 'Last': None}
            ]

    }
)
