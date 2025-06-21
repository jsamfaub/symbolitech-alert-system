# Symbolitech | Système d'alertes Mattermost

### Description:
Ce script permet d'être notifié sur une chaîne Mattermost chaque fois qu'un site web tombe en panne ou est de nouveau opérationnel.

Le script effectu une vérification puis notifie l'état du site dans Mattermost.

Si la réponse n'est pas 200, il refait la vérification après un délai de 2 minutes avant de notifier dans Mattermost.

L'utilisateur Mattermost s'appelle Alerte Fido et utilise [cet avatar](https://web.archive.org/web/20090829012411if_/http://geocities.com/odriscolll/spacedog.gif).

### Exemple de cron job:
```*/5 * * * * python3 /path/to/script/main.py > /path/to/script/logs```

### Usage:
- Ajouter une liste de urls dans main.py
- Ajouter un webhook mattermost dans functions.py
