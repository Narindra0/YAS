import sys
import os

# Ajouter le répertoire du projet au path
sys.path.insert(0, os.path.dirname(__file__))

from src.main import simulate_ussd

if __name__ == "__main__":
    simulate_ussd()
