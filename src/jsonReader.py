import json as js


class JsonLecture:

    def __init__(self, chemin):
        self.url = chemin

    def charger_fichier(self):
        try:
            with open(self.url, 'r', encoding="UTF-8") as json_file:
                fichier = js.load(json_file)
            return fichier
        except FileNotFoundError:
            print("Le fichier spécifié n'existe pas")
            return None
        except js.JSONDecodeError:
            print(f"Erreur dans le décodage du json à l'URL {self.url}")
            return None

    def lire_fichier(self):
        fichier = self.charger_fichier()
        if fichier:
            return self.extraire_valeurs(fichier)

    def extraire_valeurs(self, fichier):
        valeurs = []
        for layer in fichier.get("layers", []):
            sous_layers = layer.get("layers", [])
            for sous_layer in sous_layers:
                if sous_layer.get("type") == "text":
                    texte = sous_layer.get("text", "")
                    valeurs.append({
                        "name": sous_layer.get("name"),
                        "type": sous_layer.get("type"),
                        "fontSize": sous_layer.get("size"),
                        "text": texte,
                        "coordinates": {
                            "x": sous_layer.get("x"),
                            "y": sous_layer.get("y")
                        }
                    })
                elif sous_layer.get("type") == "image":
                    image = sous_layer.get("image", "")
                    valeurs.append({
                        "name": sous_layer.get("name"),
                        "type": sous_layer.get("type"),
                        "image": image,
                        "src": sous_layer.get("src"),
                        "size": {
                            "w": sous_layer.get("width"),
                            "h": sous_layer.get("height")
                        },
                        "coordinates": {
                            "x": sous_layer.get("x"),
                            "y": sous_layer.get("y"),
                        }
                    })

        return valeurs

    def trouver_par_nom(self, nom_recherche):
        donnees = self.lire_fichier()
        for element in donnees:
            if element.get('name') == nom_recherche:
                return element
        return None



