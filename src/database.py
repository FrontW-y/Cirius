import mysql.connector as sq
import datetime
from generer_certificat import create_certif
from Medecin import Medecin


class Database:
    def __init__(self):
        self.conn = sq.connect(host="localhost",user="root",password="",database="currerius")
        self.cursor = self.conn.cursor()
    def register_user(self, id_user, nom, prenom, date_naissance, adresse, ville, departement_numero, code_postal):
        try:
            Medecin(ville_patient=ville, dep_patient=departement_numero)
            date_naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y").strftime("%Y-%m-%d")
            self.cursor.execute("INSERT INTO utilisateurs (idDiscord, nom, prenom, dateDeNaissance, adresse, ville, numDep, codePostal,credit, freeCredit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 0,2)",
                            (id_user, nom, prenom, date_naissance, adresse, ville, departement_numero, code_postal))
            self.conn.commit()
            return True
        except sq.Error as e:
            print(e.errno)
            return e.errno
        
    def is_registered(self, id_user):
        self.cursor.execute("SELECT COUNT(*) FROM utilisateurs WHERE idDiscord = %s", (id_user,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            return True
        else:
            return False
       
    
    def get_balance(self, id_user):
        try :
            if self.is_registered(id_user) == False:
                return "Vous n'êtes pas enregistré"
            self.cursor.execute("SELECT credit FROM utilisateurs WHERE idDiscord = %s",(id_user,))
            solde =  self.cursor.fetchone()[0]
            return f"Votre solde est de {solde} crédit(s)"
            
        except sq.Error as e:
            print(e)
            return e.errno
        
    
    def generate_certificate(self, id_user, motif, date_absence, nombre_jour_absence):
        try:
            if self.is_registered(id_user) == False:
                return "Vous n'êtes pas enregistré"
            self.cursor.execute("SELECT freeCredit FROM utilisateurs WHERE idDiscord = %s",(id_user,))
            solde =  self.cursor.fetchone()[0]
            if solde < 0.5:
                self.cursor.execute("SELECT credit FROM utilisateurs WHERE idDiscord = %s",(id_user,))
                solde =  self.cursor.fetchone()[0]
                if solde < 0.5:
                    return "Vous n'avez pas assez de crédits"
                else :
                    self.cursor.execute("UPDATE utilisateurs SET credit = credit - 0.5 WHERE idDiscord = %s",(id_user,))
                    self.conn.commit()
            else :
                self.cursor.execute("UPDATE utilisateurs SET freeCredit = freeCredit - 0.5 WHERE idDiscord = %s",(id_user,))
                self.conn.commit()
            
            self.cursor.execute("SELECT nom, prenom, dateDeNaissance, adresse, codePostal, ville FROM utilisateurs WHERE idDiscord = %s",(id_user,))
            user = self.cursor.fetchone()
            nom = user[0]
            prenom = user[1]
            date_naissance = user[2].strftime("%d/%m/%Y")
            adresse = user[3]
            code_postal = user[4]
            ville = user[5]
            create_certif(prenom, nom, "M", date_naissance, date_absence, nombre_jour_absence, code_postal, adresse, remote=True)
            
            
            return True
        except sq.Error as e:
            print(e)
            return e.errno
    
    
