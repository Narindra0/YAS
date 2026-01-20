import customtkinter as ctk
import tkinter as tk
import time
from datetime import datetime
import random

# Backend integration
from data.ussd_menus import USSD_DATA
from src.ussd_engine import USSDSession
from src import utils
import data.tarifs as tarif

# Configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# --- DESIGN SYSTEM ---
class C:
    # Palette principale
    PRIMARY = "#10b981"      # Emerald 500
    PRIMARY_HOVER = "#059669" # Emerald 600
    ACCENT = "#3b82f6"       # Blue 500
    
    # Structure Téléphone
    PHONE_BG = "#0f172a"     # Slate 900
    CHASSIS = "#020617"      # Slate 950
    BORDER = "#334155"       # Slate 700
    
    # Écran et Textes
    SCREEN_BG = "#ffffff"
    TEXT_MAIN = "#1f2937"    # Gray 800
    TEXT_SEC = "#6b7280"     # Gray 500
    TEXT_WHITE = "#ffffff"
    
    # Clavier
    KEY_BG = "#f1f5f9"       # Slate 100
    KEY_HOVER = "#e2e8f0"    # Slate 200
    KEY_TEXT = "#0f172a"     # Slate 900
    
    # UI Elements
    DANGER = "#ef4444"       # Red 500
    SUCCESS = "#22c55e"      # Green 500
    OVERLAY = "#000000"      # Opacité gérée via alpha si possible, sinon simulation
    LOADING = "#f3f4f6"

    # Fonts
    FONT_FAMILY = "Segoe UI" # Windows standard, clean
    
# --- GUI ---
class MvolaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.session = USSDSession()  # Utilise le moteur USSD externalisé
        
        # Setup Window
        self.title("Mvola Pro")
        self.geometry("400x750")
        self.configure(fg_color=C.PHONE_BG)
        self.resizable(False, False)
        
        self.dialer_code = ""
        self.setup_ui()
        self.show_dialer()
        
    def setup_ui(self):
        # Container principal (Téléphone)
        self.phone_frame = ctk.CTkFrame(
            self, width=360, height=710,
            corner_radius=40,
            fg_color=C.CHASSIS,
            border_width=4, border_color=C.BORDER
        )
        self.phone_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.phone_frame.pack_propagate(False)

        # Status Bar
        self.status_bar = ctk.CTkFrame(self.phone_frame, height=30, fg_color="transparent")
        self.status_bar.pack(fill="x", padx=25, pady=(15, 5))
        
        ctk.CTkLabel(self.status_bar, text="12:00", font=(C.FONT_FAMILY, 12), text_color="white").pack(side="left")
        ctk.CTkLabel(self.status_bar, text="🔋 100%", font=(C.FONT_FAMILY, 12), text_color="white").pack(side="right")
        ctk.CTkLabel(self.status_bar, text="📶 4G+", font=(C.FONT_FAMILY, 12), text_color="white").pack(side="right", padx=10)

        # Screen Area
        self.screen = ctk.CTkFrame(
            self.phone_frame, width=330, height=600,
            corner_radius=25,
            fg_color=C.SCREEN_BG
        )
        self.screen.pack(padx=15, pady=(5, 15), fill="both", expand=True)
        self.screen.pack_propagate(False) # Strict size
        
        # Home Indicator
        ctk.CTkFrame(
            self.phone_frame, width=100, height=5,
            corner_radius=10, fg_color="#334155"
        ).pack(pady=10)

    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    # --- DIALER VIEW ---
    def show_dialer(self):
        self.clear_screen()
        # Dialer styling
        self.screen.configure(fg_color="#f8fafc") # Light gray bg
        
        # Display Zone
        display_frame = ctk.CTkFrame(self.screen, fg_color="transparent")
        display_frame.pack(pady=(40, 20), fill="x")
        
        self.lbl_code = ctk.CTkLabel(
            display_frame, text=self.dialer_code,
            font=(C.FONT_FAMILY, 32, "bold"),
            text_color=C.TEXT_MAIN
        )
        self.lbl_code.pack()
        
        ctk.CTkLabel(
            display_frame, text="Entrez le code USSD",
            font=(C.FONT_FAMILY, 12),
            text_color=C.TEXT_SEC
        ).pack(pady=5)

        # Keypad Grid
        keypad = ctk.CTkFrame(self.screen, fg_color="transparent")
        keypad.pack(pady=10)
        
        keys = [
            ('1', ''), ('2', 'ABC'), ('3', 'DEF'),
            ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'),
            ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ'),
            ('*', ''), ('0', '+'), ('#', '')
        ]
        
        for i, (digit, sub) in enumerate(keys):
            row = i // 3
            col = i % 3
            
            btn = ctk.CTkButton(
                keypad, width=70, height=70,
                corner_radius=35,
                fg_color=C.KEY_BG, hover_color=C.KEY_HOVER,
                text="", # Custom layout inside
                command=lambda d=digit: self.on_digit(d)
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            
            # Button content trick to have Main number and subtext
            lbl_digit = tk.Label(btn, text=digit, bg=C.KEY_BG, fg=C.KEY_TEXT, font=(C.FONT_FAMILY, 24, "bold"), bd=0)
            lbl_digit.place(relx=0.5, rely=0.4, anchor="center")
            lbl_digit.bind("<Button-1>", lambda e, d=digit: self.on_digit(d)) # Pass click through
            
            if sub:
                lbl_sub = tk.Label(btn, text=sub, bg=C.KEY_BG, fg=C.TEXT_SEC, font=(C.FONT_FAMILY, 9, "bold"), bd=0)
                lbl_sub.place(relx=0.5, rely=0.75, anchor="center")
                lbl_sub.bind("<Button-1>", lambda e, d=digit: self.on_digit(d))

        # Action Buttons
        actions = ctk.CTkFrame(self.screen, fg_color="transparent")
        actions.pack(pady=20, fill="x")
        
        # Call Button
        call_btn = ctk.CTkButton(
            actions, text="📞", width=70, height=70,
            corner_radius=35,
            fg_color=C.SUCCESS, hover_color="#16a34a",
            font=("Segoe UI Emoji", 28),
            command=self.on_call
        )
        call_btn.pack(side="bottom")
        
        # Delete Button (Top of call button visually or side)
        del_btn = ctk.CTkButton(
            self.screen, text="⌫", width=40, height=40,
            fg_color="transparent", hover_color=C.KEY_HOVER,
            text_color=C.TEXT_SEC, font=(C.FONT_FAMILY, 20),
            command=self.on_delete
        )
        del_btn.place(relx=0.8, rely=0.85, anchor="center")

    def on_digit(self, digit):
        if len(self.dialer_code) < 15:
            self.dialer_code += digit
            self.lbl_code.configure(text=self.dialer_code)

    def on_delete(self):
        self.dialer_code = self.dialer_code[:-1]
        self.lbl_code.configure(text=self.dialer_code)

    def on_call(self):
        # Easter Egg: Developer Credits Call
        if self.dialer_code == "0341171113":
            self.draw_modal_box(
                "Info Développeur",
                "👨‍💻 Narindra Ranjalahy\n\nMerci d'utiliser YAS USSD Simulator !\n\n© 2026",
                input_type="message",
                is_message=True
            )
            return

        if self.dialer_code.startswith("*") or self.dialer_code.startswith("#"):
            self.show_loading()
            # Start logic
            if self.dialer_code == "#359#":
                self.session.current_state = "MENU_359"
            elif self.dialer_code == "#100#":
                self.session.current_state = "MENU_CREDITS"
            else:
                self.session.current_state = "MAIN_MENU"
            
            self.after(1000, self.start_ussd)
        else:
            # Simulation d'appel normal (non implémenté)
            self.lbl_code.configure(text_color=C.DANGER)
            self.after(500, lambda: self.lbl_code.configure(text_color=C.TEXT_MAIN))

    def show_loading(self):
        # Overlay loader
        self.loader_frame = ctk.CTkFrame(self.screen, fg_color=C.OVERLAY)
        self.loader_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        ctk.CTkLabel(
            self.loader_frame, text="Exécution du code USSD...",
            text_color="white", font=(C.FONT_FAMILY, 14)
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        self.progress = ctk.CTkProgressBar(self.loader_frame, width=150, progress_color=C.PRIMARY)
        self.progress.place(relx=0.5, rely=0.55, anchor="center")
        self.progress.start()

    # --- USSD ENGINE VIEW ---
    def start_ussd(self):
        if hasattr(self, 'loader_frame'):
            self.loader_frame.destroy()
            
        data = self.session.process_node()
        self.render_ussd_modal(data)

    def render_ussd_modal(self, data):
        # Nous simulons une modale par dessus l'écran (soit app phone soit ecran gris)
        self.clear_screen()
        # Wallpaper vague/abstrait vert sombre pour "background" de l'écran derrière la modale
        bg = ctk.CTkFrame(self.screen, fg_color="#064e3b")
        bg.pack(fill="both", expand=True)

        if data.get("type") == "finish":
            # Just close
            ctk.CTkButton(bg, text="Session terminée", font=(C.FONT_FAMILY, 16), command=self.show_dialer).pack(expand=True)
            return

        if data.get("type") == "error":
            # Error modal
            self.draw_modal_box("Erreur", data.get("message"), is_error=True)
            return

        # Normal USSD Box
        is_msg = (data.get("type") == "message")
        self.draw_modal_box(data.get("title"), data.get("text"), data.get("input_type"), is_message=is_msg)

    def draw_modal_box(self, title, text, input_type="choice", is_error=False, is_message=False):
        # Modal Container
        container = ctk.CTkFrame(
            self.screen, width=300,  # Increased width
            fg_color="white", corner_radius=15
        )
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Header
        ctk.CTkLabel(
            container, text=title, 
            font=(C.FONT_FAMILY, 18, "bold"),
            text_color=C.DANGER if is_error else C.PRIMARY
        ).pack(pady=(15, 5), padx=20, anchor="w")
        
        # BodyText
        ctk.CTkLabel(
            container, text=text,
            font=(C.FONT_FAMILY, 16), text_color=C.TEXT_MAIN,
            justify="left", anchor="w", wraplength=270 # Adjusted wrap
        ).pack(pady=5, padx=20, fill="x")
        
        # Input Area (Hidden for messages and errors)
        self.ussd_entry = ctk.CTkEntry(
            container, placeholder_text="Répondre",
            font=(C.FONT_FAMILY, 14), border_color="#e2e8f0",
            fg_color="white", text_color="black" # White input
        )
        
        if not is_error and not is_message:
            self.ussd_entry.pack(padx=20, pady=10, fill="x")
            self.ussd_entry.focus_set()
            self.ussd_entry.bind("<Return>", lambda e: self.submit_ussd())

        # Buttons
        btn_row = ctk.CTkFrame(container, fg_color="transparent")
        btn_row.pack(fill="x", padx=20, pady=(0, 15))
        
        if is_error or is_message:
            # Single "Valider" button
             ctk.CTkButton(
                btn_row, text="Valider", text_color=C.PRIMARY,
                fg_color="transparent", hover_color="#ecfdf5",
                width=260, command=self.exit_ussd
            ).pack(fill="x")
        else:
            # Standard two buttons
            ctk.CTkButton(
                btn_row, text="Annuler", text_color=C.TEXT_SEC,
                fg_color="transparent", hover_color="#f1f5f9",
                width=80, command=self.exit_ussd
            ).pack(side="left")
            
            ctk.CTkButton(
                btn_row, text="Envoyer", text_color=C.PRIMARY,
                fg_color="transparent", hover_color="#ecfdf5",
                width=80, command=self.submit_ussd
            ).pack(side="right")

    def submit_ussd(self):
        val = self.ussd_entry.get()
        if not val: return
        
        # Loading interaction
        self.loader_frame = ctk.CTkFrame(self.screen, fg_color="#333333") # Fixed: Solid color instead of RGBA
        self.loader_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        ctk.CTkLabel(self.loader_frame, text="Traitement...", text_color="white").place(relx=0.5, rely=0.5, anchor="center")
        
        # Use simple reload effect
        self.after(200, lambda: self.process_submission(val))

    def process_submission(self, val):
        next_step = self.session.submit_input(val)
        if hasattr(self, 'loader_frame'):
            self.loader_frame.destroy()
        self.render_ussd_modal(next_step)

    def exit_ussd(self):
        self.dialer_code = ""
        self.show_dialer()

if __name__ == "__main__":
    app = MvolaApp()
    app.mainloop()