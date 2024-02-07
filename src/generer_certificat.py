from jsonReader import JsonLecture
from PdfClass import PDFCreation
from Medecin import Medecin
import os
import random as rd


def create_certif(prenom, nom, sexe, date_naissance, date_absence, nombre_jour_absence,
                  code_postal_patient, adresse_patient, remote=True):
    replacement = ""
    medecin = Medecin(remote=True)
    tag = {":prenom:": prenom, ":nom:": nom, ":sexe:": sexe, ":date_naissance:": date_naissance,
           ":date_absence:": date_absence, ":motif:": "", ":nombre_jour_absence:": nombre_jour_absence,
           ":telephone_medecin:": medecin.numero_medecin, ":adresse_patient:": adresse_patient,
           ":code_postal_patient:": code_postal_patient,
           ":nom_centre:": medecin.nom_centre, ":adresse_centre:": medecin.adresse_medecin,
           ":code_postal_centre:": medecin.code_postal_medecin, ":ville_centre:": medecin.ville_medecin,
           ":finess:": medecin.finess,
           ":nom_medecin:": medecin.nom_medecin}

    liste_fichier = []
    liste_sign = []

    try:
        if remote:
            liste_fichier = os.listdir("./Ressources/JSON/remote/")

        else:
            for root, dirs, fichiers in os.walk("./Ressources/JSON/"):
                for fichier in fichiers:
                    liste_fichier.append(os.path.join(root, fichier))

        liste_sign = os.listdir("./Ressources/signatures/")

    except OSError as e:
        print(f"Erreur lors de l'accès au répertoire 'JSON': {e}")

    if liste_fichier:
        nom_fichier = rd.choice(liste_fichier)

        model = JsonLecture(f"./Ressources/JSON/remote/{nom_fichier}")
        contenu_json = model.charger_fichier()

        if contenu_json:
            donnees = model.extraire_valeurs(contenu_json)
            certificat = PDFCreation()
            certificat.ajouter_page()

            for element in donnees:
                if element['name'] == 'pre' and element['type'] == 'text':
                    x = element['coordinates'].get('x')
                    y = element['coordinates'].get('y')
                    text = element['text']
                    certificat.police(element['fontSize'])
                    if len(text) > 80:
                        certificat.ajouter_texte(x, y, text, 550)
                    else:
                        certificat.ajouter_texte(x, y, text)
                elif element['name'] == 'pre' and element['type'] == 'image':
                    x = element['coordinates'].get('x')
                    y = element['coordinates'].get('y')
                    file = f"./Ressources/{element['src']}"
                    w, h = element['size'].get('w'), element['size'].get('h')
                    certificat.ajouter_image(x, y, file, w, h)
                elif element['name'] == 'sign' and element['type'] == 'image':
                    x = element['coordinates'].get('x')
                    y = element['coordinates'].get('y')
                    file = f"./Ressources/{element['src']}/{rd.choice(liste_sign)}"
                    w, h = element['size'].get('w'), element['size'].get('h')
                    certificat.ajouter_image(x, y, file, w, h)

                elif element['name'] != 'pre' and element['type'] == 'text':
                    for key, value in tag.items():
                        if key in element['text']:
                            print(f"Remplacement de {key} par {value}")
                            if isinstance(value, str):
                                replacement = value
                            elif isinstance(value, list):
                                replacement = "\n".join(map(str, value))

                            element['text'] = element['text'].replace(key, replacement)
                    x = element['coordinates'].get('x')
                    y = element['coordinates'].get('y')
                    text = element['text']
                    certificat.police(element['fontSize'])
                    if len(text) > 80:
                        certificat.ajouter_texte(x, y, text, 550)
                    else:
                        certificat.ajouter_texte(x, y, text)
                else:
                    print("Erreur lors de la lecture du fichier JSON.")
            print("Fichier PDF généré avec succès.")
            if os.path.exists(f"certif_test.pdf"):
                os.remove("certif_test.pdf")
            certificat.sauvegrader_pdf("certif_test.pdf")

        else:
            print(f"Erreur lors du chargement ou de l'analyse du fichier JSON. {contenu_json}")
    else:
        print("Aucun fichier trouvé dans le répertoire 'JSON'.")



