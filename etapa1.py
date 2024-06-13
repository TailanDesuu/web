import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox, QGridLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

class Character:
    def __init__(self, name, health, damage, image_path, special_ability):
        self.name = name
        self.health = health
        self.damage = damage
        self.image_path = image_path
        self.special_ability = special_ability

    def use_special_ability(self, target):
        if self.special_ability == "Golpe Espada":
            target.health -= self.damage * 2  # Doble daño al objetivo
        elif self.special_ability == "Volar de Fuego":
            target.health -= self.damage  # Daño normal al objetivo y a sí mismo
            self.health -= self.damage
        elif self.special_ability == "Espadazo":
            target.health -= self.damage  # Daño normal al objetivo
        elif self.special_ability == "Flecha Precisa":
            target.health -= self.damage * 2  # Doble daño al objetivo
        elif self.special_ability == "Lanzar Lanza":
            target.health -= self.damage  # Daño normal al objetivo

class Etapa1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etapa 1: Batalla contra el Monstruo")
        self.setGeometry(100, 100, 800, 600)

        # Vida inicial del monstruo y los personajes
        self.monster_health = 1000
        self.round_count = 0
        self.characters = [
            Character("Guerrero", 100, 20, "asssets/personajes/guerrero.jpeg", "Golpe Espada"),
            Character("Mago", 100, 20, "asssets/personajes/mago.jpeg", "Volar de Fuego"),
            Character("Caballero", 100, 20, "asssets/personajes/caballero.jpeg", "Espadazo"),
            Character("Arquero Elfo", 100, 20, "asssets/personajes/arquero.jpeg", "Flecha Precisa"),
            Character("Lancero", 100, 20, "asssets/personajes/lanzero.jpeg", "Lanzar Lanza")
        ]

        layout = QVBoxLayout()

        # Fondo de la ventana
        self.background_label = QLabel()
        self.background_label.setPixmap(QPixmap(""))
        layout.addWidget(self.background_label)

        # Layout vertical para el monstruo
        monster_layout = QVBoxLayout()
        layout.addLayout(monster_layout)

        # Etiqueta para mostrar la vida del monstruo
        self.monster_health_label = QLabel(f"Vida del Monstruo: {self.monster_health}")
        self.monster_health_label.setFont(QFont("Arial", 16))
        monster_layout.addWidget(self.monster_health_label)

        # Imagen del monstruo
        self.monster_image = QLabel()
        self.monster_image.setPixmap(QPixmap("asssets/vichos x/jefe esqueleto.jpeg").scaledToWidth(300))
        self.monster_image.setAlignment(Qt.AlignCenter)
        monster_layout.addWidget(self.monster_image)

        # Layout horizontal para los personajes
        characters_layout = QHBoxLayout()
        layout.addLayout(characters_layout)

        for character in self.characters:
            character_widget = QWidget()
            character_widget.setMaximumWidth(150)

            character_layout = QVBoxLayout()
            character_widget.setLayout(character_layout)

            character_label = QLabel(f"{character.name}: {character.health}")
            character_label.setAlignment(Qt.AlignCenter)
            character_layout.addWidget(character_label)

            character_image = QLabel()
            character_image.setPixmap(QPixmap(character.image_path).scaledToWidth(100))
            character_image.setAlignment(Qt.AlignCenter)
            character_layout.addWidget(character_image)

            attack_button = QPushButton(character.special_ability)
            attack_button.setStyleSheet("background-color: black; color: white;")
            attack_button.clicked.connect(lambda _, character=character: self.character_attack(character))
            character_layout.addWidget(attack_button)

            characters_layout.addWidget(character_widget)

        # Botón para curar a los personajes
        self.heal_button = QPushButton("Curar")
        self.heal_button.clicked.connect(self.heal_characters)
        self.heal_button.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.heal_button)

        self.setLayout(layout)

    def character_attack(self, character):
        # Simular el ataque de un personaje
        damage = character.damage

        # Aplicar el daño al monstruo
        self.monster_health -= damage
        if self.monster_health <= 0:
            self.monster_health = 0
            QMessageBox.information(self, "Victoria", "¡Has derrotado al monstruo!")
            self.close()
        else:
            self.monster_health_label.setText(f"Vida del Monstruo: {self.monster_health}")

            # Ejecutar la habilidad especial del personaje
            target = random.choice(self.characters)  # Se elige un objetivo al azar
            character.use_special_ability(target)

            # Actualizar la etiqueta de la vida del objetivo
            target_label = [label for label in self.findChildren(QLabel) if label.text().startswith(f"{target.name}:")][0]
            target_label.setText(f"{target.name}: {target.health}")

    def heal_characters(self):
        # Simular curación de los personajes
        # Se curará a todos los personajes
        for character in self.characters:
            character.health += 20  # Se puede ajustar la cantidad de curación
            if character.health > 100:  # Limitar la vida máxima a 100
                character.health = 100
            character_label = [label for label in self.findChildren(QLabel) if label.text().startswith(f"{character.name}:")][0]
            character_label.setText(f"{character.name}: {character.health}")
        QMessageBox.information(self, "Curación", "Todos los personajes han sido curados.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    etapa1_window = Etapa1Window()
    etapa1_window.show()
    sys.exit(app.exec_())
