import requests
import subprocess
import json
import time

def send_alert(alert_text):
    webhook_url = '' #add a mattermost webhook url
    data = {
        "icon_url": "https://web.archive.org/web/20090829012411if_/http://geocities.com/odriscolll/spacedog.gif",
        "username": "Alert Dog",
        "text": alert_text
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    print(response.text)

def test_url(url):
    response = requests.head(url, allow_redirects=True)
    http_status = response.status_code
    print(http_status)
    return http_status

def test_urls(urls, success_rate_controller, url_status_controller):
    alert_text=""
    for url in urls:
        current_url_alert_text=""
        http_status=0 #0 is the status given in case of failed curl
        try:
            http_status = test_url(url)
            if http_status!=200:
                print(f"URL {url} not working. Waiting 2 minutes before retry.")
                time.sleep(30*4)
                http_status = test_url(url)
            if http_status==200:
                success_rate_controller.add_success()
                current_url_alert_text=":thumbsup: The following site is back online: {}\n\n".format(url)
            else:
                current_url_alert_text=":rotating_light: :exclamation: URL: {} has the status of {}\n\n".format(url, http_status)
                success_rate_controller.add_error()
        except requests.exceptions.ConnectionError as e:
            current_url_alert_text=":rotating_light: :exclamation: URL: {} Error: {}\n\n".format(url, e)
            success_rate_controller.add_error()
        status_has_changed=url_status_controller.set_current_status_for_url(url,http_status)
        if status_has_changed and current_url_alert_text:
            alert_text+=current_url_alert_text
    if alert_text:
        send_alert(alert_text)
