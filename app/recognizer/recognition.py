import re
from typing import Dict


class NameRecognizer(object):
    def __init__(self, name_parser):
        self.parser = name_parser

    def __call__(self, text) -> Dict:
        text_cleaned, text_deleted = self.clear_data(text)
        model = {}
        _text = list(text_cleaned)
        for name in self.parser.findall(text_cleaned):
            name = name.fact
            for span in reversed(name.spans):
                del _text[span.start:span.stop]
            is_all_recognized = not (bool(''.join(_text).strip()) and text_deleted)
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





