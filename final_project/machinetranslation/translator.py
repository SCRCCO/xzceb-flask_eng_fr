'''Description of your file.'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)
def english_to_french(english_text):
    """Funzione che traduce da inglese a francese"""
    translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result() # this is fine.
    french_text = translation['translations'][0]['translation']

    print(french_text)
    return french_text
def french_to_english(french_text):
    """Funzione che traduce da francese a inglese"""
    translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result() # this is fine.
    english_text = translation['translations'][0]['translation']
    print(english_text)
    return english_text
