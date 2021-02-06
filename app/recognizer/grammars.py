from yargy import (
    rule,
    and_, or_, not_,
    Parser,
)
from yargy.interpretation import fact
from yargy.predicates import (
    gram,
    is_capitalized,
    eq,
)
from yargy.predicates.bank import DictionaryPredicate as dictionary
from yargy.tokenizer import MorphTokenizer

from recognizer.dictionary import load_dict

DASH = eq('-')
TITLE = is_capitalized()

Name = fact(
    'Name',
    ['first', 'last', 'middle'],
)


class Name(Name):
    @property
    def obj(self):
        from natasha import obj
        return obj.Name(self.first, self.last, self.middle)


FIRST_DICT = set(load_dict('first.txt'))
LAST_DICT = set(load_dict('last.txt'))


IN_FIRST = dictionary(FIRST_DICT)
IN_LAST = dictionary(LAST_DICT)


LAST_OC = gram('Surn')
MIDDLE_OC = gram('Patr')
ABBR_OC = gram('Abbr')


# FIRST
FIRST_EASY = and_(
    IN_FIRST,
    TITLE,
    not_(ABBR_OC),
)

FIRST_HARD = rule(
      FIRST_EASY,
      DASH,
      FIRST_EASY,
)

FIRST = or_(
    rule(FIRST_EASY),
    FIRST_HARD,
).interpretation(
    Name.first
)


# LAST

LAST = and_(
    or_(
        IN_LAST,
        LAST_OC,
    ),
    TITLE,
    not_(ABBR_OC),
).interpretation(
    Name.last
)


#MIDDLE

MIDDLE = and_(
    MIDDLE_OC,
    TITLE,
).interpretation(
    Name.middle
)


LAST_FIRST_MIDDLE = rule(
    LAST,
    FIRST,
    MIDDLE,
)

FIRST_MIDDLE_LAST = rule(
    FIRST,
    MIDDLE,
    LAST,
)

FIRST_LAST = rule(
    FIRST,
    LAST,
)

LAST_FIRST = rule(
    LAST,
    FIRST,
)

FIRST_MIDDLE = rule(
    FIRST,
    MIDDLE,
)


NAME_PARSER = or_(
    LAST_FIRST_MIDDLE,
    FIRST_MIDDLE_LAST,

    FIRST_MIDDLE,

    LAST_FIRST,
    FIRST_LAST,

    FIRST,
    LAST,
).interpretation(
    Name
)


tokenizer = MorphTokenizer()
name_parser = Parser(NAME_PARSER, tokenizer=tokenizer)



