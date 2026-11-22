import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QWidget,
    QVBoxLayout
)

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from About import AboutWindow

class IceCreamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ice Cream Sales Analyzer')
        self.setGeometry(200,100,760,620)
        