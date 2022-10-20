from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from pandas import json_normalize

load_dotenv()

APIKEY = 'YOUR apikey'
URL = 'Your URL'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))


def english_to_french(englishtext):
    if englishtext == '':
        return 'Empty'
    translation_new = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    french_text = translation_new['translations'][0]['translation']
    return french_text


def french_to_english(frenchtext):
    if frenchtext == '':
        return 'Empty'
    translation_new = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    english_text = translation_new['translations'][0]['translation']
    return english_text


print(english_to_french('this project is for translate from English to French and from French to English'))
print(french_to_english('Je suis du Pakistan'))
