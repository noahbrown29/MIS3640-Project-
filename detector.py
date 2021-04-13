# Install googletrans API in Command Prompt
# pip install googletrans==3.1.0a0

import googletrans
from googletrans import Translator

translator = Translator()
translator.detect('이 문장은 한글로 쓰여졌습니다.')
# <Detected lang=ko confidence=0.27041003>
translator.detect('この文章は日本語で書かれました。')
# <Detected lang=ja confidence=0.64889508>
translator.detect('This sentence is written in English.')
# <Detected lang=en confidence=0.22348526>
translator.detect('Tiu frazo estas skribita en Esperanto.')
# <Detected lang=eo confidence=0.10538048>

langs = translator.detect(['한국어', '日本語', 'English', 'le français'])
for lang in langs:
    print(lang.lang, lang.confidence)
# ko 1
# ja 0.92929292
# en 0.96954316
# fr 0.043500196

