import re
from typing import Dict


class NameRecognizer(object):
    def __init__(self, name_parser):
        self.parser = name_parser

    def __call__(self, text) -> Dict:
        text = self.clear_data(text)
        model = {}
        for name in self.parser.findall(text):
            name = name.fact
            return {
                'last': name.last,
                'first': name.first,
                'middle': name.middle,
            }

        return model

    def clear_data(self, text):
        return re.sub(r'\(.+?\)\s', '', text)
