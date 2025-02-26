import json
import ssl
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
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """function to convert Eng to French"""
    if english_text=="":
        french_text = "Nullinput"
    else:
        conv = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()
        french_text = (conv["translations"][0]["translation"])
    
    return french_text

def french_to_english(french_text):
    """function to convert French to English"""
    if french_text=="":
        english_text = "Nullinput"
    else:
        conv = language_translator.translate(
        text = french_text,
        model_id = 'fr-en').get_result()
        english_text = (conv["translations"][0]["translation"])
        print(english_text)

    return english_text

