from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class ModernSlider(QSlider):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setOrientation(Qt.Horizontal)
        slider = '''
        QSlider {
            margin-top: 3px;
            margin-bottom: 3px;
        }

        QSlider::groove:horizontal {
            border: #000088;
            height: 3px;
            background: #6aa6ed;
            margin: 2px 0;
        }

        QSlider::handle:horizontal {
            background: white;
            border: 4px solid #6aa6ed;
            width: 9px;
            margin: -7px 0;
            border-radius: 8px;
        }
        QSlider::add-page:horizontal {
            background: white;
            margin: 2px 0;
        }
        '''
        self.setStyleSheet(slider)