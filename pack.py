import shutil
import os


def main():
    os.system("pyinstaller -w main.py")
    shutil.copy("frpc.exe", "dist/main/frpc.exe")
    shutil.copy("start.bat", "dist/main/start.bat")
    os.remove("main.spec")
    shutil.rmtree("build")


if __name__ == '__main__':
    main()
