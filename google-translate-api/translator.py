 
# Install googletrans API in Command Prompt
# pip install googletrans==3.1.0a0

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

