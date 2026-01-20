import sys
import os

# Ajouter le répertoire du projet au path
sys.path.insert(0, os.path.dirname(__file__))

from src.interface import MvolaApp

if __name__ == "__main__":
    app = MvolaApp()
    app.mainloop()
