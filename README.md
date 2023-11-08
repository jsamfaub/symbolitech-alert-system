# systeme-alertes-symbolitech

### Description:
This script allows you to be notified in a mattermost channel whenever one of your websites goes down or back up.

There is a built-in function that makes sure a site is really down when the response is not 200 (or redirect) by checking once and then waiting 2 minutes before checking again.

The mattermost user is called Alert Dog and uses [this avatar](https://web.archive.org/web/20090829012411if_/http://geocities.com/odriscolll/spacedog.gif). You can easily change the name and avatar in the code.

### Recommended cron job:
```*/5 * * * * python3 /path/to/script/main.py > /path/to/script/logs```

### To use the script:
- Add a list of urls in main.py
- Add a mattermost webhook in functions.py
