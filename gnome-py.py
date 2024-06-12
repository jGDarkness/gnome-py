from PyQt6.QtCore import (
    QEvent, 
    QSize, 
    Qt
)
from PyQt6.QtGui import (
    QFontDatabase, 
    QAction, 
    QIcon,
    QMouseEvent,
    QPalette
)

from PyQt6.QtWidgets import (
    QApplication, 
    QHBoxLayout,
    QLabel,
    QMainWindow, 
    QMessageBox,
    QStyle,
    QToolButton, 
    QVBoxLayout,
    QWidget
)


import os
import sys

# This application provides a GUI for editing certain system settings that aren't typically available by default in GNOME. 
# The initial release will handle listing all audio devices, provide the user the ability to rename them, and to hide them
# as desired. 

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ColorRole.Window)
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(0, 0, 0, 0)
        title_bar_layout.setSpacing(2)

        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setStyleSheet(
            """font-weight: bold;
               margin: 2px;
               margin-left: 48px;
            """
        )
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if title := parent.windowTitle():
            self.title.setText(title)
        title_bar_layout.addWidget(self.title)

        self.min_button = QToolButton(self)
        min_icon = QIcon("icons/window-shrink-symbolic.svg")
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Restore Down or rather, default window size
        self.normal_button = QToolButton(self)
        normal_icon = QIcon("icons/arrows-pointing-inward-symbolic.svg")
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)
        
        # Max button
        self.max_button = QToolButton(self)
        max_icon = QIcon("icons/window-grow-symbolic.svg")
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = QIcon("icons/cross-large-symbolic.svg")
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)


        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(36, 36))
            button.setStyleSheet(
                """QToolButton { border: 0px solid white;
                                 border-radius: 0px;
                                }
                """
            )
            title_bar_layout.addWidget(button)



    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)



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



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        """
        Qt Main Window Framework - Layout
        
        Intial Version of this app will not have any Dock Widgets.

        |---------------------------|
        | Title Bar                 |
        |---------------------------|
        | Menu Bar                  |   
        |---------------------------|
        |         Toolbars          |
        |---------------------------|
        |       Dock Widgets        |
        |   ---------------------   |
        |   |                   |   |
        |   |   Central Widget  |   |
        |   |                   |   |
        |   ---------------------   |
        |                           |
        |---------------------------|
        |         Status Bar        |
        |---------------------------|
        
        """
        

        ##### Default Color Palette ########################################################################################

        w = "#ffffff"       # Universal White
        vlg = "#fafafa"     # Very Light Gray
        lg = "#efefef"      # Light Gray
        dg = "#242424"      # Dark Gray
        vdg = "#1e1e1e"     # Very Dark Gray
        h = "#15539e"       # Universal Highlight
        b = "#000000"       # Universal Black
        
        light_mode_toolbar = f"background-color: {vlg}; color: {vlg}; font-size: 14px;"
        dark_mode_toolbar = f"background-color: {vdg}; color: {w}; font-size: 14px;"
        highlighted_toolbar = f"background-color: {h}; color: {w}; font-size: 14px;"

        light_mode_central = f"background-color: {lg}; color: {dg}; font-size: 14px; border-radius: 7px;"
        dark_mode_central = f"background-color: {dg}; color: {lg}; font-size: 14px;"



        ##### System Attributes ############################################################################################

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width: int = screen_geometry.width()
        screen_height: int = screen_geometry.height()

        QApplication.setFont(QFontDatabase.systemFont(QFontDatabase.SystemFont.GeneralFont))



        ##### QMainWindow Object ###########################################################################################

        self.setWindowTitle("GNOME Hidden Settings Editor")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(light_mode_central)
        
        window_width: int = int(screen_width * 0.35)
        window_height: int = int(screen_height * 0.40)
        self.resize(window_width, window_height)

        workspace_layout = QVBoxLayout()
        workspace_layout.setContentsMargins(3, 3, 3, 3)
        workspace_layout.addWidget(QLabel("Hello, World!", self))

        ##### QTitleBar Object #############################################################################################

        self.title_bar = CustomTitleBar(self)


        ##### QMenuBar Object ##############################################################################################
                
        

        ##### QToolBar Object #############################################################################################



        ##### QDockWidgets Object #########################################################################################



        ##### QCentral Widget Object ######################################################################################

        central_widget = QWidget()
        central_widget.setObjectName("Container")
        central_widget.setStyleSheet(light_mode_central)

        central_widget_layout = QVBoxLayout()
        central_widget_layout.setContentsMargins(10, 10, 10, 10)
        central_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        central_widget_layout.addWidget(self.title_bar)
        central_widget_layout.addLayout(workspace_layout)

        central_widget.setLayout(central_widget_layout) 

        ##### QStatusBar Object ###########################################################################################



        ##### Add Layouts to MainWindow ####################################################################################
        
        self.setCentralWidget(central_widget)



    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()



def gnome_check () -> bool:
    """
    This function checks to see if the current desktop session is GNOME, and returns a boolean along with the value of the 
    associated environment variable.
    """
    current_desktop_session: str = os.getenv('DESKTOP_SESSION')
    if current_desktop_session == 'gnome':
        return True
    else:
        msg_box_a = QMessageBox()
        msg_box_a.setIcon(QMessageBox.Icon.Warning)
        msg_box_a.setText(f"""
                          Only GNOME Desktop Sessions are supported. Your current desktop session is: 
                          {current_desktop_session}"""
                          )
        msg_box_a.setWindowTitle("Unsupported DESKTOP_SESSION")
        msg_box_a.exec()
        return False



def main():
    # Create the QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MainWindow()
    main_window.show()

    # First, check to ensure that the current 'DESKTOP_SESSION' environment 
    # variable is 'gnome'. If it is not, then notify the user that only GNOME 
    # sessions are supported.
    
    gnome_session = gnome_check()
    if not gnome_session:
        app.quit()
    else:
        sys.exit(app.exec())



if __name__ == "__main__":
    main()