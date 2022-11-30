import RRT
import graph
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def create_obstacle(self):
        self.obstacles.append(
            RRT.Rectangle((int(self.obstacle_min_input_x.text()), int(self.obstacle_min_input_y.text())),
                          (int(self.obstacle_max_input_x.text()), int(self.obstacle_max_input_y.text()))))

    def algorithm_start(self):

        qinit = (int(self.qinit_input_x.text()), int(self.qinit_input_y.text()))
        qend = (int(self.qend_input_x.text()), int(self.qend_input_y.text()))
        n = (int(self.iterations_input.text()))
        obstacles = self.obstacles
        self.qinit = qinit
        self.qend = qend
        self.edges = self.rapidly_exploring_random_trees(n, qinit, qend, obstacles)

        self.flag = True

    def __init__(self):
        super().__init__()

        self.flag = False

        self.qinit = None
        self.qend = None
        self.edges = []
        self.obstacles = []

        self.rrt_start = QPushButton(self)
        self.rrt_start.setGeometry(QRect(RRT.MAXIMUM_X + 180, 640, 151, 41))
        self.rrt_start.setObjectName("rrt_start")
        self.rrt_start.setText("Start Algorithm")
        self.rrt_start.clicked.connect(self.algorithm_start)

        self.iterations_lable = QLabel(self)
        self.iterations_lable.setGeometry(QRect(RRT.MAXIMUM_X + 180, 410, 151, 20))
        self.iterations_lable.setObjectName("iterations_lable")
        self.iterations_lable.setText("Enter the number of iterations")

        self.iterations_input = QLineEdit(self)
        self.iterations_input.setGeometry(QRect(RRT.MAXIMUM_X + 180, 440, 151, 31))
        self.iterations_input.setObjectName("iterations_input")

        self.obstacle_max_input_x = QLineEdit(self)
        self.obstacle_max_input_x.setGeometry(QRect(RRT.MAXIMUM_X + 180, 240, 31, 31))
        self.obstacle_max_input_x.setObjectName("obstacle_max_input_x")

        self.obstacle_max_label = QLabel(self)
        self.obstacle_max_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 210, 171, 20))
        self.obstacle_max_label.setObjectName("obstacle_max_label")
        self.obstacle_max_label.setText("Enter rectangle max point")

        self.obstacle_push_button = QPushButton(self)
        self.obstacle_push_button.setGeometry(QRect(RRT.MAXIMUM_X + 180, 360, 151, 41))
        self.obstacle_push_button.setObjectName("obstacle_push_button")
        self.obstacle_push_button.setText("Add obstacle")
        self.obstacle_push_button.clicked.connect(self.create_obstacle)

        self.qinit_label = QLabel(self)
        self.qinit_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 480, 151, 20))
        self.qinit_label.setObjectName("qinit_label")
        self.qinit_label.setText("Enter the starting point")

        self.obstacle_min_input_x = QLineEdit(self)
        self.obstacle_min_input_x.setGeometry(QRect(RRT.MAXIMUM_X + 180, 310, 31, 31))
        self.obstacle_min_input_x.setObjectName("obstacle_min_input_x")

        self.obstacle_min_label = QLabel(self)
        self.obstacle_min_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 280, 171, 20))
        self.obstacle_min_label.setObjectName("obstacle_min_label")
        self.obstacle_min_label.setText("Enter rectangle min point")

        self.rrt_label = QLabel(self)
        self.rrt_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 140, 201, 21))
        self.rrt_label.setObjectName("rrt_label")
        self.rrt_label.setText("Rapidly Exploring Random Trees Algorithm")

        self.alert_label = QLabel(self)
        self.alert_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 180, 201, 16))
        self.alert_label.setObjectName("alert_label")
        self.alert_label.setText("All values should be entered as integers!")

        self.obstacle_max_input_y = QLineEdit(self)
        self.obstacle_max_input_y.setGeometry(QRect(RRT.MAXIMUM_X + 220, 240, 31, 31))
        self.obstacle_max_input_y.setObjectName("obstacle_max_input_y")

        self.obstacle_min_input_y = QLineEdit(self)
        self.obstacle_min_input_y.setGeometry(QRect(RRT.MAXIMUM_X + 220, 310, 31, 31))
        self.obstacle_min_input_y.setObjectName("obstacle_min_input_y")

        self.qinit_input_x = QLineEdit(self)
        self.qinit_input_x.setGeometry(QRect(RRT.MAXIMUM_X + 180, 510, 31, 31))
        self.qinit_input_x.setObjectName("qinit_input_x")

        self.qinit_input_y = QLineEdit(self)
        self.qinit_input_y.setGeometry(QRect(RRT.MAXIMUM_X + 220, 510, 31, 31))
        self.qinit_input_y.setObjectName("qinit_input_y")

        self.qend_input_x = QLineEdit(self)
        self.qend_input_x.setGeometry(QRect(RRT.MAXIMUM_X + 180, 580, 31, 31))
        self.qend_input_x.setObjectName("qend_input_x")

        self.qend_input_y = QLineEdit(self)
        self.qend_input_y.setGeometry(QRect(RRT.MAXIMUM_X + 220, 580, 31, 31))
        self.qend_input_y.setObjectName("qend_input_y")

        self.qend_label = QLabel(self)
        self.qend_label.setGeometry(QRect(RRT.MAXIMUM_X + 180, 550, 151, 20))
        self.qend_label.setObjectName("qend_label")
        self.qend_label.setText("Enter the ending point")

    def rapidly_exploring_random_trees(self, n, q_init, q_end, obstacles):

        g = graph.Graph()
        g.add_vertex(q_init)

        for i in range(n):
            try:
                q_rand = RRT.random_sample()
                qn = RRT.nearest(g, q_rand)
                if qn != q_rand:
                    qs = RRT.steer(qn, q_rand, obstacles)
                    g.add_edge(qn, qs)
            except ValueError:
                pass
        last = RRT.nearest(g, q_end)
        g.add_edge(last, q_end)

        return g.edges

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawLine(RRT.MAXIMUM_X, RRT.MAXIMUM_Y, RRT.MAXIMUM_X, 0)
        painter.drawLine(0, RRT.MAXIMUM_Y, RRT.MAXIMUM_X, RRT.MAXIMUM_Y)

        if self.flag:
            painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
            for obstacle in self.obstacles:
                if obstacle.if_inside(self.qinit) or obstacle.if_inside(self.qend):
                    print("Can't reach Q_end")
                    exit(1)
                painter.drawLine(obstacle.points[0][0], RRT.MAXIMUM_Y - obstacle.points[0][1],
                                 obstacle.points[2][0], RRT.MAXIMUM_Y - obstacle.points[2][1])
                painter.drawLine(obstacle.points[1][0], RRT.MAXIMUM_Y - obstacle.points[1][1],
                                 obstacle.points[2][0], RRT.MAXIMUM_Y - obstacle.points[2][1])
                painter.drawLine(obstacle.points[1][0], RRT.MAXIMUM_Y - obstacle.points[1][1],
                                 obstacle.points[3][0], RRT.MAXIMUM_Y - obstacle.points[3][1])
                painter.drawLine(obstacle.points[0][0], RRT.MAXIMUM_Y - obstacle.points[0][1],
                                 obstacle.points[3][0], RRT.MAXIMUM_Y - obstacle.points[3][1])

            painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
            for edge in self.edges:
                painter.drawLine(edge[0][0], RRT.MAXIMUM_Y - edge[0][1], edge[1][0], RRT.MAXIMUM_Y - edge[1][1])

            painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(self.qinit[0] - 5, RRT.MAXIMUM_Y - self.qinit[1] - 5, 10, 10)

            painter.setPen(QPen(Qt.red, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawEllipse(self.qend[0] - 5, RRT.MAXIMUM_Y - self.qend[1] - 5, 10, 10)

            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawLine(RRT.MAXIMUM_X, RRT.MAXIMUM_Y, RRT.MAXIMUM_X, 0)
            painter.drawLine(0, RRT.MAXIMUM_Y, RRT.MAXIMUM_X, RRT.MAXIMUM_Y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.resize(RRT.MAXIMUM_X + 400, RRT.MAXIMUM_Y + 250)
    ex.show()
    sys.exit(app.exec_())
