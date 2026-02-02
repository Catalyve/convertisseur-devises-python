import os
import currency_converter
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon


class App(QtWidgets.QWidget):
    """Application de conversion de devises avec interface graphique."""

    def __init__(self):
        """Initialise l'application, les composants et les styles."""
        super().__init__()

        self.c = currency_converter.CurrencyConverter(
            fallback_on_missing_rate=True
        )

        self.setWindowTitle("Convertisseur de devises")

        base_path = os.path.dirname(__file__)
        logo_path = os.path.join(base_path, "styles", "logo.png")
        self.setWindowIcon(QIcon(logo_path))

        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
        self.load_style()

    def setup_ui(self):
        """Construit l'interface utilisateur et les widgets."""
        self.layout = QtWidgets.QHBoxLayout(self)

        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QDoubleSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QDoubleSpinBox()

        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
        self.lbl_taux = QtWidgets.QLabel("Taux : -")
        self.btn_copier = QtWidgets.QPushButton("Copier")
        self.historique = QtWidgets.QListWidget()

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
        self.layout.addWidget(self.lbl_taux)
        self.layout.addWidget(self.btn_copier)
        self.layout.addWidget(self.historique)

    def set_default_values(self):
        """Configure les valeurs initiales et les paramètres par défaut."""
        devises = sorted(self.c.currencies)

        self.cbb_devisesFrom.addItems(devises)
        self.cbb_devisesTo.addItems(devises)

        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("USD")

        for spin in (self.spn_montant, self.spn_montantConverti):
            spin.setRange(0.01, 1_000_000_000)
            spin.setDecimals(2)

        self.spn_montant.setValue(100.00)
        self.spn_montantConverti.setValue(0.00)

    def setup_connections(self):
        """Relie les actions utilisateur aux fonctions."""
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)
        self.btn_copier.clicked.connect(self.copier_resultat)

    def compute(self):
        """Effectue la conversion et met à jour l'affichage."""
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
            taux = self.c.convert(1, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            QMessageBox.warning(
                self,
                "Conversion impossible",
                "Les taux de change pour cette devise ne sont pas disponibles."
            )
            return

        self.spn_montantConverti.setValue(resultat)
        self.lbl_taux.setText(
            f"Taux : 1 {devise_from} = {taux:.4f} {devise_to}"
        )

        ligne = f"{montant:.2f} {devise_from} → {resultat:.2f} {devise_to}"
        self.historique.insertItem(0, ligne)

    def inverser_devise(self):
        """Inverse les devises source et cible."""
        from_dev = self.cbb_devisesFrom.currentText()
        to_dev = self.cbb_devisesTo.currentText()

        self.cbb_devisesFrom.setCurrentText(to_dev)
        self.cbb_devisesTo.setCurrentText(from_dev)

        self.compute()

    def copier_resultat(self):
        """Copie le montant converti dans le presse-papiers."""
        valeur = self.spn_montantConverti.value()
        QtWidgets.QApplication.clipboard().setText(f"{valeur:.2f}")

    def load_style(self):
        """Charge et applique le style graphique QSS."""
        base_path = os.path.dirname(__file__)
        qss_path = os.path.join(base_path, "styles", "style.qss")

        with open(qss_path, "r", encoding="utf-8") as f:
            qss = f.read()

        self.setStyleSheet(qss.replace("\\", "/"))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec()
