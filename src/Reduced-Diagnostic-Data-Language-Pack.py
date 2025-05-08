import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QGroupBox, QCheckBox, QLineEdit, QPushButton, 
    QLabel, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class LanguageSelector(QGroupBox):
    selectionChanged = pyqtSignal(list)

    def __init__(self, languages, parent=None):
        super().__init__("", parent)
        self.all_languages = languages
        self.setup_ui()
        self.setup_style()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 5, 20, 20)

        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)
        
        self.load_all_languages()

    def setup_style(self):
        self.setFont(QFont("微软雅黑", 10))

    def load_all_languages(self):
        row, col = 0, 0
        for lang in self.all_languages:
            cb = QCheckBox(lang["name"])
            cb.setObjectName(lang["name"]) 
            cb.setChecked(lang.get("default", False))
            cb.stateChanged.connect(lambda: self.selectionChanged.emit(self.get_selected()))
            cb.setStyleSheet("""
                QCheckBox {
                    font-size: 16px;
                    spacing: 8px;
                    padding: 5px 0;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                }
            """)
            self.grid_layout.addWidget(cb, row, col)
            col = (col + 1) % 3
            row += col == 0

    def get_selected(self):
        return [lang for lang in self.all_languages 
                if self.findChild(QCheckBox, lang["name"]).isChecked()]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_styles()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(800, 600)

    def init_ui(self):
        self.setWindowTitle("Reduced Diagnostic Data Language Pack for ODIS & ODIS-E")
        self.setWindowIcon(QIcon(resource_path("src/VW.ico")))
        self.setGeometry(300, 300, 800, 600)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        label = QLabel("Select the language you want to save：")
        label.setFont(QFont("微软雅黑", 12))
        main_layout.insertWidget(0, label)

        languages = [
            {"name": "čeština (cs_CZ)", "suffix": "cs_CZ_", "default": False},
            {"name": "dansk (da_DK)", "suffix": "da_DK_", "default": False},
            {"name": "Deutsch (de_DE)", "suffix": "de_DE_", "default": True},
            {"name": "Ελληνικά (el_GR)", "suffix": "el_GR_", "default": False},
            {"name": "English (GB) (en_GB)", "suffix": "en_GB_", "default": False},
            {"name": "English (US) (en_US)", "suffix": "en_US_", "default": True},
            {"name": "Español (es_ES)", "suffix": "es_ES_", "default": False},
            {"name": "suomea (fi_FI)", "suffix": "fi_FI_", "default": False},
            {"name": "français (fr_FR)", "suffix": "fr_FR_", "default": False},
            {"name": "hrvatski (hr_HR)", "suffix": "hr_HR_", "default": False},
            {"name": "magyar (hu_HU)", "suffix": "hu_HU_", "default": False},
            {"name": "Italiano (it_IT)", "suffix": "it_IT_", "default": False},
            {"name": "国語 (JP) (ja_JP)", "suffix": "ja_JP_", "default": False},
            {"name": "한국어 (KR) (ko_KR)", "suffix": "ko_KR_", "default": False},
            {"name": "Nederlands (NL) (nl_NL)", "suffix": "nl_NL_", "default": False},
            {"name": "polski (PL) (pl_PL)", "suffix": "pl_PL_", "default": False},
            {"name": "Português (PT) (pt_PT)", "suffix": "pt_PT_", "default": False},
            {"name": "P у с с к и й (RU) (ru_RU)", "suffix": "ru_RU_", "default": False},
            {"name": "slovenščina (SI) (sl_SI)", "suffix": "sl_SI_", "default": False},
            {"name": "svenska (SE) (sv_SE)", "suffix": "sv_SE_", "default": False},
            {"name": "Türkçe (TR) (tr_TR)", "suffix": "tr_TR_", "default": False},
            {"name": "中国的 (zh_CN)", "suffix": "zh_CN_", "default": True},
            {"name": "român (RO) (ro_RO)", "suffix": "ro_RO_", "default": False},
            {"name": "Português (BR) (pt_BR)", "suffix": "pt_BR_", "default": False},
        ]

        self.lang_selector = LanguageSelector(languages)
        self.lang_selector.selectionChanged.connect(self.update_selection)
        main_layout.addWidget(self.lang_selector)

        operation_panel = QWidget()
        operation_layout = QVBoxLayout(operation_panel)
        
        operation_layout.addWidget(QLabel("Path："))
        
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Click select button to choose root folder")
        operation_layout.addWidget(self.path_input)
        
        browse_btn = QPushButton("Select Folder (B)")
        browse_btn.clicked.connect(self.browse_path)
        operation_layout.addWidget(browse_btn)
        
        process_btn = QPushButton("Process (P)")
        process_btn.clicked.connect(self.start_process)
        operation_layout.addWidget(process_btn)
        operation_layout.addStretch(1)
        label = QLabel("版本：V1.0.1 vagtools.com")
        label.setAlignment(Qt.AlignRight)
        operation_layout.addWidget(label)
        
        main_layout.addWidget(operation_panel)

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
            }
            QGroupBox {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                min-width: 100px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                font-size: 12px;
            }
        """)

    def browse_path(self):
        path = QFileDialog.getExistingDirectory(self, "Choose Folder")
        if path:
            self.path_input.setText(path)

    def start_process(self):
        selected = self.lang_selector.get_selected()
        unselected_suffixes = [lang["suffix"] for lang in self.lang_selector.all_languages if lang not in selected]

        base_path = self.path_input.text()
        if not base_path:
            QMessageBox.warning(self, "Path not selected", "Please select a root folder path first!", QMessageBox.Ok)
            return

        self.delete_unselected_languages(base_path, unselected_suffixes)
        QMessageBox.information(self, "Processing Completed", "All files for unselected languages ​​have been deleted and logs have been generated.", QMessageBox.Ok)

    def delete_unselected_languages(self, base_path, unselected_suffixes):
        log_file = os.path.join(base_path, "deletion_log.txt")
        with open(log_file, "w", encoding="utf-8") as log:
            for root, _, files in os.walk(base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    for suffix in unselected_suffixes:
                        if suffix.lower() in file.lower():
                            try:
                                os.remove(file_path)
                                log.write(f"Deleted files: {file_path}\n")
                            except Exception as e:
                                log.write(f"Failed to delete file: {file_path}, Error: {e}\n")

    def update_selection(self, selected):
        print(f"Current Selected：{len(selected)} languages")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())