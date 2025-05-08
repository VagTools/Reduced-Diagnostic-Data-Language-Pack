# 精简诊断数据语言包

## 概述
此软件旨在管理和处理用于 ODIS 和 ODIS-E 诊断工具的语言包。用户可以选择特定语言，并从指定目录中删除不必要的语言文件，从而节省存储空间并提高组织效率。

## 软件截图

以下是该软件运行的一些截图:

![Screenshot](./Screenshots/Image_20250508192750_1310.png)

## 功能
- 用户友好的图形界面，用于选择语言。
- 从指定目录中删除未选择的语言文件。
- 生成已删除文件的日志文件。

## 构建和打包说明

### 前置条件
要构建和打包此软件，请确保已安装以下依赖项：
- Python 3.8 或更高版本
- PyQt5

您可以使用以下命令安装所需依赖项：
```bash
pip install -r requirements.txt
```

### 打包
要将软件打包为可执行文件，请使用 `PyInstaller`：
```bash
pip install pyinstaller
pyinstaller --hidden-import=win32timezone --onefile --noconsole --icon=src/VW.ico --name=Reduced-Diagnostic-Data-Language-Pack --collect-binaries=pyzbar --add-data "src/VW.ico;src" .\src\Reduced-Diagnostic-Data-Language-Pack.py
```
打包后的可执行文件将位于 `dist` 目录中。
