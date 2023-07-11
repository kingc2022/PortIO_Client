import base64
import datetime
import os
import shutil
import sys
import time
import webbrowser
import zipfile
from datetime import datetime

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from qfluentwidgets import MessageBox

import config
from ui import Ui_MainWindow


class Ui(QMainWindow, Ui_MainWindow):
    def message_ok(self, title: str, content: str):
        self.m = MessageBox(title, content, parent=self)
        self.m.yesButton.setText("确定")
        self.m.cancelButton.hide()
        self.m.open()

    def message_ok_cancel(self, title: str, content: str):
        self.m = MessageBox(title, content, parent=self)
        self.m.yesButton.setText("确定")
        self.m.cancelButton.setText("取消")
        self.m.open()

    def message_cancel(self, title: str, content: str):
        self.m = MessageBox(title, content, parent=self)
        self.m.yesButton.hide()
        self.m.cancelButton.setText("取消")
        self.m.open()

    def message_confirm(self, title: str, content: str, yes=None, no=None, yes_text="确定", no_text="取消"):
        self.m = MessageBox(title, content, self)
        self.m.yesButton.setText(yes_text)
        self.m.cancelButton.setText(no_text)
        if yes is not None:
            self.m.yesButton.clicked.connect(yes)
        if no is not None:
            self.m.cancelButton.clicked.connect(no)
        self.m.open()

    def open_page(self, url: str):
        webbrowser.open(url)

    def write_token(self):
        self.tk = self.api_token.toPlainText()
        if " " in self.tk:
            self.message_ok("登录", "访问密钥中不得有空格")
            self.api_token.setPlainText("")
            return
        if "\n" in self.tk:
            self.message_ok("登录", "访问密钥中不得有换行")
            self.api_token.setPlainText("")
            return
        # 检验 Token 是否存在
        self.response = requests.get(f"{self.base_url}/user", headers={
            "Authorization": f"Bearer {self.tk}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        if self.response.status_code == 401:
            self.message_ok("登录", "访问密钥无效! 请重新生成")
            self.api_token.setPlainText("")
            return
        with open("token.txt", 'w', encoding='UTF-8') as f:
            f.write(base64.urlsafe_b64encode(self.tk.encode()).decode())
        self.message_ok("登录", "登录成功! 请重新启动软件")

    def download_frp(self):
        if os.path.exists("frpc.exe"):
            self.message_confirm("下载 Frp 客户端", "已经有 Frp 客户端了, 是否需要下载",
                                 yes=lambda: self.open_page("https://github.com/fatedier/frp/releases/download/v0.51"
                                                            ".0/frp_0.51.0_windows_amd64.zip"))
            return
        else:
            self.open_page("https://github.com/fatedier/frp/releases/download/v0.51.0/frp_0.51.0_windows_amd64.zip")

    def get_tunnels(self, ui=True):
        self.tunnels = self.session.get(f"{self.base_url}/tunnels").json()
        if ui:
            if len(self.tunnels) == 0:
                self.message_confirm("启动隧道", "您还没有隧道",
                                     yes=lambda: self.open_page("https://muhanfrp.cn/tunnels/create"),
                                     yes_text="创建隧道")
            else:
                self.select_tunnel.clear()
                for tunnel in self.tunnels:
                    self.select_tunnel.addItem(f"{tunnel['id']} | {tunnel['name']}")
                self.select_tunnel.setCurrentIndex(0)

    def start_tun(self):
        if not os.path.exists("config"):
            os.mkdir("config")
        self.detail = self.session.get(f"{self.base_url}/tunnels/{self.select_tunnel.currentText().split(' | ')[0]}")\
            .json()
        self.cfg = f"{self.detail['config']['server']}\n\n{self.detail['config']['client']}"
        if not os.path.exists(f"config/{self.detail['name']}.ini"):
            with open(f"config/{self.detail['name']}.ini", 'w', encoding="UTF-8") as f:
                f.write(self.cfg)
        os.system(f'start start.bat "{self.detail["name"]}" "config/{self.detail["name"]}.ini"')

        self.message_ok("启动隧道", f"隧道启动成功")

    def del_cfg(self):
        self.lenfiles = len(os.listdir("config"))
        if os.path.exists("config"):
            if self.lenfiles != 0:
                self.files = os.listdir("config")
                for file in self.files:
                    os.remove(f"config/{file}")
                self.message_ok("清理配置文件缓存", f"清理完成! 共清理了 {self.lenfiles} 个文件")
                return
        self.message_ok("清理配置文件缓存", "没有配置文件缓存可清理")

    def __init__(self):
        super().__init__()

        self.lenfiles = None
        self.files = None
        self.cfg = None
        self.detail = None
        self.tunnels = None
        self.response = None
        self.m = None
        self.setupUi(self)
        self.show()

        self.base_url = config.BASE_URL
        if not os.path.exists("frpc.exe"):
            self.start_tunnel_page.setDisabled(True)

        if os.path.exists("token.txt"):
            with open("token.txt", 'r', encoding='UTF-8') as f:
                self.tk = f.read()
            self.tk = base64.urlsafe_b64decode(self.tk.encode()).decode()
        else:
            self.message_ok("登录", "您尚未登录，请填写访问密钥后保存并重启软件即可登录")
            self.tk = ""
            self.download_frpc_page.setDisabled(True)
            self.user_page.setDisabled(True)
            self.start_tunnel_page.setDisabled(True)
            self.start_tunnel_page.setDisabled(True)
        if self.tk:
            if os.path.exists("frpc.exe"):
                self.tabWidget.setCurrentIndex(3)
            else:
                self.tabWidget.setCurrentIndex(1)

            self.session = requests.Session()
            self.session.headers = {
                "Authorization": f"Bearer {self.tk}",
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            self.user = self.session.get(f"{self.base_url}/user").json()
            self.create_time = datetime.strptime(self.user['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ") \
                .strftime("%Y年%m月%d日 %H时%M分%S秒")
            self.user_info.setText(f"{str(self.user['id'])}\n\n{self.user['name']}\n\n{self.user['email']}"
                                   f"\n\n{self.create_time}\n\n{self.user['traffic']} GB")
            self.get_tunnels()

        self.get_token.clicked.connect(lambda: self.open_page("https://muhanfrp.cn"))
        self.login_btn.clicked.connect(self.write_token)
        self.download.clicked.connect(self.download_frp)
        self.refresh_tunnels.clicked.connect(self.get_tunnels)
        self.start_tunnel.clicked.connect(self.start_tun)
        self.del_config.clicked.connect(self.del_cfg)
        self.github_page.clicked.connect(lambda: self.open_page("https://github.com/kingc2022/PortIO_Client"))


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    win = Ui()
    win.show()
    app.exec_()
