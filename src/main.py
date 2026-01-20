import time
from src.ussd_engine import USSDSession
from src.utils import load_user_profile, clear_screen

def simulate_ussd():
    # Chargement du profil utilisateur
    user_profile = load_user_profile()
    session = USSDSession(user_profile)
    
    # Simulation du lancement
    print("Codes disponibles : #111# (Menu principal), #322# (Promotions), #359# (Mes infos)")
    code = input("Composez le code USSD : ")
    
    if code == "#111#":
        session.current_state = "MAIN_MENU"
    elif code == "#322#":
        session.current_state = "PROMOTION_MENU"
    elif code == "#359#":
        session.current_state = "MENU_359"
    elif code == "#100#":
        session.current_state = "MENU_CREDITS"
    else:
        print("Code invalide.")
        return

    print("Exécution du code USSD...")
    time.sleep(1)

    # Boucle principale
    while True:
        # Traiter le nœud actuel (compute, logic) jusqu'à avoir un écran affichable
        view = session.process_node()
        
        # Affichage
        clear_screen()
        
        # Gestion des erreurs
        if view.get("type") == "error":
            print(f"\n⚠️  ERREUR: {view.get('message')}\n")
            time.sleep(2)
            break
        
        # Formatage du texte avec les données de session
        display_text = view.get("text", "")
        
        # Affichage du titre et du texte
        print(f"\n--- {view.get('title', 'Menu')} ---")
        print(display_text)
        
        # Gestion du type "message" (fin de session)
        if view.get("type") == "message":
            input("\nAppuyez sur Entrée pour terminer...")
            print("Session terminée.")
            break
        
        # Gestion du type "finish"
        if view.get("type") == "finish":
            print("Session terminée.")
            break
        
        # Entrée utilisateur
        choice = input("\nRépondre : ")
        
        # Quitter
        if choice.lower() in ['quitter', 'cancel', 'q']:
            print("Session terminée.")
            break

        # Soumettre l'entrée au moteur USSD
        next_view = session.submit_input(choice)

if __name__ == "__main__":
    simulate_ussd()
