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
            margin-top: 9px;
            margin-bottom: 9px;
        }

        QSlider::groove:horizontal {
            border: #000088;
            height: 8px;
            background: #6aa6ed;
            margin: 2px 0;
        }

        QSlider::handle:horizontal {
            background: white;

            border: 8px solid #6aa6ed;
            width: 24px;
            margin: -16px 0;
            border-radius: 20px;
        }
        QSlider::add-page:horizontal {
            background: white;
            height: 8px;
            margin: 2px 0;
        }
        '''
        self.setStyleSheet(slider)