# assuming that the user inputs only 4 factors
Q_parameterScalingArray = [0.25, 0.25, 0.25, 0.25]

def Q(quality, persons, Q_parameterArray):
    parameter_X_weight = 0
    for i in range(len(Q_parameterArray)):
        parameter_X_weight += Q_parameterArray[i] * Q_parameterScalingArray[i]
    return parameter_X_weight * quality * persons

Q_basic = 1
Qfunc = lambda value: float(value) * Q_basic
def qualityFactorsInput(qualityScalingFactorsArray):
    global qualityBasic, qualityStandard, qualityHigh, qualityPremium
    qualityBasic, qualityStandard, qualityHigh, qualityPremium = map(Qfunc, qualityScalingFactorsArray)

Q_Simple = {}
Q_Medium = {}
Q_High = {}
Q_Complex = {}

# def qualityMapping():
#     global Q_Simple, Q_Medium, Q_High, Q_Complex
#     Q_Simple = {"Entry": Q(qualityBasic), "Intermediate": Q(0.75*qualityBasic), "High": Q(0.5*qualityBasic), "Expert": Q(0.25*qualityBasic)}
#     Q_Medium = {"Entry": Q(qualityStandard), "Intermediate": Q(qualityStandard), "High": Q(qualityBasic), "Expert": Q(0.5*qualityBasic)}
#     Q_High = {"Entry": Q(qualityHigh), "Intermediate": Q(qualityHigh), "High": Q(qualityStandard), "Expert": Q(qualityBasic)}
#     Q_Complex = {"Entry": Q(qualityPremium), "Intermediate": Q(qualityPremium), "High": Q(qualityHigh), "Expert": Q(qualityStandard)}