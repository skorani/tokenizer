from flashtext import KeywordProcessor

from . import lookup_dic


def init():
    global __keyword_processor
    global __reverse_lookup_dict
    global lookup_dic_CODE
    global pattern

    lookup_dic.read_phrases()
    __keyword_processor = KeywordProcessor()
    __keyword_processor.add_keywords_from_dict(lookup_dic.lookup_dic_CODE)

#    __reverse_lookup_dict = lookup_dic.create_reverse_dic_code()


def tokenize(text):
    global __keyword_processor
    global __reverse_lookup_dict
    global pattern
    text = __keyword_processor.replace_keywords(text)

    tokens_list = text.split()

    tokens_list = [
        lookup_dic.reverse_replace(token)
        if token in lookup_dic.lookup_dic_CODE else token
        for token in tokens_list
    ]

    return tokens_list
