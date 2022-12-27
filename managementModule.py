# assuming that the user inputs only 5 factors
M_parameterScalingArray = [0.15, 0.15, 0.3, 0.25, 0.15]

def M(management, persons, M_parameterArray):
    parameter_X_weight = 0
    for i in range(len(M_parameterArray)):
        parameter_X_weight += M_parameterArray[i] * M_parameterScalingArray[i]
    return parameter_X_weight * management * persons

M_low = 1
Mfunc = lambda value: float(value) * M_low
def managementFactorsInput(managementScalingFactorsArray):
    global managementLow, managementMedium, managementHigh
    managementLow, managementMedium, managementHigh = map(Mfunc, managementScalingFactorsArray)

M_Simple = {}
M_Medium = {}
M_High = {}
M_Complex = {}

# def managementMapping():
#     global M_Simple, M_Medium, M_High, M_Complex
#     M_Simple = {"Entry": M(managementLow), "Intermediate": M(managementLow)}
#     M_Medium = {"Entry": M(managementMedium), "Intermediate": M(managementMedium), "High": M(managementLow), "Expert": M(managementLow)}
#     M_High = {"Entry": M(managementHigh), "Intermediate": M(managementHigh), "High": M(managementMedium), "Expert": M(managementLow)}
#     M_Complex = {"High": M(managementHigh), "Expert": M(managementHigh)}
 