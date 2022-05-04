"""
Translation Module
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
APIKEY_LT = os.environ['apikey']
URL_LT = os.environ['url']
VERSION_LT = '2018-05-01'
AUTHENTICATOR = IAMAuthenticator(APIKEY_LT)
LT = LanguageTranslatorV3(version=VERSION_LT, authenticator=AUTHENTICATOR)
LT.set_service_url(URL_LT)


def english_to_french(textinput: str):
    """
    :return: Translates English To French
    """
    frenchtext = \
        LT.translate(str(textinput), model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchtext
    # LT.translate returns a dictionary containing the translation and other infos
    # You can check translatable languages with:
    # LT.list_identifiable_languages().get_result() and get the model id you need
    # model_id= specifies from what language translation must be done to what language ;)


def french_to_english(textinput: str):
    """
    :return: Translates French To English
    """
    englishtext = \
        LT.translate(str(textinput), model_id='fr-en').get_result()['translations'][0]['translation']
    return englishtext
