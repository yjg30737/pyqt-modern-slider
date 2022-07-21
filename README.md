# pyqt-modern-slider
PyQt modern styled slider

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-modern-slider`

## Example
```python
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
from pyqt_modern_slider import ModernSlider

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = ModernSlider()
    btn = QPushButton('Play')
    lay = QVBoxLayout()
    lay.addWidget(example)
    lay.addWidget(btn)
    mainWidget = QWidget()
    mainWidget.setLayout(lay)
    mainWidget.show()
    app.exec_()
```

Preview

![image](https://user-images.githubusercontent.com/55078043/180106917-8d1fc889-b748-4213-aa68-42f4af00cd72.png)

## See Also
* <a href="https://github.com/yjg30737/pyqt-media-slider.git">pyqt-media-slider</a> - QSlider which is good to use in media player
* <a href="https://github.com/yjg30737/pyqt-label-slider.git">pyqt-label-slider</a> - QSlider which is connected with QLabel 
