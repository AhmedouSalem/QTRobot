import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class RobotGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jeu de Robot - Résoudre l'opération")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        self.layout = QVBoxLayout()

        # Affichage du robot
        self.robot_label = QLabel(self)
        self.robot_pixmap = QPixmap("neutre.png")  # Assurez-vous que l'image est dans le bon dossier
        if not self.robot_pixmap.isNull():
            print("Image 'robot_neutre.png' chargée avec succès.")
        else:
            print("Erreur de chargement de l'image 'robot_neutre.png'.")
        self.robot_pixmap = self.robot_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Redimensionner
        self.robot_label.setPixmap(self.robot_pixmap)
        self.robot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.robot_label)

        # Générer la première opération aléatoire
        self.generate_new_question()

        # Affichage de l'opération
        self.operation_label = QLabel(f"Quel est le résultat de {self.num1} {self.operation} {self.num2} ?", self)
        self.layout.addWidget(self.operation_label)

        # Champ de saisie de la réponse
        self.answer_input = QLineEdit(self)
        self.layout.addWidget(self.answer_input)

        # Bouton pour vérifier la réponse
        self.check_button = QPushButton("Vérifier", self)
        self.check_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.check_button)

        # Zone de résultat (indication de bonne ou mauvaise réponse)
        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        # Configuration du layout
        self.setLayout(self.layout)

    def generate_new_question(self):
        """ Génère une nouvelle question mathématique """
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operation = random.choice(["+", "-", "*"])
        self.correct_answer = self.compute_answer()

    def compute_answer(self):
        """ Calcule la réponse correcte en fonction de l'opération """
        if self.operation == "+":
            return self.num1 + self.num2
        elif self.operation == "-":
            return self.num1 - self.num2
        elif self.operation == "*":
            return self.num1 * self.num2

    def check_answer(self):
        """ Vérifie la réponse donnée par l'utilisateur et génère une nouvelle question en cas de bonne réponse """
        try:
            user_answer = int(self.answer_input.text())
            if user_answer == self.correct_answer:
                self.result_label.setText("Bravo ! Vous avez trouvé la bonne réponse.")
                self.robot_pixmap = QPixmap("happy.png")  # Remplacez par le chemin de votre image
                if not self.robot_pixmap.isNull():
                    print("Image 'robot_joyeux.png' chargée avec succès.")
                else:
                    print("Erreur de chargement de l'image 'happy.png'.")
                self.robot_pixmap = self.robot_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Redimensionner l'image
                self.generate_new_question()  # Nouvelle question après une bonne réponse
                self.operation_label.setText(f"Quel est le résultat de {self.num1} {self.operation} {self.num2} ?")
                self.answer_input.clear()  # Réinitialiser le champ de saisie
            else:
                self.result_label.setText("Dommage ! Essayez encore.")
                self.robot_pixmap = QPixmap("mecontent.gif")  # Remplacez par le chemin de votre image
                if not self.robot_pixmap.isNull():
                    print("Image 'robot_mecontent.png' chargée avec succès.")
                else:
                    print("Erreur de chargement de l'image 'robot_mecontent.png'.")
                self.robot_pixmap = self.robot_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Redimensionner l'image
            self.robot_label.setPixmap(self.robot_pixmap)
        except ValueError:
            self.result_label.setText("Veuillez entrer un nombre valide.")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = RobotGame()
    window.show()

    sys.exit(app.exec())
