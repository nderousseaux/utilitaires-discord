Bienvenue sur le WIKI du projet **utilitaires_discord_server**

Pour l'instant, une interface web n'est pas prévue, donc tout sera référencé ici, dans ce répo.

# Objectifs du projet

Le projet servira à updater de manière aléatoire le titre d'un groupe discord. Le titre sera choisi aléatoirement, et ça se fera à intervalles aléatoire, entre deux bornes, minimale et maximale.

# Variables d'environnement

## Variables de Login
- UTDI_LOGIN : Le login de l'utilisateur
- UTDI_PASSWORD : Le mot de passe de l'utilisateur

ou
- UTDI_TOKEN : Le token d'identification

## Variables sur l'api discord
- UTDI_ID_GROUP : Le groupe à modifier
- UTDI_API_DISCORD_BASE_URL : L'adresse de l'api discord

## Variables sur le temps
- UTDI_UPDATE_TIMEOUT : L'intervale entre chaque update (en secondes)

ou
- UTDI_UPDATE_TIMEOUT_MIN : L'intervale minimal entre chaque update (en secondes)
- UTDI_UPDATE_TIMEOUT_MAX : L'intervale maximal entre chaque update (en secondes)

