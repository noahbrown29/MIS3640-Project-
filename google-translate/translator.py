# WHAT WE NEED TO CHANGE TO MAKE THIS WORK FOR US:
# 1. The user needs to be able to input any word or phrase AND select the language they want the program to translate it to

"""
Install googletrans API in Command Prompt
pip install googletrans==3.1.0a0
"""

import googletrans
from googletrans import Translator

translator = Translator()
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='mi')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개

# print(googletrans.LANGUAGES)

