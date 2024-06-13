import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox,QLineEdit
from PySide6.QtGui import QPixmap
import os
from etapa1 import Etapa1Window

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.nickname_label = QLabel("Apodo:")
        self.nickname_input = QLineEdit()

        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.check_credentials)

        layout.addWidget(self.nickname_label)
        layout.addWidget(self.nickname_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_credentials(self):
        nickname = self.nickname_input.text()
        password = self.password_input.text()

        # Verifica si las credenciales son correctas (nombre de usuario y contraseña iguales a "1")
        if nickname == "1" and password == "1":
            QMessageBox.information(self, "Inicio de Sesión", "¡Credenciales verificadas!\nRedirigiendo a la sala de carga.")
            self.loading_screen = LoadingScreen() # Guardamos la referencia a la sala de carga
            self.loading_screen.show()
            self.hide()  # Ocultamos la ventana de inicio de sesión
        else:
            QMessageBox.warning(self, "Inicio de Sesión", "Credenciales incorrectas. Inténtalo de nuevo.")

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sala de Carga")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.welcome_label = QLabel("¡Bienvenido a la Sala de Carga!")
        self.background_label = QLabel()

        # Imprimir la ruta completa de la imagen
        #print("Ruta de la imagen:", "asssets/cargas/carga.jpg")

        self.background_label.setPixmap(QPixmap("asssets/cargas/carga.jpeg")) # Imagen de fondo de la sala de carga

        self.start_button = QPushButton("Iniciar Juego")
        self.start_button.clicked.connect(self.start_game)

        layout.addWidget(self.welcome_label)
        layout.addWidget(self.background_label)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_game(self):
        # Al presionar el botón "Iniciar Juego", creamos una instancia de Etapa1Window y la mostramos
        self.etapa1_window = Etapa1Window()
        self.etapa1_window.show()
        self.hide()  # Ocultamos la sala de carga

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
