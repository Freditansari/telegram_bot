import requests
def send(bot_message):

    bot_chatID = '559737247'

    send_text = 'https://api.telegram.org/bot1270470028:AAGitNmo6dBYzfatJ2bokXHCfL_AuMFfiiY'+'/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    # resp = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(token), params)

    response = requests.get(send_text)
    return response.json()