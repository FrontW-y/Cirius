import csv
import random


class Medecin:
    """Classe permettant de créer un objet Medecin et de récupérer les informations d'un médecin"""
    def __init__(self, filepath="./Ressources/CSV/medecins.csv", remote=True, ville_patient=None, dep_patient=None):
        self.filepath = filepath
        self.remote = remote
        self.ville_patient = ville_patient
        self.dep_patient = dep_patient
        self.medecin = self._select_medecin()
        self._set_attributes()

    def _select_medecin(self):
        medecins = []
        with open(self.filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader: 
                if self.remote:
                    medecins.append(row)
                elif row['Commune'] == self.ville_patient or row['Code Officiel Département'] == self.dep_patient:
                    medecins.append(row)

            if medecins:
                return random.choice(medecins)
            else:
                return None

    def _set_attributes(self):
        if self.medecin:
            self.numero_medecin = self.medecin['Numéro de téléphone']
            self.nom_medecin = self.medecin['Nom du professionnel']
            self.adresse_medecin = self.medecin['Adresse']
            self.ville_medecin = self.medecin['Commune']
            self.code_postal_medecin = self.medecin['Code Officiel Département']
            self.finess = self.medecin['Code Officiel EPCI']
            self.nom_centre = self.medecin['Nom Officiel EPCI']
        else:
            self.numero_medecin = None
            self.nom_medecin = None
            self.adresse_medecin = None
            self.finess = None
            self.nom_centre = None
            self.ville_medecin = None
            self.code_postal_medecin = None
