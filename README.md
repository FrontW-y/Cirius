
# Cirius

FR: Cirius est un bot Python ainsi qu'un générateur de certificat médical écrit en Python, basé sur différents modèles reproduits en JSON. Cette différence avec [CertifSharp](https://github.com/FrontW-y/certifSharp) lui offre une modularité et une flexibilité supérieures ainsi qu'une meilleure structure.

EN: Cirius is a Python bot as well as a medical certificate generator written in Python, based on various models reproduced in JSON. This difference with [CertifSharp](https://github.com/FrontW-y/certifSharp) provides it with superior modularity and flexibility, as well as a better structure.


## Bon à savoir/ Good to know

FR : 

- La base de données ainsi que le fichier contenant l'entièreté des médecins ont été supprimés ainsi que le token du bot pour des raisons de sécurité.

EN :

- The database as well as the file containing all the doctors' information have been deleted, along with the bot token, for security reasons.
 

## Documentation

FR :

Structure du Code :

- Le code est organisé dans la section "source" et est divisé en trois classes principales :

  - Classe Médecin :
    Cette classe permet de créer et de gérer les informations d'un praticien en se basant sur des caractéristiques officielles telles que le numéro de téléphone, le nom et l'adresse.

  - Classe PDFClasse :
    La classe PDFClasse est responsable de la création de fichiers PDF au format A4. Elle offre la possibilité d'ajouter divers attributs tels que des images, du texte, de définir la police, et de contrôler si le texte est souligné ou non.

  - Classe Database :
    La classe Database facilite la connexion à une base de données sur le réseau local et permet d'effectuer des requêtes SQL.

- La partie bot est contenue dans le fichier main.py. Son rôle est de lancer l'application et de gérer les commandes slash nécessaires à la génération des certificats médicaux.

EN : 

Code Structure:

- The code is organized in the "source" section and is divided into three main classes:

  - Doctor Class:
    This class allows for the creation and management of practitioner information based on official characteristics such as phone number, name, and address.

  - PDFClass:
    The PDFClass is responsible for creating PDF files in A4 format. It provides the ability to add various attributes such as images, text, define the font, and control whether the text is underlined or not.

  - Database Class:
    The Database class facilitates connection to a database on the local network and allows for SQL queries.

- The bot part is contained in the main.py file. Its role is to launch the application and handle the slash commands necessary for generating medical certificates.



    


## Installation



 - Windows

```bash
  pip install -r ./requirement.txt
```

 - Linux

```bash
  pip3 install -r ./requirement.txt
```

Modifiez le jeton du bot par le vôtre dans Ressources/TOKEN/config.py et installez votre base de données (non fournie). Ensuite lancez main.py

Change bot token by yours in `Ressources/TOKEN/config.py` and install your database (not provided). Then start main.py
    
## Auteur / Author

- [@FrontW-y](https://github.com/FrontW-y)



## Avertissement  / Disclaimer 

- Avis de non-responsabilité :

Ce projet est fourni uniquement à des fins éducatives. Toute utilisation des matériaux et du code fournis dans ce dépôt est à vos propres risques. L'auteur(e) de ce projet ne peut être tenu(e) responsable de tout abus, dommage ou conséquence découlant de l'utilisation de ce projet. Il vous incombe d'utiliser les informations et le code de manière responsable et conformément aux lois et réglementations applicables.

- Disclaimer:

This project is provided for educational purposes only. Any use of the materials and code provided in this repository is at your own risk. The author(s) of this project cannot be held responsible for any misuse, damage, or consequences arising from the use of this project. It is your responsibility to use the information and code responsibly and in accordance with applicable laws and regulations.
