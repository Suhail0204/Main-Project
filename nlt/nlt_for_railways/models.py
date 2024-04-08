from django.db import models
from db_connection import db

# Create your models here.

users_collection = db['Users']

def get_language_code(language_name):
    language_map = {
        'arabic': 'ar_AR',
        'czech': 'cs_CZ',
        'german': 'de_DE',
        'english': 'en_XX',
        'spanish': 'es_XX',
        'estonian': 'et_EE',
        'finnish': 'fi_FI',
        'french': 'fr_XX',
        'gujarati': 'gu_IN',
        'hindi': 'hi_IN',
        'italian': 'it_IT',
        'japanese': 'ja_XX',
        'kazakh': 'kk_KZ',
        'korean': 'ko_KR',
        'lithuanian': 'lt_LT',
        'latvian': 'lv_LV',
        'burmese': 'my_MM',
        'nepali': 'ne_NP',
        'dutch': 'nl_XX',
        'romanian': 'ro_RO',
        'russian': 'ru_RU',
        'sinhala': 'si_LK',
        'turkish': 'tr_TR',
        'vietnamese': 'vi_VN',
        'chinese': 'zh_CN',
        'afrikaans': 'af_ZA',
        'azerbaijani': 'az_AZ',
        'bengali': 'bn_IN',
        'persian': 'fa_IR',
        'hebrew': 'he_IL',
        'croatian': 'hr_HR',
        'indonesian': 'id_ID',
        'georgian': 'ka_GE',
        'khmer': 'km_KH',
        'macedonian': 'mk_MK',
        'malayalam': 'ml_IN',
        'mongolian': 'mn_MN',
        'marathi': 'mr_IN',
        'polish': 'pl_PL',
        'pashto': 'ps_AF',
        'portuguese': 'pt_XX',
        'swedish': 'sv_SE',
        'swahili': 'sw_KE',
        'tamil': 'ta_IN',
        'telugu': 'te_IN',
        'thai': 'th_TH',
        'tagalog': 'tl_XX',
        'ukrainian': 'uk_UA',
        'urdu': 'ur_PK',
        'xhosa': 'xh_ZA',
        'galician': 'gl_ES',
        'slovene': 'sl_SI'
    }
    
    return language_map.get(language_name.lower(), 'Unknown')

# Example usage:
language_name = 'French'
language_code = get_language_code(language_name)
print(f"The language code for {language_name} is {language_code}")

