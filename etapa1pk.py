import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox
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
        self.characters = [
            Character("Guerrero", 100, 20, "asssets/personajes/guerrero.jpeg", "Golpe Espada"),
            Character("Mago", 100, 20, "asssets/personajes/mago.jpeg", "Volar de Fuego"),
            Character("Caballero", 100, 20, "asssets/personajes/caballero.jpeg", "Espadazo"),
            Character("Arquero Elfo", 100, 20, "asssets/personajes/arquero.jpeg", "Flecha Precisa"),
            Character("Lancero", 100, 20, "asssets/personajes/lanzero.jpeg", "Lanzar Lanza")
        ]
        self.current_character = self.characters[0]  # Inicialmente seleccionamos al primer personaje

        main_layout = QVBoxLayout()

        # Layout vertical para el monstruo
        monster_layout = QVBoxLayout()
        main_layout.addLayout(monster_layout)

        # Etiqueta para mostrar la vida del monstruo
        self.monster_health_label = QLabel(f"Vida del Monstruo: {self.monster_health}")
        self.monster_health_label.setFont(QFont("Arial", 16))
        monster_layout.addWidget(self.monster_health_label)

        # Imagen del monstruo
        self.monster_image = QLabel()
        self.monster_image.setPixmap(QPixmap("asssets/vichos x/jefe esqueleto.jpeg").scaledToWidth(300))
        self.monster_image.setAlignment(Qt.AlignCenter)
        monster_layout.addWidget(self.monster_image)

        # Layout para el personaje activo
        self.active_character_layout = QVBoxLayout()
        main_layout.addLayout(self.active_character_layout)

        # Selector de personajes
        self.character_selector = QComboBox()
        self.character_selector.addItems([char.name for char in self.characters])
        self.character_selector.currentIndexChanged.connect(self.update_active_character)
        main_layout.addWidget(self.character_selector)

        # Botón de ataque
        self.attack_button = QPushButton(self.current_character.special_ability)
        self.attack_button.setStyleSheet("background-color: black; color: white;")
        self.attack_button.clicked.connect(self.attack_monster)
        main_layout.addWidget(self.attack_button)

        # Botón para curar a los personajes
        self.heal_button = QPushButton("Curar")
        self.heal_button.clicked.connect(self.heal_characters)
        self.heal_button.setStyleSheet("background-color: black; color: white;")
        main_layout.addWidget(self.heal_button)

        self.setLayout(main_layout)
        self.update_active_character(0)

    def update_active_character(self, index):
        # Actualizar el personaje activo basado en la selección
        self.current_character = self.characters[index]
        self.update_active_character_layout()

    def update_active_character_layout(self):
        # Limpiar el layout del personaje activo
        for i in reversed(range(self.active_character_layout.count())):
            self.active_character_layout.itemAt(i).widget().setParent(None)

        # Añadir la imagen y la vida del personaje activo
        character_label = QLabel(f"{self.current_character.name}: {self.current_character.health}")
        character_label.setAlignment(Qt.AlignCenter)
        self.active_character_layout.addWidget(character_label)

        character_image = QLabel()
        character_image.setPixmap(QPixmap(self.current_character.image_path).scaledToWidth(100))
        character_image.setAlignment(Qt.AlignCenter)
        self.active_character_layout.addWidget(character_image)

    def attack_monster(self):
        # Simular el ataque del personaje activo
        damage = self.current_character.damage

        # Aplicar el daño al monstruo
        self.monster_health -= damage
        if self.monster_health <= 0:
            self.monster_health = 0
            QMessageBox.information(self, "Victoria", "¡Has derrotado al monstruo!")
            self.close()
        else:
            self.monster_health_label.setText(f"Vida del Monstruo: {self.monster_health}")

            # Ejecutar la habilidad especial del personaje
            target = random.choice([char for char in self.characters if char.health > 0])  # Se elige un objetivo vivo al azar
            self.current_character.use_special_ability(target)

            # Actualizar la etiqueta de la vida del objetivo
            target_label = [label for label in self.findChildren(QLabel) if label.text().startswith(f"{target.name}:")][0]
            target_label.setText(f"{target.name}: {target.health}")

            if target.health <= 0:
                QMessageBox.information(self, "Derrota", f"¡{target.name} ha sido derrotado!")
                target_image = [label for label
            in self.findChildren(QLabel) if label.pixmap() and target.image_path in label.pixmap().toImage().text()][0]
            target_image.setPixmap(QPixmap("asssets/creacion de personajes/muerto.jpeg").scaledToWidth(100)) # Ruta de la imagen del cadáver


            # Eliminar el personaje derrotado del selector
            self.character_selector.removeItem(self.character_selector.findText(target.name))

            # Cambiar al siguiente personaje disponible
            if self.character_selector.count() > 0:
                self.character_selector.setCurrentIndex(0)
                self.update_active_character(0)
            else:
                QMessageBox.information(self, "Derrota", "¡Todos los personajes han sido derrotados!")
                self.close()

    def heal_characters(self):
        # curación de los personajes
        for character in self.characters:
            if character.health > 0:
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