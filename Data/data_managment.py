#Sert à récupérer des donnés dans un fichier ou à y écrire, tous ceux qui est data

def lire(ligne,fichier):
    """ retourne le contenu de la ligne "i" du fichier spécifié, renvoie False si la ligne est vide """
    
    with open(fichier,'r') as file:
        line_content = file.readlines()[ligne-1]
        if line_content == '':
            return False
        return line_content
        
def ecrire(ligne,contenu,fichier):
    """écrit à la ligne "i" dans le fichier spécifié avec le contenu entré"""
    
    with open(fichier,'r') as file:
        file_content = file.readlines()
        file_content[ligne-1] = str(contenu)
        file_content = ''.join(file_content)
    with open(fichier,'w') as file:
        file.write(file_content)