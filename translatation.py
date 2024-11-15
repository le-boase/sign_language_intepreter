from vulavula import VulavulaClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file if present
load_dotenv()

# Fetch the API key from environment variables with a fallback placeholder
VULAVULA_API_KEY = os.getenv("VULAVULA_API_KEY", "default_vulavula_key")

def convert_lang_code(lang_code):
  lang_mapping = {
    "nso_Latn": "sepedi",
    "afr_Latn": "afrikaans",
    "sot_Latn": "sesotho",
    "ssw_Latn": "siswati",
    "tso_Latn": "xitsonga",
    "tsn_Latn": "setswana",
    "xho_Latn": "isixhosa",
    "zul_Latn": "isizulu",
    "eng_Latn": "english",
    "swh_Latn": "swahili"
  }
  return lang_mapping.get(lang_code, lang_code)

def translate_from_box(input_text, target_lang_code):  

    client = VulavulaClient(VULAVULA_API_KEY)

    # Define the translation data
    translation_data = {
    "input_text": input_text , 
    "source_lang": ("eng_Latn"),
    "target_lang": target_lang_code
    }

    source_lang = convert_lang_code(translation_data['source_lang'])
    target_lang = convert_lang_code(translation_data['target_lang'])

    translation_result = client.translate(translation_data)
    spoken_text = translation_result['translation'][0]['translated_text']

    return spoken_text





