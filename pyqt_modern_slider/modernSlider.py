from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class ModernSlider(QSlider):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setOrientation(Qt.Horizontal)
        height = 8
        slider = f'''
        QSlider {{
            margin-top: {height+1}px;
            margin-bottom: {height+1}px;
        }}

        QSlider::groove:horizontal {{
            border: #000088;
            height: {height}px;
            background: #6aa6ed;
            margin: {height // 4}px 0;
        }}

        QSlider::handle:horizontal {{
            background: white;

            border: {height} solid #6aa6ed;
            width: {height * 3};
            margin: {height * 2 * -1} 0;
            border-radius: {height * 2 + height // 2}px;
        }}
        QSlider::add-page:horizontal {{
            background: white;
            height: {height}px;
            margin: {height // 4}px 0;
        }}
        '''
        self.setStyleSheet(slider)