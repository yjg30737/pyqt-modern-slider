# pyqt-modern-slider
PyQt modern styled slider

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-modern-slider`

## Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_modern_slider import ModernSlider

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = ModernSlider()
    example.show()
    app.exec_()
```

Preview

![image](https://user-images.githubusercontent.com/55078043/174434080-46db6da2-0356-4a86-bc9c-38e0fac29ce9.png)

## See Also
* <a href="https://github.com/yjg30737/pyqt-media-slider.git">pyqt-media-slider</a> - QSlider which is good to use in media player
* <a href="https://github.com/yjg30737/pyqt-label-slider.git">pyqt-label-slider</a> - QSlider which is connected with QLabel 
