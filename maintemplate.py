# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newui2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNome = QtWidgets.QLabel(self.groupBox_2)
        self.labelNome.setObjectName("labelNome")
        self.verticalLayout.addWidget(self.labelNome)
        self.diretorio = QtWidgets.QLineEdit(self.groupBox_2)
        self.diretorio.setText("")
        self.diretorio.setObjectName("diretorio")
        self.verticalLayout.addWidget(self.diretorio)
        self.carregar = QtWidgets.QPushButton(self.groupBox_2)
        self.carregar.setObjectName("carregar")
        self.verticalLayout.addWidget(self.carregar)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelAltura = QtWidgets.QLabel(self.groupBox_2)
        self.labelAltura.setObjectName("labelAltura")
        self.horizontalLayout.addWidget(self.labelAltura)
        self.alturavideo = QtWidgets.QLineEdit(self.groupBox_2)
        self.alturavideo.setText("")
        self.alturavideo.setObjectName("alturavideo")
        self.horizontalLayout.addWidget(self.alturavideo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLimiarcor = QtWidgets.QLabel(self.groupBox_2)
        self.labelLimiarcor.setObjectName("labelLimiarcor")
        self.horizontalLayout_2.addWidget(self.labelLimiarcor)
        self.limiarcor = QtWidgets.QLineEdit(self.groupBox_2)
        self.limiarcor.setText("")
        self.limiarcor.setObjectName("limiarcor")
        self.horizontalLayout_2.addWidget(self.limiarcor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelLimiarmascara = QtWidgets.QLabel(self.groupBox_2)
        self.labelLimiarmascara.setObjectName("labelLimiarmascara")
        self.horizontalLayout_3.addWidget(self.labelLimiarmascara)
        self.Limiarmascara = QtWidgets.QLineEdit(self.groupBox_2)
        self.Limiarmascara.setText("")
        self.Limiarmascara.setObjectName("Limiarmascara")
        self.horizontalLayout_3.addWidget(self.Limiarmascara)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.selecionarAelha = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selecionarAelha.sizePolicy().hasHeightForWidth())
        self.selecionarAelha.setSizePolicy(sizePolicy)
        self.selecionarAelha.setObjectName("selecionarAelha")
        self.verticalLayout_3.addWidget(self.selecionarAelha)
        self.iniciar = QtWidgets.QPushButton(self.groupBox_2)
        self.iniciar.setObjectName("iniciar")
        self.verticalLayout_3.addWidget(self.iniciar)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labeltempcaminhamento = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempcaminhamento.setObjectName("labeltempcaminhamento")
        self.gridLayout_4.addWidget(self.labeltempcaminhamento, 2, 0, 1, 1)
        self.tempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        self.tempoestacionario.setObjectName("tempoestacionario")
        self.gridLayout_4.addWidget(self.tempoestacionario, 8, 1, 1, 1)
        self.labeltempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempodescanco.setObjectName("labeltempodescanco")
        self.gridLayout_4.addWidget(self.labeltempodescanco, 7, 0, 1, 1)
        self.labeldistanciapercorrida = QtWidgets.QLabel(self.groupBox_2)
        self.labeldistanciapercorrida.setObjectName("labeldistanciapercorrida")
        self.gridLayout_4.addWidget(self.labeldistanciapercorrida, 0, 0, 1, 1)
        self.labeltempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempoestacionario.setObjectName("labeltempoestacionario")
        self.gridLayout_4.addWidget(self.labeltempoestacionario, 8, 0, 1, 1)
        self.tempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.tempodescanco.setObjectName("tempodescanco")
        self.gridLayout_4.addWidget(self.tempodescanco, 7, 1, 1, 1)
        self.distaciaPercrrida = QtWidgets.QLabel(self.groupBox_2)
        self.distaciaPercrrida.setObjectName("distaciaPercrrida")
        self.gridLayout_4.addWidget(self.distaciaPercrrida, 0, 1, 1, 1)
        self.velocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.velocidademedia.setObjectName("velocidademedia")
        self.gridLayout_4.addWidget(self.velocidademedia, 5, 1, 1, 1)
        self.tempocaminhamento = QtWidgets.QLabel(self.groupBox_2)
        self.tempocaminhamento.setObjectName("tempocaminhamento")
        self.gridLayout_4.addWidget(self.tempocaminhamento, 2, 1, 1, 1)
        self.labelvelocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.labelvelocidademedia.setObjectName("labelvelocidademedia")
        self.gridLayout_4.addWidget(self.labelvelocidademedia, 5, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 132, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1185, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Configurações"))
        self.labelNome.setText(_translate("MainWindow", "Nome ou diretório do video:"))
        self.carregar.setText(_translate("MainWindow", "Carregar"))
        self.labelAltura.setText(_translate("MainWindow", "Altura do video"))
        self.labelLimiarcor.setText(_translate("MainWindow", "Limiar de cor"))
        self.labelLimiarmascara.setText(_translate("MainWindow", "Limiar de mascarade ruidos"))
        self.selecionarAelha.setText(_translate("MainWindow", "Selecionar abelha"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.labeltempcaminhamento.setText(_translate("MainWindow", "Tempo de caminhamento"))
        self.tempoestacionario.setText(_translate("MainWindow", "0.0"))
        self.labeltempodescanco.setText(_translate("MainWindow", "Tempo de descanço"))
        self.labeldistanciapercorrida.setText(_translate("MainWindow", "]Distancia Percorrida"))
        self.labeltempoestacionario.setText(_translate("MainWindow", "Tempo estacionário"))
        self.tempodescanco.setText(_translate("MainWindow", "0.0"))
        self.distaciaPercrrida.setText(_translate("MainWindow", "0.0"))
        self.velocidademedia.setText(_translate("MainWindow", "0.0"))
        self.tempocaminhamento.setText(_translate("MainWindow", "0.0"))
        self.labelvelocidademedia.setText(_translate("MainWindow", "Velocidade média"))
        self.pushButton.setText(_translate("MainWindow", "Parar"))


