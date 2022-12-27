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

# counter for keeping in check the back and previous screen windows
counter = 0



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
        abilityEntry = float(self.abilityEntry.text())
        abilityIntermediate = float(self.abilityIntermediate.text())
        abilityHigh = float(self.abilityHigh.text())
        abilityExpert = float(self.abilityExpert.text())

        abilityEntry, abilityIntermediate, abilityHigh, abilityExpert = map(lambda x : x/abilityEntry, [abilityEntry, abilityIntermediate, abilityHigh, abilityExpert])

        global jobSimple, jobMedium, jobHigh, jobComplex
        jobSimple = float(self.jobSimple.text())
        jobMedium = float(self.jobMedium.text())
        jobHigh = float(self.jobHigh.text())
        jobComplex = float(self.jobComplex.text())

        jobSimple, jobMedium, jobHigh, jobComplex = map(lambda x : x/jobSimple, [jobSimple, jobMedium, jobHigh, jobComplex])

        print('Ability scaling:', abilityEntry, abiltyIntermediate, abilityHigh, abilityExpert)
        print('JobType scaling:', jobSimple, jobMedium, jobHigh, jobComplex)

        global counter
        if counter == 0:
            counter += 1
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
        self.backButton.clicked.connect(self.backScreen)

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

        s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4 = map(int, [s1, s2, s3, s4, m1, m2, m3, m4, h1, h2, h3, h4, c1, c2, c3, c4])

        global counter
        if counter == 1:
            counter += 1
            next_window = quality_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# QUALITY SCREEN
class quality_window(QMainWindow):
    def __init__(self):
        super(quality_window, self).__init__()
        uic.loadUi('ui_files/quality_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        A = self.paramA.text()
        B = self.paramB.text()
        C = self.paramC.text()
        D = self.paramD.text()
        A, B, C, D = map(float, [A, B, C, D])

        global Q_parameterArray
        Q_parameterArray = [A, B, C, D]

        print('Q_parameterArray:', Q_parameterArray)

        global counter
        if counter == 2:
            counter += 1
            next_window = quality_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# QUALITY SCALING SCREEN
class quality_scaling_window(QMainWindow):
    def __init__(self):
        super(quality_scaling_window, self).__init__()
        uic.loadUi('ui_files/quality_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        qualityBasic = self.qualityBasic.text()
        qualityStandard = self.qualityStandard.text()
        qualityHigh = self.qualityHigh.text()
        qualityPremium = self.qualityPremium.text()
        
        qualityBasic, qualityStandard, qualityHigh, qualityPremium = map(float, [qualityBasic, qualityStandard, qualityHigh, qualityPremium])
        qualityBasic, qualityStandard, qualityHigh, qualityPremium = map(lambda x : x/qualityBasic, [qualityBasic, qualityStandard, qualityHigh, qualityPremium])

        qualityScalingFactorsArray = [qualityBasic, qualityStandard, qualityHigh, qualityPremium]
        
        print('qualityScalingFactorsArray:', qualityScalingFactorsArray)

        qualityFactorsInput(qualityScalingFactorsArray)
        
        # Quality Factors Mapping
        global Q_Simple, Q_Medium, Q_High, Q_Complex
        Q_Simple = {"Entry": Q(qualityBasic, s1, Q_parameterArray), "Intermediate": Q(0.75*qualityBasic, s2, Q_parameterArray), "High": Q(0.5*qualityBasic, s3, Q_parameterArray), "Expert": Q(0.25*qualityBasic, s4, Q_parameterArray)}
        Q_Medium = {"Entry": Q(qualityStandard, m1, Q_parameterArray), "Intermediate": Q(qualityStandard, m2, Q_parameterArray), "High": Q(qualityBasic, m3, Q_parameterArray), "Expert": Q(0.5*qualityBasic, m4, Q_parameterArray)}
        Q_High = {"Entry": Q(qualityHigh, h1, Q_parameterArray), "Intermediate": Q(qualityHigh, h2, Q_parameterArray), "High": Q(qualityStandard, h3, Q_parameterArray), "Expert": Q(qualityBasic, h4, Q_parameterArray)}
        Q_Complex = {"Entry": Q(qualityPremium, c1, Q_parameterArray), "Intermediate": Q(qualityPremium, c2, Q_parameterArray), "High": Q(qualityHigh, c3, Q_parameterArray), "Expert": Q(qualityStandard, c4, Q_parameterArray)}
        # Quality Output Dictionary
        global Quality_Dict
        Quality_Dict = {'Simple': Q_Simple, 'Medium': Q_Medium, 'High': Q_High, 'Complex': Q_Complex}

        global counter
        if counter == 3:
            counter += 1
            next_window = management_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# MANAGEMENT SCREEN
class management_window(QMainWindow):
    def __init__(self):
        super(management_window, self).__init__()
        uic.loadUi('ui_files/management_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        E = self.paramE.text()
        F = self.paramF.text()
        G = self.paramG.text()
        H = self.paramH.text()
        I = self.paramI.text()
        E, F, G, H, I = map(float, [E, F, G, H, I])

        global M_parameterArray
        M_parameterArray = [E, F, G, H, I]

        print('M_parameterArray:', M_parameterArray)

        global counter
        if counter == 4:
            counter += 1
            next_window = management_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# MANAGEMENT SCALING SCREEN
class management_scaling_window(QMainWindow):
    def __init__(self):
        super(management_scaling_window, self).__init__()
        uic.loadUi('ui_files/management_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        managementLow = self.managementLow.text()
        managementMedium = self.managementMedium.text()
        managementHigh = self.managementHigh.text()

        managementLow, managementMedium, managementHigh = map(float, [managementLow, managementMedium, managementHigh])
        managementLow, managementMedium, managementHigh = map(lambda x : x/managementLow, [managementLow, managementMedium, managementHigh])

        managementScalingFactorsArray = [managementLow, managementMedium, managementHigh]

        print('managementScalingFactorsArray:', managementScalingFactorsArray)

        managementFactorsInput(managementScalingFactorsArray)
        
        # Management Factors Mapping
        global M_Simple, M_Medium, M_High, M_Complex
        M_Simple = {"Entry": M(managementLow, s1, M_parameterArray), "Intermediate": M(managementLow, s2, M_parameterArray)}
        M_Medium = {"Entry": M(managementMedium, m1, M_parameterArray), "Intermediate": M(managementMedium, m2, M_parameterArray), "High": M(managementLow, m3, M_parameterArray), "Expert": M(managementLow, m4, M_parameterArray)}
        M_High = {"Entry": M(managementHigh, h1, M_parameterArray), "Intermediate": M(managementHigh, h2, M_parameterArray), "High": M(managementMedium, h3, M_parameterArray), "Expert": M(managementLow, h4, M_parameterArray)}
        M_Complex = {"High": M(managementHigh, c3, M_parameterArray), "Expert": M(managementHigh, c4, M_parameterArray)}

        # Management Output Dictionary
        global Management_Dict
        Management_Dict = {'Simple': M_Simple, 'Medium': M_Medium, 'High': M_High, 'Complex': M_Complex}

        global counter
        if counter == 5:
            counter += 1
            next_window = risk_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# RISK SCREEN
class risk_window(QMainWindow):
    def __init__(self):
        super(risk_window, self).__init__()
        uic.loadUi('ui_files/risk_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        J = self.paramJ.text()
        K = self.paramK.text()
        L = self.paramL.text()
        J, K, L = map(float, [J, K, L])

        global R_parameterArray
        R_parameterArray = [J, K, L]

        print('R_parameterArray:', R_parameterArray)

        global counter
        if counter == 6:
            counter += 1
            next_window = risk_scaling_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



# RISK SCALING SCREEN
class risk_scaling_window(QMainWindow):
    def __init__(self):
        super(risk_scaling_window, self).__init__()
        uic.loadUi('ui_files/risk_scaling_screen.ui', self)

        self.nextButton.clicked.connect(self.nextScreen)
        self.backButton.clicked.connect(self.backScreen)

    def nextScreen(self):
        riskLow = self.riskLow.text()
        riskMedium = self.riskMedium.text()
        riskHigh = self.riskHigh.text()
        riskComplex = self.riskComplex.text()

        riskLow, riskMedium, riskHigh, riskComplex = map(float, [riskLow, riskMedium, riskHigh, riskComplex])
        riskLow, riskMedium, riskHigh, riskComplex = map(lambda x : x/riskLow, [riskLow, riskMedium, riskHigh, riskComplex])

        riskScalingFactorsArray = [riskLow, riskMedium, riskHigh, riskComplex]

        print('riskScalingFactorsArray:', riskScalingFactorsArray)

        riskFactorsInput(riskScalingFactorsArray)
        
        # Risk Factors Mapping
        global R_Low, R_Medium, R_High, R_Undefined
        R_Low = {"Simple": R(riskLow, R_parameterArray)}
        R_Medium = {"Simple": R(riskLow, R_parameterArray), "Medium": R(riskLow, R_parameterArray), "High": R(riskMedium, R_parameterArray)}
        R_High = {"Simple": R(riskMedium, R_parameterArray), "Medium": R(riskMedium, R_parameterArray), "High": R(riskHigh, R_parameterArray), "NA": R(riskComplex, R_parameterArray)}
        R_Undefined = {"NA": R(riskComplex, R_parameterArray)}

        # Risk Output Dictionary
        global Risk_Dict
        Risk_Dict = {'Low': R_Low, 'Medium': R_Medium, 'High': R_High, 'Undefined': R_Undefined}

        global counter
        if counter == 7:
            counter += 1
            next_window = output_drop_down_window()
            widget.addWidget(next_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)



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

        self.backButton.clicked.connect(self.backScreen)

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
        self.outputDataLabel.setText(f'{output_text:.2f}' + " " + str(self.factors.currentText()) + " units") 
        
    def backScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    

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
