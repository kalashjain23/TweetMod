import requests
import config.config as config

def text_mod(tweet):
    data = {
        'text': f'{tweet}',
        'mode': 'standard',
        'lang': 'en',
        'opt_countries': 'us,gb,fr',
        'api_user': config.api_user,
        'api_secret': config.api_secret
    }
    response = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)

    json_data = response.json()
    list = json_data['profanity']['matches']
    if (len(list)!=0):
        type = list[0]['type']
        return ('It contains '+type+' words.')
    else:
        return tweet
