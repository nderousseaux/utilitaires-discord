# Utilitaires Discord - Serveur

## Lancer l'application

- Créer et remplir le fichier `.env`. (.env.dev ou .env.production)

- Lancer l'application :
```shell
#Développement
$ docker-compose up --build

#Debug
$ docker-compose -f docker-compose.yml -f docker-compose.debug.yml up --build

#Linter server
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --rm server pylint src/

#Production
$ docker-compose -f docker-compose.yml -f docker-compose.production.yml up --build
```

## Documentation 
On retrouvera la documentation du projet juste [ici](https://gitlab.com/projets-diy/utilitaires-discord/utilitaires-discord/-/wikis/home)

