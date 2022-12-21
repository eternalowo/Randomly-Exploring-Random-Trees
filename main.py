import RRT
import graph
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.flag = False

        self.qinit = None
        self.qgoal = None
        self.edges = []
        self.vertices = []
        self.result = []
        self.obstacles = []
        self.message = ''
        self.iterations = 100

        self.setObjectName("Window")
        self.setStyleSheet("background-color: rgb(255, 236, 112);\n"
                           "border-radius: 20;")

        self.import_button = QPushButton(self)
        self.import_button.setGeometry(QRect(20, 740, 181, 41))
        self.import_button.setStyleSheet("background-color: rgb(170, 237, 255);\n"
                                         "border-radius:20;\n"
                                         "font: 75 14pt \"MS Sans Serif\";")
        self.import_button.setObjectName("import_button")
        self.import_button.setText("Import")
        self.import_button.clicked.connect(self.import_file)

        self.export_button = QPushButton(self)
        self.export_button.setGeometry(QRect(230, 740, 181, 41))
        self.export_button.setStyleSheet("background-color: rgb(170, 237, 255);\n"
                                         "border-radius:20;\n"
                                         "font: 75 14pt \"MS Sans Serif\";")
        self.export_button.setObjectName("export_button")
        self.export_button.setText("Export")
        self.export_button.clicked.connect(self.export_file)

        self.add_qinit_button = QPushButton(self)
        self.add_qinit_button.setGeometry(QRect(940, 30, 191, 41))
        self.add_qinit_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                            "border-radius:20;\n"
                                            "font: 75 14pt \"MS Sans Serif\";")
        self.add_qinit_button.setObjectName("add_qinit_button")
        self.add_qinit_button.setText("Add Qinit")
        self.add_qinit_button.clicked.connect(self.add_qinit)

        self.input_qinit = QLineEdit(self)
        self.input_qinit.setGeometry(QRect(940, 90, 191, 31))
        self.input_qinit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10;")
        self.input_qinit.setObjectName("input_qinit")

        self.add_qgoal_button = QPushButton(self)
        self.add_qgoal_button.setGeometry(QRect(940, 140, 191, 41))
        self.add_qgoal_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                            "border-radius:20;\n"
                                            "font: 75 14pt \"MS Sans Serif\";")
        self.add_qgoal_button.setObjectName("add_qgoal_button")
        self.add_qgoal_button.setText("Add QGoal")
        self.add_qgoal_button.clicked.connect(self.add_qgoal)

        self.input_qgoal = QLineEdit(self)
        self.input_qgoal.setGeometry(QRect(940, 200, 191, 31))
        self.input_qgoal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10;")
        self.input_qgoal.setObjectName("input_qgoal")

        self.add_obstacle_button = QPushButton(self)
        self.add_obstacle_button.setGeometry(QRect(940, 440, 191, 41))
        self.add_obstacle_button.setStyleSheet("background-color: rgb(170, 237, 255);\n"
                                               "border-radius:20;\n"
                                               "font: 75 14pt \"MS Sans Serif\";")
        self.add_obstacle_button.setObjectName("add_obstacle_button")
        self.add_obstacle_button.setText("Add Obstacle")
        self.add_obstacle_button.clicked.connect(self.add_obstacle)

        self.input_obstacle = QLineEdit(self)
        self.input_obstacle.setGeometry(QRect(940, 500, 191, 31))
        self.input_obstacle.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 10;\n"
                                          "")
        self.input_obstacle.setObjectName("input_obstacle")

        self.remove_obstacles_button = QPushButton(self)
        self.remove_obstacles_button.setGeometry(QRect(940, 550, 191, 41))
        self.remove_obstacles_button.setStyleSheet("background-color: rgb(170, 237, 255);\n"
                                                   "border-radius:20;\n"
                                                   "font: 75 14pt \"MS Sans Serif\";")
        self.remove_obstacles_button.setObjectName("remove_obstacles_button")
        self.remove_obstacles_button.setText("Remove Obstacles")
        self.remove_obstacles_button.clicked.connect(self.remove_obstacles)

        self.start_button = QPushButton(self)
        self.start_button.setGeometry(QRect(940, 680, 191, 41))
        self.start_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                        "border-radius:20;\n"
                                        "font: 75 14pt \"MS Sans Serif\";")
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Start Algorithm")
        self.start_button.clicked.connect(self.start_algorithm)

        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(QRect(940, 740, 191, 41))
        self.exit_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                       "border-radius:20;\n"
                                       "font: 75 14pt \"MS Sans Serif\";")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("Exit")
        self.exit_button.clicked.connect(self.stop_exec)

        self.input_iterations = QLineEdit(self)
        self.input_iterations.setGeometry(QRect(940, 310, 191, 31))
        self.input_iterations.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 10;")
        self.input_iterations.setObjectName("input_iterations")

        self.add_iterations_button = QPushButton(self)
        self.add_iterations_button.setGeometry(QRect(940, 250, 191, 41))
        self.add_iterations_button.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                                 "border-radius:20;\n"
                                                 "font: 75 14pt \"MS Sans Serif\";")
        self.add_iterations_button.setObjectName("add_iterations_button")
        self.add_iterations_button.setText("Set Iterations")
        self.add_iterations_button.clicked.connect(self.get_iterations)

    def add_qinit(self):
        self.qinit = tuple(int(item) for item in self.input_qinit.text().split(','))

    def add_qgoal(self):
        self.qgoal = tuple(int(item) for item in self.input_qgoal.text().split(','))

    def get_iterations(self):
        self.iterations = int(self.input_iterations.text())

    def add_obstacle(self):
        tup = tuple(int(item) for item in self.input_obstacle.text().split(','))
        self.obstacles.append(RRT.Rectangle((tup[0], tup[1]), (tup[2], tup[3])))

    def remove_obstacles(self):
        self.obstacles = []

    def stop_exec(self):
        exit(1)

    def import_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'r') as F:
            lines = F.readlines()
        self.iterations = int(lines[0])
        self.qinit = tuple(map(int, lines[1].split(', ')))
        self.qgoal = tuple(map(int, lines[2].split(', ')))
        for i in range(3, len(lines)):
            line = tuple(map(int, lines[i].split(', ')))
            self.obstacles.append(RRT.Rectangle((line[0], line[1]), (line[2], line[3])))

    def export_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        with open(f'{filename}', 'w') as F:
            F.write(f'{self.iterations}' + '\n')
            F.write(f'{self.qinit}'[1:-1:] + '\n')
            F.write(f'{self.qgoal}'[1:-1:] + '\n')
            for item in self.obstacles:
                F.write(f'{item.min_p}'[1:-1:] + ', ' + f'{item.max_p}'[1:-1:])

    def start_algorithm(self):
        self.edges, self.result, self.vertices, self.message = RRT.rapidly_exploring_random_trees(self.iterations,
                                                                                                  self.qinit,
                                                                                                  self.qgoal,
                                                                                                  self.obstacles)
        self.flag = True

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QPen(Qt.white, 20, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawRect(20, 20, 900, 700)

        if self.flag:
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))

            for obstacle in self.obstacles:
                painter.drawLine(20 + obstacle.points[0][0], 20 + RRT.MAXIMUM_Y - obstacle.points[0][1],
                                 20 + obstacle.points[2][0], 20 + RRT.MAXIMUM_Y - obstacle.points[2][1])
                painter.drawLine(20 + obstacle.points[1][0], 20 + RRT.MAXIMUM_Y - obstacle.points[1][1],
                                 20 + obstacle.points[2][0], 20 + RRT.MAXIMUM_Y - obstacle.points[2][1])
                painter.drawLine(20 + obstacle.points[1][0], 20 + RRT.MAXIMUM_Y - obstacle.points[1][1],
                                 20 + obstacle.points[3][0], 20 + RRT.MAXIMUM_Y - obstacle.points[3][1])
                painter.drawLine(20 + obstacle.points[0][0], 20 + RRT.MAXIMUM_Y - obstacle.points[0][1],
                                 20 + obstacle.points[3][0], 20 + RRT.MAXIMUM_Y - obstacle.points[3][1])

            painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
            for edge in self.edges:
                painter.drawLine(20 + edge[0][0], 20 + RRT.MAXIMUM_Y - edge[0][1],
                                 20 + edge[1][0], 20 + RRT.MAXIMUM_Y - edge[1][1])

            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            for i in range(len(self.result) - 1):
                painter.drawLine(20 + self.result[i][0], 20 + RRT.MAXIMUM_Y - self.result[i][1],
                                 20 + self.result[i + 1][0], 20 + RRT.MAXIMUM_Y - self.result[i + 1][1])

            painter.setPen(QPen(Qt.green, 10, Qt.SolidLine))
            painter.drawEllipse(20 + self.qinit[0] - 2, 20 + RRT.MAXIMUM_Y - self.qinit[1] - 2, 4, 4)

            painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
            painter.drawEllipse(20 + self.qgoal[0] - 2, 20 + RRT.MAXIMUM_Y - self.qgoal[1] - 2, 4, 4)

            self.update()
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.resize(1147, 815)
    ex.show()
    sys.exit(app.exec_())
