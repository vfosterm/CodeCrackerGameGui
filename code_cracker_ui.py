# icon https://visualpharm.com/free-icons/matrix%20desktop-595b40b75ba036ed117d860b
# coding=utf8


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import random


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindowObject")
        self.resize(422, 442)
        self.center_on_screen()
        self.icon = os.path.join(os.getcwd(), 'code_cracker_icon.svg')
        self.setWindowIcon(QtGui.QIcon(self.icon))
        # Begin UI
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.guess_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guess_input.sizePolicy().hasHeightForWidth())
        self.guess_input.setSizePolicy(sizePolicy)
        self.guess_input.setMinimumSize(QtCore.QSize(80, 30))
        self.guess_input.setMaximumSize(QtCore.QSize(80, 30))
        self.guess_input.setBaseSize(QtCore.QSize(80, 20))
        self.guess_input.setAcceptDrops(False)
        self.guess_input.setToolTip("")
        self.guess_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.guess_input.setObjectName("guess_input")
        self.guess_input.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_input.setMaxLength(4)
        self.guess_input.setValidator(QtGui.QIntValidator())
        self.horizontalLayout_2.addWidget(self.guess_input)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_game_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_game_btn.setObjectName("new_game_btn")
        self.horizontalLayout.addWidget(self.new_game_btn)
        spacerItem3 = QtWidgets.QSpacerItem(30, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.guess_btn = QtWidgets.QPushButton(self.centralwidget)
        self.guess_btn.setObjectName("guess_btn")
        self.horizontalLayout.addWidget(self.guess_btn)
        self.guess_btn.setDefault(True)
        spacerItem4 = QtWidgets.QSpacerItem(30, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setObjectName("quit_btn")
        self.horizontalLayout.addWidget(self.quit_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.frame)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_10.setDigitCount(4)
        self.lcdNumber_10.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_10.display('----')
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_9.setDigitCount(4)
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.display('----')
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_8.setDigitCount(4)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.display('----')
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_7.setDigitCount(4)
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_7.display('----')
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_6.setDigitCount(4)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.display('----')
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_5.setDigitCount(4)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.display('----')
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_4.setDigitCount(4)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.display('----')
        self.lcdNumber_4.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_3.setDigitCount(4)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.display('----')
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setDigitCount(4)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.display('----')
        self.lcdNumber_2.setObjectName("lcdNumber_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.splitter_2)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.display('----')
        self.lcdNumber.setObjectName("lcdNumber")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_10 = QtWidgets.QLabel(self.splitter_3)
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setObjectName("label_9")
        self.label_9 = QtWidgets.QLabel(self.splitter_3)
        self.label_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_9.setObjectName("label_8")
        self.label_8 = QtWidgets.QLabel(self.splitter_3)
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.splitter_3)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.splitter_3)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.splitter_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.font = QtGui.QFont()
        self.font.setFamily("SF Mono")
        self.font.setPointSize(4)
        self.font.setStyleHint(QtGui.QFont.Monospace)
        self.title_label.setFont(self.font)
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setScaledContents(True)
        self.title_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.title_label.setObjectName("title_label")
        self.gridLayout_2.addWidget(self.title_label, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 2, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # end UI
        self.code_list = [self.lcdNumber, self.lcdNumber_2, self.lcdNumber_3, self.lcdNumber_4, self.lcdNumber_5, self.lcdNumber_6, self.lcdNumber_7, self.lcdNumber_8, self.lcdNumber_9, self.lcdNumber_10]
        self.guess_list = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8, self.label_9, self.label_10]

        self.code = gen_code()
        self.current_guess = ''
        self.game_turn = 0
        # print(self.code)
        self.quit_btn.clicked.connect(self.quit)
        self.guess_btn.clicked.connect(self.guess)
        self.guess_input.returnPressed.connect(self.guess_btn.click)
        self.new_game_btn.clicked.connect(self.new_game)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", " "))
        self.guess_input.setPlaceholderText(_translate("MainWindow", "InputCode"))
        self.new_game_btn.setText(_translate("MainWindow", "NewGame"))
        self.guess_btn.setText(_translate("MainWindow", "Crack"))
        self.quit_btn.setText(_translate("MainWindow", "Quit"))
        self.label_10.setText(_translate("MainWindow", "    "))
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_9.setText(_translate("MainWindow", "    "))
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_8.setText(_translate("MainWindow", "    "))
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_7.setText(_translate("MainWindow", "    "))
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_6.setText(_translate("MainWindow", "    "))
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_5.setText(_translate("MainWindow", "    "))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_4.setText(_translate("MainWindow", "    "))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_3.setText(_translate("MainWindow", "    "))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_2.setText(_translate("MainWindow", "    "))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setText(_translate("MainWindow", "    "))
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><pre align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"maincontent\"/> ██████╗ ██████╗ ██████╗ ███████╗         ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ </pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">██╔════╝██╔═══██╗██╔══██╗██╔════╝        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗</pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">██║     ██║   ██║██║  ██║█████╗          ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝</pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">██║     ██║   ██║██║  ██║██╔══╝          ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗</pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">╚██████╗╚██████╔╝██████╔╝███████╗███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║</pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝</pre><p align=\"center\"><br/></p></body></html>"))
        self.title_label.setTextFormat(QtCore.Qt.RichText)
    def center_on_screen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)), int((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def quit(self):
        sys.exit(app)

    # Game Logic here
    def guess(self):
        if len(self.guess_input.text()) == 4 and self.game_turn < 10:
            self.current_guess = self.guess_input.text()
            self.code_list[self.game_turn].display(self.current_guess)
            crack = check(self.code, self.current_guess)
            guess_out = guess_out_string(crack)
            self.guess_list[self.game_turn].setText(guess_out)
            self.game_turn += 1

            if crack == ['O', 'O', 'O', 'O']:
                self.win_game()

            if self.game_turn == 10:
                self.game_over()


        self.guess_input.clear()

    def new_game(self):
        self.label.setText('    ')
        self.label_2.setText('    ')
        self.label_3.setText('    ')
        self.label_4.setText('    ')
        self.label_5.setText('    ')
        self.label_6.setText('    ')
        self.label_7.setText('    ')
        self.label_8.setText('    ')
        self.label_9.setText('    ')
        self.label_10.setText('    ')
        self.lcdNumber.display('----')
        self.lcdNumber_2.display('----')
        self.lcdNumber_3.display('----')
        self.lcdNumber_4.display('----')
        self.lcdNumber_5.display('----')
        self.lcdNumber_6.display('----')
        self.lcdNumber_7.display('----')
        self.lcdNumber_8.display('----')
        self.lcdNumber_9.display('----')
        self.lcdNumber_10.display('----')
        self.game_turn = 0
        self.code = gen_code()
        self.show()
        #print(self.code)

    def win_game(self):
        self.hide()
        win = QtWidgets.QMessageBox()
        win.setWindowIcon(QtGui.QIcon(self.icon))
        win.setWindowTitle(" ")
        font = QtGui.QFont()
        font.setFamily("SF Mono")
        font.setStyleHint(QtGui.QFont.Monospace)
        win.setFont(font)
        win.setTextFormat(QtCore.Qt.RichText)
        win.setText("<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"maincontent\"/><span style=\" font-family:'SF Mono'; font-size:6pt;\"/><span style=\" font-family:'SF Mono'; font-size:6pt;\">██████╗ ██████╗ ██████╗ ███████╗         ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\">██╔════╝██╔═══██╗██╔══██╗██╔════╝        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\">██║     ██║   ██║██║  ██║█████╗          ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\">██║     ██║   ██║██║  ██║██╔══╝          ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\">╚██████╗╚██████╔╝██████╔╝███████╗███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\"> ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ </span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Mono'; font-size:6pt;\"/></pre><p><br/></p></body></html>")
        new_game_btn = win.addButton("New Game", QtWidgets.QMessageBox.YesRole)
        quit_game_btn = win.addButton("Quit Game", QtWidgets.QMessageBox.NoRole)

        win.exec_()

        if win.clickedButton() is new_game_btn:
            self.new_game()
            win.close()
            return
        elif win.clickedButton() is quit_game_btn:
            win.close()
            self.quit()
        else:
            win.close()
            self.quit()

    def game_over(self):
        self.hide()
        win = QtWidgets.QMessageBox()
        win.setWindowIcon(QtGui.QIcon(self.icon))
        win.setWindowTitle(" ")
        font = QtGui.QFont()
        font.setFamily("SF Mono")
        font.setStyleHint(QtGui.QFont.Monospace)
        win.setFont(font)
        win.setTextFormat(QtCore.Qt.RichText)
        win.setText("<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"maincontent\"/><span style=\" font-family:\'SF Mono\'; font-size:6pt;\"/><span style=\" font-family:\'SF Mono\'; font-size:6pt;\">██████╗  █████╗ ███╗   ███╗███████╗         ██████╗ ██╗   ██╗███████╗██████╗ </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\">██╔════╝ ██╔══██╗████╗ ████║██╔════╝        ██╔═══██╗██║   ██║██╔════╝██╔══██╗</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\">██║  ███╗███████║██╔████╔██║█████╗          ██║   ██║██║   ██║█████╗  ██████╔╝</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\">██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\">╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\"> ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝</span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF Mono\'; font-size:6pt;\"/></pre><p><br/></p></body></html>")
        new_game_btn = win.addButton("New Game", QtWidgets.QMessageBox.YesRole)
        quit_game_btn = win.addButton("Quit Game", QtWidgets.QMessageBox.NoRole)

        win.exec_()

        if win.clickedButton() is new_game_btn:
            self.new_game()
            win.close()
            return
        elif win.clickedButton() is quit_game_btn:
            win.close()
            self.quit()
        else:
            win.close()
            self.quit()


def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0, 9))

    return code


def check(code, guess):
    guess_out = ['-', '-', '-', '-']
    x_it = 0
    temp_code = []
    guess_in = []

    for char in guess:
        guess_in.append(int(char))
    for num in code:
        temp_code.append(num)

    for x in range(len(guess_in)):
        if guess_in[x] == temp_code[x]:
            guess_out[x_it] = 'O'
            x_it += 1
            temp_code[x] = 99
            guess_in[x] = 99

    for x in range(len(guess_in)):
        for y in range(len(code)):
            if guess_in[x] == temp_code[y] and x != y and guess_in[x] < 10:
                guess_out[x_it] = 'X'
                x_it += 1
                guess_in[x] = 99
                temp_code[y] = 99

    return guess_out


def guess_out_string(guess_out):
    guess_string = ''
    for char in guess_out:
        guess_string += char
    return guess_string


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
