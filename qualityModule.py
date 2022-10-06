QA_parameterArray = []
# assuming that the user inputs only 4 factors
QA_parameterScalingArray = [0.25, 0.25, 0.25, 0.25]

def QA(quality, persons):
    parameter_X_weight = 0
    for i in range(len(QA_parameterScalingArray)):
        parameter_X_weight += QA_parameterArray[i] * QA_parameterScalingArray[i]
    return parameter_X_weight * quality * persons

QA_basic = 1
QAfunc = lambda value: float(value) * QA_basic
def qualityFactorsInput(qualityScalingFactorsArray):
    global qualityBasic, qualityStandard, qualityHigh, qualityPremium
    qualityBasic, qualityStandard, qualityHigh, qualityPremium = map(QAfunc, qualityScalingFactorsArray)

QA_Simple = {}
QA_Medium = {}
QA_High = {}
QA_Complex = {}

# def qualityMapping():
#     global QA_Simple, QA_Medium, QA_High, QA_Complex
#     QA_Simple = {"Entry": QA(qualityBasic), "Intermediate": QA(0.75*qualityBasic), "High": QA(0.5*qualityBasic), "Expert": QA(0.25*qualityBasic)}
#     QA_Medium = {"Entry": QA(qualityStandard), "Intermediate": QA(qualityStandard), "High": QA(qualityBasic), "Expert": QA(0.5*qualityBasic)}
#     QA_High = {"Entry": QA(qualityHigh), "Intermediate": QA(qualityHigh), "High": QA(qualityStandard), "Expert": QA(qualityBasic)}
#     QA_Complex = {"Entry": QA(qualityPremium), "Intermediate": QA(qualityPremium), "High": QA(qualityHigh), "Expert": QA(qualityStandard)}