import pygame
import pygame_menu
import json
import sys

# 🏁 - Initialisation de Pygame :
pygame.init()
pygame.font.init()
info = pygame.display.Info()

# 🔢 - Définition des constantes :

WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h
MENU_WIDTH = info.current_w
MENU_HEIGHT = info.current_h
TEXT_COLOR = (24,20,37)
FONT_SIZE = 32
FONT = pygame_menu.font.FONT_NEVIS


# 🎨 - Creation des Themes :

main_menu_theme = pygame_menu.Theme(
    background_color=(228, 59, 68), 
    title=False,
    title_background_color=TEXT_COLOR, 
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, 
    title_font=FONT,
    widget_alignment=pygame_menu.locals.ALIGN_LEFT, 
    widget_font=FONT, 
    widget_font_color=TEXT_COLOR,
    widget_font_size=72, 
    widget_margin=(64, 64))

options_menu_theme = pygame_menu.Theme(
    background_color=(254, 231, 97), 
    title_background_color=TEXT_COLOR,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL, 
    title_font=FONT,
    widget_border_width=0,  
    widget_font=FONT, 
    widget_font_color=(38,43,68), 
    widget_font_size=48)


# ⚙ - Fonction d'affichage des options :

with open("parametre.json","r") as f:
    r = json.load(f)

def show_options():
    # 📄 - Code pour afficher la page d'options :

    menu_options = pygame_menu.Menu("Options", MENU_WIDTH, MENU_HEIGHT, theme=options_menu_theme)
    menu_options.add.button("Retour", menu)
    for word in r:
        menu_options.add.label(word, font_size=FONT_SIZE, font_name=FONT, font_color=TEXT_COLOR)
        input_field = menu_options.add.text_input(f'', default=f'{r[word]}', onchange=lambda text, key=word: r.__setitem__(key, text), onreturn=on_text_entered,cursor_selection_enable=False)
        
     # Deselectionner le texte lors de l'appui sur la touche Entrée

    menu_options.mainloop(pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))


def on_text_entered(text_input):
    with open("parametre.json","w") as f:
        for i in r:
            r[i] = int(r[i])
        json.dump(r,f,indent=3)

    
# ❎ - Fonction de fermeture de l'application :

def quit_game():
    pygame.quit()
    sys.exit()

# 💻 - Création de la fenêtre Pygame :

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Le Jeu de l'Humanité")

# 🚩 - Création du menu principal :

menu = pygame_menu.Menu("Menu Principal", WINDOW_WIDTH, WINDOW_HEIGHT, theme=main_menu_theme)

menu.add.image("sprite/logo.png")
menu.add.button("Jouer", menu.disable)
menu.add.button("Options", show_options)
menu.add.button("Quitter", quit_game)
invisible_button = menu.add.button("", None)

# 💻 - Affichage du menu :

menu.mainloop(window)

# ✅ - Mise à jour de l'écran :

pygame.display.update()