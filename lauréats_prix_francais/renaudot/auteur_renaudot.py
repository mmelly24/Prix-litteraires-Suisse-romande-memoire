"""
"""
import re
from pathlib import Path

# Creation des chemins pour les fichiers source et destination
DATA_FILE_PATH = Path("./laureat_renaudot.txt")
RESULTS_FILE_PATH = Path("./final_auteur_renaudot.xslx")

def main():
    """Programme principal"""

    # Recuperation du fichier source et stockage de son contenu dans une variable
    if DATA_FILE_PATH.exists():
        try:
            with DATA_FILE_PATH.open(mode="r", encoding="utf-8") as fichier:
                content = fichier.read()
        except IOError:
            print("Error while retrieving data from file.")
    else:
        print("Data file not found.")
            
    # Definition regex pour extraction des données
    regex = re.compile(r"(\d+) \| ([A-Z].*) \| ([A-Z].*) \| (.*)")
        
    #Création d'une liste contenant les données correspondant à la regex
    matchs = list()
    for match in regex.finditer(content):
        matchs.append(match)
            
    #Sauvergarde de la liste extraite dans le fichier destination
    with RESULTS_FILE_PATH.open(mode="w", encoding="utf-8") as fichier:
        for match in matchs:
            fichier.write(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}\t{match.group(4)}\n")
                


if __name__ == "__main__":
    main()

