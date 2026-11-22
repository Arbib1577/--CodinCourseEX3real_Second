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

        self.temperatures = []
        self.profits = []

        self.load_btn=QPushButton('Select CSV File', self)
        self.load_btn.setGeometry(30,20,170,38)
        self.load_btn.clicked.connect(self.load_file)

        self.file_label= QLabel('No file selected', self)
        self.file_label.setGeometry(215,20,360,38)

        self.about_btn = QPushButton('About', self)
        self.about_btn.setObjectName('about_btn')
        self.about_btn.setGeometry(610, 20, 120, 38)
        self.about_btn.clicked.connect(self.open_about)

        self.plot_container = QWidget(self)
        self.plot_container.setGeometry(30, 75, 700, 515)
        plot_layout = QVBoxLayout(self.plot_container)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

        self.about_window = None
        self.plot_placeholder()

    def plot_placeholder(self):
        self.figure.clear()
        ax= self.figure.add_subplot(111)
        ax.plot([1,2,3,4],[10,20,35,30])
        ax.set_title('Temporary Graph (Load CSV to Update)')
        self.canvas.draw()

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select Ice Cream CSV File',
            '',
            'CSV Files (*.csv);;All Files (*)'
        )
        if not file_path:
            return

        self.file_label.setText(file_path.split('/')[-1])
        self.temperatures.clear()
        self.profits.clear()

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines[1:]:
            line = line.strip()
            if line:
                parts = line.split(',')
                self.temperatures.append(float(parts[0]))
                self.profits.append(float(parts[1]))

        self.plot_data()

    def plot_data(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Scatter plot with point size = 1
        ax.scatter(self.temperatures, self.profits, s=1)

        # Remove top and right borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Title and axis labels
        ax.set_title('Ice Cream Sales Profits vs. Outside Temperature')
        ax.set_xlabel('Outside Temperature (°C)')
        ax.set_ylabel('Ice Cream Sales Profits ($)')

        self.canvas.draw()

    def open_about(self):
        if self.about_window is None:
            self.about_window = AboutWindow()
        self.about_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())