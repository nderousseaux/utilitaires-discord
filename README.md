# Utilitaires Discord - Serveur

## Lancer l'application

- Créer et remplir le fichier `.env`. (.env.dev ou .env.production)

- Lancer l'application :
```shell
#Développement
$ docker-compose --build up

#Debug
$ docker-compose --build -f docker-compose.yml -f docker-compose.debug.yml up

#Linter server
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --rm server pylint src/

#Production
$ docker-compose --build -f docker-compose.yml -f docker-compose.production.yml up
```

## Documentation 
On retrouvera la documentation du projet juste [ici](https://gitlab.com/projets-diy/utilitaires-discord/utilitaires-discord/-/wikis/home)

