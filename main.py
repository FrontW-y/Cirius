import discord
from discord.ext import commands
from Ressources.TOKEN.config import TOKEN
from src.database import Database

db = Database()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)


async def on_message(self, message):
    print(f"Message from {message.author}: {message.content}")


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hey {interaction.user.id} !")


@bot.tree.command(name="register", description="S'enregistrer")
async def register(interaction: discord.Interaction, nom: str, prénom: str, date_naissance: str, adresse: str,
                   ville: str, department_numéro: int, code_postal: int):
    id_user = interaction.user.id
    reponse = db.register_user(id_user=id_user, nom=nom, prenom=prénom, date_naissance=date_naissance, adresse=adresse,
                               ville=ville, departement_numero=department_numéro, code_postal=code_postal)
    if reponse == True:
        await interaction.response.send_message(f"@{interaction.user.name} vous êtes bien enregistré")
    elif reponse == 1062:
        await interaction.response.send_message(f"Erreur, l'utilisateur @{interaction.user.name} est déjà enregistré")
    else:
        await interaction.response.send_message(f"Erreur {reponse} lors de l'enregistrement")


@bot.tree.command(name="balance", description="Voir son solde")
async def balance(interaction: discord.Interaction):
    id_user = interaction.user.id
    msg = db.get_balance(id_user=id_user)
    await interaction.response.send_message(msg, ephemeral=True)
    
@bot.tree.command(name="Generer", description="Générer un certificat")
async def generer(interaction: discord.Interaction, motif: str, date_absence: str, nombre_jour_absence: int):
    id_user = interaction.user.id
    reponse = db.generate_certificate(id_user=id_user, motif=motif, date_absence=date_absence, nombre_jour_absence=nombre_jour_absence)
    if reponse == True:
        await interaction.response.send_message(f"@{interaction.user.name} votre certificat a bien été généré")
    else:
        await interaction.response.send_message(f"Erreur {reponse} lors de la génération du certificat")



bot.run(TOKEN)
