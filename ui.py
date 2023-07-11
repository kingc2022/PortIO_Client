# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainQAlMAn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qfluentwidgets import PlainTextEdit
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import HyperlinkButton
from qfluentwidgets import PushButton
from qfluentwidgets import ComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(600, 400)
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 581, 371))
        self.tabWidget.setFont(font)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setEnabled(True)
        self.nol2 = QLabel(self.login)
        self.nol2.setObjectName(u"nol2")
        self.nol2.setGeometry(QRect(190, 40, 161, 31))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.nol2.setFont(font1)
        self.nol2.setStyleSheet(u"")
        self.nol2.setAlignment(Qt.AlignCenter)
        self.api_token = PlainTextEdit(self.login)
        self.api_token.setObjectName(u"api_token")
        self.api_token.setGeometry(QRect(120, 90, 321, 111))
        self.login_btn = PrimaryPushButton(self.login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(120, 220, 321, 31))
        self.get_token = HyperlinkButton(self.login)
        self.get_token.setObjectName(u"get_token")
        self.get_token.setGeometry(QRect(190, 270, 171, 31))
        self.tabWidget.addTab(self.login, "")
        self.download_frpc_page = QWidget()
        self.download_frpc_page.setObjectName(u"download_frpc_page")
        self.download = PrimaryPushButton(self.download_frpc_page)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(210, 60, 141, 31))
        self.label_2 = QLabel(self.download_frpc_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 501, 101))
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.download_frpc_page, "")
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.nol4 = QLabel(self.user_page)
        self.nol4.setObjectName(u"nol4")
        self.nol4.setGeometry(QRect(120, 60, 81, 201))
        font3 = QFont()
        font3.setFamily(u"\u5b8b\u4f53")
        font3.setPointSize(12)
        self.nol4.setFont(font3)
        self.nol4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.user_info = QLabel(self.user_page)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setGeometry(QRect(230, 60, 321, 201))
        self.user_info.setFont(font3)
        self.user_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tabWidget.addTab(self.user_page, "")
        self.start_tunnel_page = QWidget()
        self.start_tunnel_page.setObjectName(u"start_tunnel_page")
        self.nol3 = QLabel(self.start_tunnel_page)
        self.nol3.setObjectName(u"nol3")
        self.nol3.setGeometry(QRect(20, 20, 71, 51))
        font4 = QFont()
        font4.setFamily(u"\u5b8b\u4f53")
        font4.setPointSize(10)
        self.nol3.setFont(font4)
        self.nol3.setAlignment(Qt.AlignCenter)
        self.select_tunnel = ComboBox(self.start_tunnel_page)
        self.select_tunnel.setObjectName(u"select_tunnel")
        self.select_tunnel.setGeometry(QRect(100, 30, 171, 31))
        self.refresh_tunnels = PushButton(self.start_tunnel_page)
        self.refresh_tunnels.setObjectName(u"refresh_tunnels")
        self.refresh_tunnels.setGeometry(QRect(100, 70, 171, 31))
        self.label = QLabel(self.start_tunnel_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 20, 251, 301))
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.start_tunnel = PrimaryPushButton(self.start_tunnel_page)
        self.start_tunnel.setObjectName(u"start_tunnel")
        self.start_tunnel.setGeometry(QRect(20, 120, 251, 31))
        self.del_config = PushButton(self.start_tunnel_page)
        self.del_config.setObjectName(u"del_config")
        self.del_config.setGeometry(QRect(20, 160, 251, 31))
        self.tabWidget.addTab(self.start_tunnel_page, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.nol1 = QLabel(self.about)
        self.nol1.setObjectName(u"nol1")
        self.nol1.setGeometry(QRect(60, 70, 461, 61))
        font5 = QFont()
        font5.setFamily(u"Courier")
        font5.setPointSize(12)
        self.nol1.setFont(font5)
        self.nol1.setTextFormat(Qt.PlainText)
        self.nol1.setAlignment(Qt.AlignCenter)
        self.github_page = PushButton(self.about)
        self.github_page.setObjectName(u"github_page")
        self.github_page.setGeometry(QRect(180, 180, 171, 31))
        self.tabWidget.addTab(self.about, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PortIO \u5ba2\u6237\u7aef", None))
        self.nol2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u60a8\u7684\u8bbf\u95ee\u5bc6\u94a5", None))
        self.api_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8bbf\u95ee\u5bc6\u94a5", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.get_token.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u8bbf\u95ee\u5bc6\u94a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u82e5\u60a8\u7684 Frpc \u5ba2\u6237\u7aef\u88ab\u8bef\u5220\uff0c\u8bf7\u70b9\u51fb\u4e0b\u8f7d\u6309\u94ae\uff0c\u4e0b\u8f7d Zip \u6587\u4ef6\uff0c\u5e76\u89e3\u538b\n"
"\n"
"\u5c06\u89e3\u538b\u51fa\u7684\u6587\u4ef6\u5939\u4e2d\u7684 frpc.exe \u653e\u5165\u672c\u7a0b\u5e8f\u76ee\u5f55\u4e0b\uff0c\u5e76\u91cd\u542f\u672c\u7a0b\u5e8f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.download_frpc_page), QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d Frp \u5ba2\u6237\u7aef", None))
        self.nol4.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237 ID\n"
"\n"
"\u7528\u6237\u540d\n"
"\n"
"\u90ae\u7bb1\n"
"\n"
"\u6ce8\u518c\u65f6\u95f4\n"
"\n"
"\u5f53\u524d\u6d41\u91cf\n"
"", None))
        self.user_info.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237 ID\n"
"\n"
"\u7528\u6237\u540d\n"
"\n"
"\u90ae\u7bb1\n"
"\n"
"\u6ce8\u518c\u65f6\u95f4\n"
"\n"
"\u5f53\u524d\u6d41\u91cf\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_page), QCoreApplication.translate("MainWindow", u"\u7528\u6237\u4fe1\u606f", None))
        self.nol3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u96a7\u9053", None))
        self.refresh_tunnels.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u96a7\u9053\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"## \u542f\u52a8\u96a7\u9053 Tips\n"
"\n"
"\u70b9\u51fb\u542f\u52a8\u96a7\u9053\u540e\uff0c\u4f1a\u5f39\u51fa\u4e00\u4e2a\u7a97\u53e3\n"
"\n"
"\u82e5\u5728\u7a97\u53e3\u5185\u663e\u793a <code>start proxy succes</code>\n"
"\n"
"\u5373\u4e3a\u542f\u52a8\u6210\u529f\uff0c\u6b64\u65f6\u53ef\u4ee5\u5173\u95ed\u672c\u7a0b\u5e8f\n"
"\n"
"\u53cd\u4e4b\u8bf7\u68c0\u67e5\u4f60\u662f\u5426\u591a\u5f00\u7a7f\u900f\u5ba2\u6237\u7aef\n"
"\n"
"\u672c\u5730\u670d\u52a1\u662f\u5426\u5f00\u542f\n"
"\n"
"\u670d\u52a1\u5668\u662f\u5426\u5728\u7ebf", None))
        self.start_tunnel.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u96a7\u9053", None))
        self.del_config.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7406\u914d\u7f6e\u6587\u4ef6\u7f13\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.start_tunnel_page), QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u96a7\u9053", None))
        self.nol1.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 kingc, All rights reserved.", None))
        self.github_page.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00 GitHub \u4ed3\u5e93", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

