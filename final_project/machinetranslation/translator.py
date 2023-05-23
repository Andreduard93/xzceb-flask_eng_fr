import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('z-UAXhZ60fna-VsvCyC9tQXZYpUD9tH8OonV1Pl1oiaK')
language_translator = LanguageTranslatorV3(
    version='2023-05-16',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c9125650-f643-4a59-b46d-eb219462a65f')

def english_to_french(english_text):

    """This function translate english to french"""
    frenchtranslation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return frenchtranslation.get('translations')[0].get('translation')

def french_to_english(french_text):

    """This function translate french to english"""

    englishtranslation=language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    return englishtranslation.get('translations')[0].get('translation')
