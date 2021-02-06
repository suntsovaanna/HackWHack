import re
import pymorphy2
from typing import Dict
from transliterate import translit
from spellchecker import SpellChecker
morph = pymorphy2.MorphAnalyzer()
spell = SpellChecker(language=None, case_sensitive=False)
spell.word_frequency.load_text_file('../data/first.txt')
spell.word_frequency.load_text_file('../data/last.txt')


class NameRecognizer(object):
    def __init__(self, name_parser):
        self.parser = name_parser

    def __call__(self, text) -> Dict:
        text = str(text)
        text = translit(text, "ru")
        text_cleaned, text_deleted = self.clear_data(text)
        text_cleaned = ' '.join([correct(text_cl) for text_cl in text_cleaned.split()])

        model = {}
        _text = list(text_cleaned)
        for name in self.parser.findall(text_cleaned):
            name = name.fact
            for span in reversed(name.spans):
                del _text[span.start:span.stop]
            is_all_recognized = not (bool(''.join(_text).strip()) or text_deleted)
            return {
                'last': name.last,
                'first': name.first,
                'middle': name.middle,
                'is_all_recognized': is_all_recognized,
            }

        return model

    def clear_data(self, text):
        test_deleted = []
        searches = re.findall('\([^()]*\)', text)
        start = 0
        for search in searches:
            start_index = text.index(search, start)
            start = start_index + len(search)
            test_deleted.append(
                {
                    'start': start_index,
                    'end': start_index + len(search) - 1,
                }
            )

        for search in searches:
            text = text.replace(search, '', 1)

        return text, test_deleted


def correct(part: str):
    if is_name(part):
        return part

    if part in spell:
        return part
    else:
        return correction(part)


def correction(name):
    is_lower = name.islower()
    result = spell.correction(name)
    return result if is_lower else result.capitalize()

QWE = ['Patr', 'Surn', 'Name']


def is_name(word):
    flag = False
    for p in morph.parse(word):
        for q in QWE:
            if q in list(p.tag.grammemes):
                flag = True

    return flag


