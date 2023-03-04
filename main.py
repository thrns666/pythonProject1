import requests
import time
token = '2Qh1qZ0k6EEud350aVAXDUT2CCPGM4oQ'
url = 'https://api.telegram.org/bot' + token
#print(url)
#print(response.content)
#a = 'https://api.telegram.org/bot5381519309:AAHwRLwvXHk_UIVPJjcq07ksLs_S3XtXTZg'
#response = requests.get(url + '/getUpdates')

counter: int = 0
max_counter: int = 100
offset: int = -2
chat_id: int
timeout: int = 50


while counter < max_counter:
    print(counter)
    updates = requests.get(url + '/getUpdates?offset=' + f'{offset + 1}').json()
#if updates[result]:
    for res in updates['result']:
        chat_id = res['message']['from']['id']
        offset = res['update_id']
        requests.get(f'{url}/sendMessage?chat_id={chat_id}&text=wakey')

    counter += 1
    time.sleep(1)

