from PyQt6.QtCore import QEvent, QSize, Qt
from PyQt6.QtGui import QColor, QFontDatabase, QIcon, QPixmap, QPainter
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QMainWindow,n
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QSpacerItem,
    QSplitter,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtSvg import QSvgRenderer


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("CustomTitleBar")
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(10, 5, 10, 5)
        title_bar_layout.setSpacing(0)
        self.setStyleSheet(
            """
            CustomTitleBar {
                background-color: #28323F;
            }
            QLabel {
                text-transform: uppercase; 
                font-size: 16pt; 
                margin-left: 48px;
                color: white;
                background-color: transparent;
                border: none;
            }
            QToolButton {
                background-color: #28323F;
                border: none;
                color: white;
            }
            QToolButton:checked {
                background-color: #28323F;
                border: none;
                color: white;
            }
            """
        )
        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if title := parent.windowTitle():
            self.title.setText(title)
        title_bar_layout.addWidget(self.title)

        
        # Min button
        self.min_button = QToolButton(self)
        min_icon = self.recolor_svg("icons/window-shrink-symbolic.svg", QColor("white"))
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Restore Down or rather, default window size
        self.normal_button = QToolButton(self)
        normal_icon = self.recolor_svg("icons/arrows-pointing-inward-symbolic.svg", QColor("white"))
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)

        # Max button
        self.max_button = QToolButton(self)
        max_icon = self.recolor_svg("icons/window-grow-symbolic.svg", QColor("white"))
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = self.recolor_svg("icons/cross-large-symbolic.svg", QColor("white"))
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)
        
        # Add buttons
        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        button_style = """
        QToolButton {
            background-color: #28323F;
            color: #7B8187;
        }
        QToolButton:checked {
            background-color: #28323F;
            color: white;
        }
        """
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(32, 32))
            button.setStyleSheet(button_style)
            title_bar_layout.addWidget(button)

    @staticmethod
    def recolor_svg(svg_path, color):
        renderer = QSvgRenderer(svg_path)
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        # Apply color overlay
        painter.begin(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()

        return QIcon(pixmap)

    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # App

        self.setObjectName("Tweaks - Extra!")
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width: int = screen_geometry.width()
        screen_height: int = screen_geometry.height()
        QApplication.setFont(QFontDatabase.systemFont(
            QFontDatabase.SystemFont.GeneralFont)
            )
        self.setWindowTitle("Tweaks - Extra!")
        self.resize(int(screen_width * 0.35), int(screen_height * 0.40))
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


        # App > MainWindow

        main_window_widget = QWidget()
        main_window_widget.setObjectName("Container")
        main_window_widget.setStyleSheet(
            """#Container {
            background-color: #0F1419;
            border-radius: 5px;
        }"""
        )
        main_window_layout = QVBoxLayout()
        main_window_layout.setContentsMargins(0, 0, 0, 0)
        main_window_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        

        # App > MainWindow > TitleBar (Row: 1, Colspan: 2)
        title_bar_container = QWidget()
        title_bar_container.setObjectName("TitleBarContainer")
        title_bar_container.setStyleSheet(
            """#TitleBarContainer {
                background-color: #28323F;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }"""
        )
        title_bar_layout = QHBoxLayout()
        title_bar_layout.setContentsMargins(0, 0, 0, 0)
        title_bar_layout.setSpacing(0)
        title_bar_container.setLayout(title_bar_layout)
        self.title_bar = CustomTitleBar(self)
        title_bar_layout.addWidget(self.title_bar)
        


        # App > MainWindow > CentralWidget (Row: 2, Cols: 1,2)

        central_widget_layout = QVBoxLayout()
        central_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        central_widget_layout.setContentsMargins(0, 0, 0, 0)
        central_widget_layout.setSpacing(0)
        
        
        # App > MainWindow > CentralWidget > Actions (Row: 2, Col: 1)
        actions_widget = QWidget()
        actions_widget.setStyleSheet(
            """#ActionsWidget {
                background-color: #28323f;
            }"""
        )
        actions_layout = QVBoxLayout()
        actions_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(0)


        # ...Action #1

        button_style = """
        QPushButton {
            background-color: #28323F;
            border: none;
            color: #7B8187;
            font-size: 14pt;
            padding: 10px 30px;
            text-align: left;
        }
        QPushButton:checked {
            background-color: #28323F;
            border: noen;
            color: white;
            font-size: 14pt;
            padding: 10px 30px;
            text-align: left;
        }
        """
        action_one_button = QPushButton("Audio Input (Source) Devices")
        action_one_button.setStyleSheet(button_style)
        action_one_button.setCheckable(True)


        action_two_button = QPushButton("Audio Output (Sink) Devices")
        action_two_button.setStyleSheet(button_style)
        action_two_button.setCheckable(True)

        button_group = QButtonGroup(self)
        button_group.addButton(action_one_button)
        button_group.addButton(action_two_button)

        # ...Add Actions to ActionsLayout
        actions_layout.addWidget(action_one_button)
        actions_layout.addWidget(action_two_button)
        actions_widget.setLayout(actions_layout)


        # App > MainWindow > CentralWidget > Content (Row: 2, Col 2)

        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)



        content_widget.setLayout(content_layout)


        # ...Add Actions to ContentLayout; Use Splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(actions_widget)
        splitter.addWidget(content_widget)
        splitter.setSizes([200, screen_width - 200])  # Initial sizes 
        central_widget_layout.addWidget(splitter)
        vertical_spacer = QSpacerItem(
            20, 
            40, 
            QSizePolicy.Policy.Minimum, 
            QSizePolicy.Policy.Expanding
            )
        central_widget_layout.addItem(vertical_spacer)

        # App > MainWindow > StatusBar (Row: 3, Colspan: 2)
        
        status_bar_container = QWidget()
        status_bar_container.setObjectName("StatusBarContainer")
        status_bar_container.setStyleSheet(
            """#StatusBarContainer {
                background-color: #28323F;
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
            }"""
        )
        status_bar_layout = QHBoxLayout(status_bar_container)
        status_bar = QStatusBar()
        status_bar.setStyleSheet("background-color: #28323F; color: #7B8187;")
        status_bar_layout.addWidget(status_bar)
        status_bar_container.setLayout(status_bar_layout)
        fixed_height = 30
        status_bar_container.setFixedHeight(fixed_height)
        status_bar.setFixedHeight(fixed_height)


        # App > Layout and Widget Additions to MainWindow        
        
        main_window_layout.addWidget(title_bar_container)
        main_window_layout.addLayout(central_widget_layout)
        main_window_layout.addWidget(status_bar_container)
        main_window_widget.setLayout(main_window_layout)
        self.setCentralWidget(main_window_widget)


    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()

    
    def window_state_changed(self, state):
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)

    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

   
    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    
    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()