# assuming that the user inputs only 3 factors
R_parameterScalingArray = [0.33, 0.33, 0.34]

def R(risk, R_parameterArray):
    parameter_X_weight = 1
    for i in range(len(R_parameterArray)):
        parameter_X_weight *= R_parameterArray[i] * R_parameterScalingArray[i]
    return parameter_X_weight * 1000 * risk

R_low = 1
Rfunc = lambda value: float(value) * R_low
def riskFactorsInput(riskScalingFactorsArray):
    global riskLow, riskMedium, riskHigh, riskComplex
    riskLow, riskMedium, riskHigh, riskComplex = map(Rfunc, riskScalingFactorsArray)

R_Low = {}
R_Medium = {}
R_High = {}
R_Undefined = {}

# def riskMapping():
#     global R_Low, R_Medium, R_High, R_Undefined
#     R_Low = {"Simple": R(riskLow)}
#     R_Medium = {"Simple": R(riskLow), "Medium": R(riskLow), "High": R(riskMedium)}
#     R_High = {"Simple": R(riskMedium), "Medium": R(riskMedium), "High": R(riskHigh), "NA": R(riskComplex)}
#     R_Undefined = {"NA": R(riskComplex)}