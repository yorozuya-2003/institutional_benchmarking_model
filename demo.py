# MODULE STUFF
from qualityModule import *
from managementModule import *
from riskModule import *

# UI STUFF
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore

# for dependent comboboxes
from PyQt5.QtGui import QStandardItemModel, QStandardItem

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons



# ABILITY JOB-TYPE SCALING SCREEN
abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert = map(float, [1, 1, 1, 1])
jobSimple, jobMedium, jobHigh, jobComplex = map(float, [1, 1, 1, 1])

class ability_jobType_scaling_window(QMainWindow):
    def __init__(self):
        super(ability_jobType_scaling_window, self).__init__()
        uic.loadUi('ui_files/ability-jobType_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        global abilityEntry, abilityIntermediate, abilityHigh, abilityExpert
        abilityIntermediate = float(self.abilityIntermediate.text())
        abilityHigh = float(self.abilityHigh.text())
        abilityExpert = float(self.abilityExpert.text())

        global jobSimple, jobMedium, jobHigh, jobComplex
        jobMedium = float(self.jobMedium.text())
        jobHigh = float(self.jobHigh.text())
        jobComplex = float(self.jobComplex.text())

        print(abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert)
        print(jobSimple, jobMedium, jobHigh, jobComplex)

        next_window = ability_jobType_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# ABILITY JOB TYPE SCREEN
class ability_jobType_window(QMainWindow):
    def __init__(self):
        super(ability_jobType_window, self).__init__()
        uic.loadUi('ui_files/ability_jobType_screen.ui', self)
        self.show()

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        global s1, s2, s3, s4
        s1 = self.s1.text()
        s2 = self.s2.text()
        s3 = self.s3.text()
        s4 = self.s4.text()

        global m1, m2, m3, m4
        m1 = self.m1.text()
        m2 = self.m2.text()
        m3 = self.m3.text()
        m4 = self.m4.text()

        global h1, h2, h3, h4
        h1 = self.h1.text()
        h2 = self.h2.text()
        h3 = self.h3.text()
        h4 = self.h4.text()

        global c1, c2, c3, c4
        c1 = self.c1.text()
        c2 = self.c2.text()
        c3 = self.c3.text()
        c4 = self.c4.text()
        next_window = quality_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4 = map(int, [s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4])



# QUALITY SCREEN
class quality_window(QMainWindow):
    def __init__(self):
        super(quality_window, self).__init__()
        uic.loadUi('ui_files/quality_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        A = self.paramA.text()
        B = self.paramB.text()
        C = self.paramC.text()
        D = self.paramD.text()
        QA_parameterArray.append(float(A))
        QA_parameterArray.append(float(B))
        QA_parameterArray.append(float(C))
        QA_parameterArray.append(float(D))
        
        print(QA_parameterArray)

        next_window = quality_scaling_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# QUALITY SCALING SCREEN
class quality_scaling_window(QMainWindow):
    def __init__(self):
        super(quality_scaling_window, self).__init__()
        uic.loadUi('ui_files/quality_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        qualityScalingFactorsArray = []
        qualityBasic = 1.0
        qualityStandard = self.qualityStandard.text()
        qualityHigh = self.qualityHigh.text()
        qualityPremium = self.qualityPremium.text()
        
        qualityBasic, qualityStandard, qualityHigh, qualityPremium = map(float, [qualityBasic, qualityStandard, qualityHigh, qualityPremium])

        qualityScalingFactorsArray.append(qualityBasic)
        qualityScalingFactorsArray.append(qualityStandard)
        qualityScalingFactorsArray.append(qualityHigh)
        qualityScalingFactorsArray.append(qualityPremium)
        
        print(qualityScalingFactorsArray)

        qualityFactorsInput(qualityScalingFactorsArray)
        
        # Quality Factors Mapping
        global QA_Simple, QA_Medium, QA_High, QA_Complex
        QA_Simple = {"Entry": QA(qualityBasic, s1), "Intermediate": QA(0.75*qualityBasic, s2), "High": QA(0.5*qualityBasic, s3), "Expert": QA(0.25*qualityBasic, s4)}
        QA_Medium = {"Entry": QA(qualityStandard, m1), "Intermediate": QA(qualityStandard, m2), "High": QA(qualityBasic, m3), "Expert": QA(0.5*qualityBasic, m4)}
        QA_High = {"Entry": QA(qualityHigh, h1), "Intermediate": QA(qualityHigh, h2), "High": QA(qualityStandard, h3), "Expert": QA(qualityBasic, h4)}
        QA_Complex = {"Entry": QA(qualityPremium, c1), "Intermediate": QA(qualityPremium, c2), "High": QA(qualityHigh, c3), "Expert": QA(qualityStandard, c4)}

        # Quality Output Dictionary
        global Quality_Dict
        Quality_Dict = {'Simple': QA_Simple, 'Medium': QA_Medium, 'High': QA_High, 'Complex': QA_Complex}

        # next_window = quality_output_window()
        next_window = management_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)               



# QUALITY OUTPUT
class quality_output_window(QMainWindow):
    def __init__(self):
        super(quality_output_window, self).__init__()
        uic.loadUi('ui_files/quality_output_screen.ui', self)

        self.pushButton.clicked.connect(self.generateOutput)
        self.nextButton.clicked.connect(self.nextScreen)

    def generateOutput(self):
        self.qualityOutputLabel.setText("Simple: " + str(QA_Simple) + "\n" + "Medium: " + str(QA_Medium) + "\n" + "High: " + str(QA_High) + "\n" + "Complex" + str(QA_Complex))

    def nextScreen(self):
        next_window = management_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# MANAGEMENT SCREEN
class management_window(QMainWindow):
    def __init__(self):
        super(management_window, self).__init__()
        uic.loadUi('ui_files/management_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        E = self.paramE.text()
        F = self.paramF.text()
        G = self.paramG.text()
        H = self.paramH.text()
        I = self.paramI.text()

        M_parameterArray.append(float(E))
        M_parameterArray.append(float(F))
        M_parameterArray.append(float(G))
        M_parameterArray.append(float(H))
        M_parameterArray.append(float(I))

        print(M_parameterArray)

        next_window = management_scaling_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)    



# MANAGEMENT SCALING SCREEN
class management_scaling_window(QMainWindow):
    def __init__(self):
        super(management_scaling_window, self).__init__()
        uic.loadUi('ui_files/management_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        managementScalingFactorsArray = []
        managementLow = 1.0
        managementMedium = self.managementMedium.text()
        managementHigh = self.managementHigh.text()

        managementLow, managementMedium, managementHigh = map(float, [managementLow, managementMedium, managementHigh])

        managementScalingFactorsArray.append(managementLow)
        managementScalingFactorsArray.append(managementMedium)
        managementScalingFactorsArray.append(managementHigh)

        print(managementScalingFactorsArray)

        managementFactorsInput(managementScalingFactorsArray)
        
        # Management Factors Mapping
        global M_Simple, M_Medium, M_High, M_Complex
        M_Simple = {"Entry": M(managementLow, s1), "Intermediate": M(managementLow, s2)}
        M_Medium = {"Entry": M(managementMedium, m1), "Intermediate": M(managementMedium, m2), "High": M(managementLow, m3), "Expert": M(managementLow, m4)}
        M_High = {"Entry": M(managementHigh, h1), "Intermediate": M(managementHigh, h2), "High": M(managementMedium, h3), "Expert": M(managementLow, h4)}
        M_Complex = {"High": M(managementHigh, c3), "Expert": M(managementHigh, c4)}

        # Management Output Dictionary
        global Management_Dict
        Management_Dict = {'Simple': M_Simple, 'Medium': M_Medium, 'High': M_High, 'Complex': M_Complex}

        # next_window = management_output_window()
        next_window = risk_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# MANAGEMENT OUTPUT
class management_output_window(QMainWindow):
    def __init__(self):
        super(management_output_window, self).__init__()
        uic.loadUi('ui_files/management_output_screen.ui', self)

        self.pushButton.clicked.connect(self.generateOutput)
        self.nextButton.clicked.connect(self.nextScreen)

    def generateOutput(self):
        self.managementOutputLabel.setText("Simple: " + str(M_Simple) + "\n" + "Medium: " + str(M_Medium) + "\n" + "High: " + str(M_High) + "\n" + "Complex: " + str(M_Complex))

    def nextScreen(self):
        next_window = risk_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# RISK SCREEN
class risk_window(QMainWindow):
    def __init__(self):
        super(risk_window, self).__init__()
        uic.loadUi('ui_files/risk_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        J = self.paramJ.text()
        K = self.paramK.text()
        L = self.paramL.text()

        R_parameterArray.append(float(J))
        R_parameterArray.append(float(K))
        R_parameterArray.append(float(L))

        print(R_parameterArray)

        next_window = risk_scaling_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# RISK SCALING SCREEN
class risk_scaling_window(QMainWindow):
    def __init__(self):
        super(risk_scaling_window, self).__init__()
        uic.loadUi('ui_files/risk_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)

    def nextScreen(self):
        riskScalingFactorsArray = []
        riskLow = 1.0
        riskMedium = self.riskMedium.text()
        riskHigh = self.riskHigh.text()
        riskComplex = self.riskComplex.text()

        riskLow, riskMedium, riskHigh, riskComplex = map(float, [riskLow, riskMedium, riskHigh, riskComplex])

        riskScalingFactorsArray.append(riskLow)
        riskScalingFactorsArray.append(riskMedium)
        riskScalingFactorsArray.append(riskHigh)
        riskScalingFactorsArray.append(riskComplex)

        print(riskScalingFactorsArray)

        riskFactorsInput(riskScalingFactorsArray)
        
        # Risk Factors Mapping
        global R_Low, R_Medium, R_High, R_Undefined
        R_Low = {"Simple": R(riskLow)}
        R_Medium = {"Simple": R(riskLow), "Medium": R(riskLow), "High": R(riskMedium)}
        R_High = {"Simple": R(riskMedium), "Medium": R(riskMedium), "High": R(riskHigh), "NA": R(riskComplex)}
        R_Undefined = {"NA": R(riskComplex)}

        # Risk Output Dictionary
        global Risk_Dict
        Risk_Dict = {'Low': R_Low, 'Medium': R_Medium, 'High': R_High, 'Undefined': R_Undefined}

        # next_window = risk_output_window()
        next_window = output_drop_down_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



# RISK OUTPUT
class risk_output_window(QMainWindow):
    def __init__(self):
        super(risk_output_window, self).__init__()
        uic.loadUi('ui_files/risk_output_screen.ui', self)

        self.pushButton.clicked.connect(self.generateOutput)
        self.nextButton.clicked.connect(self.nextScreen)

    def generateOutput(self):
        self.riskOutputLabel.setText("Low: " + str(R_Low) + "\n" + "Medium: " + str(R_Medium) + "\n" + "High: " + str(R_High) + "\n" + "Undefined: " + str(R_Undefined))

    def nextScreen(self):
        next_window = output_drop_down_window()
        widget.addWidget(next_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

# OUTPUT SCREEN
class output_drop_down_window(QMainWindow):
    def __init__(self):
        super(output_drop_down_window, self).__init__()
        uic.loadUi('ui_files/output_drop_down_screen.ui', self)
        self.setGeometry(200, 100, 810, 450)
        self.show()

        self.model = QStandardItemModel(self)

        self.factors.setModel(self.model)
        self.parameters1.setModel(self.model)
        self.parameters2.setModel(self.model)

        for factor_key in dictionary.keys():
            FACTOR = QStandardItem(factor_key)
            self.model.appendRow(FACTOR)
            factor_key_dict = dictionary.get(factor_key)

            for param1_key in factor_key_dict.keys():
                PARAM1 = QStandardItem(param1_key)
                FACTOR.appendRow(PARAM1)
                
                param1_array = factor_key_dict.get(param1_key)
                
                for value in param1_array:
                    PARAM2 = QStandardItem(value)
                    PARAM1.appendRow(PARAM2)

        self.factors.currentIndexChanged.connect(self.updateParam1Combo)
        self.updateParam1Combo(0)
        self.factors.activated.connect(self.labelUpdate)

        # initial default values for labels
        self.paramLabel1.setText('Job Type')
        self.paramLabel2.setText('Ability')

        self.generateButton.clicked.connect(self.generateOutput)

    def labelUpdate(self):
        if self.factors.currentText() == "Quality" or self.factors.currentText() == "Management":
            self.paramLabel1.setText('Job Type')
            self.paramLabel2.setText('Ability')
        elif self.factors.currentText() == "Risk":
            self.paramLabel1.setText('Risk Impact')
            self.paramLabel2.setText('Mitigation Options')

    def updateParam1Combo(self, index):
        model_index = self.model.index(index, 0, self.factors.rootModelIndex())
        self.parameters1.setRootModelIndex(model_index)
        self.parameters1.setCurrentIndex(0)
        self.parameters1.currentIndexChanged.connect(self.updateParam2Combo)
        self.updateParam2Combo(0)

    def updateParam2Combo(self, index):
        model_index = self.model.index(index, 0, self.parameters1.rootModelIndex())
        self.parameters2.setRootModelIndex(model_index)
        self.parameters2.setCurrentIndex(0)

    def generateOutput(self):
        # output_text = self.factors.currentText() + " " + self.parameters1.currentText() + " " + self.parameters2.currentText()
        # self.outputDataLabel.setText(output_text)
        
        # OUTPUT DICTIONARY
        output_dictionary = {'Quality': Quality_Dict, 'Management': Management_Dict, 'Risk': Risk_Dict}
        output_text = output_dictionary[self.factors.currentText()][self.parameters1.currentText()][self.parameters2.currentText()]
        self.outputDataLabel.setText(str(output_text)) 

    

# FACTORS & PARAMETERS DICTIONARY
dictionary = {
    'Quality':
        {'Simple': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['Entry', 'Intermediate', 'High', 'Expert']
    },

    'Management':{
        'Simple': ['Entry', 'Intermediate'],
        'Medium': ['Entry', 'Intermediate', 'High', 'Expert'],
        'High': ['Entry', 'Intermediate', 'High', 'Expert'],
        'Complex': ['High', 'Expert']
    },

    'Risk':{
        'Low': ['Simple'],
        'Medium': ['Simple', 'Medium', 'High'],
        'High': ['Simple', 'Medium', 'High', 'NA'],
        'Undefined': ['NA']
    }
}

demoApp = QApplication([])

widget = QtWidgets.QStackedWidget()
first_window = ability_jobType_scaling_window()

# CHECK
# first_window = output_drop_down_window()

widget.addWidget(first_window)
# widget.setFixedHeight(700)
# widget.setFixedWidth(750)
widget.showMaximized()

demoApp.exec_()
