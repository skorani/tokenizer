import logging

from flashtext import KeywordProcessor

from . import lookup_dic

log = logging.getLogger(f"pizza_nlp.{__name__}")


def init():
    log.info("Tokenizer initialization")
    global __keyword_processor
    global __reverse_lookup_dict
    global lookup_dic_CODE

    log.debug("Tokenizer: calls lookup_dic.read_phrases")
    lookup_dic.read_phrases()

    log.debug("Instanciate flashtext.KeyworkProcessor")
    __keyword_processor = KeywordProcessor()
    log.debug("Insert data into flashtext.KeyworkProcessor instance.")
    __keyword_processor.add_keywords_from_dict(lookup_dic.lookup_dic_CODE)
    log.info("Tokenizer initialization successful")


def tokenize(text):
    log.debug(f"Tokenizer called on {text}")
    global __keyword_processor
    global __reverse_lookup_dict

    log.debug("Phase I: Replacing phrases.")
    text = __keyword_processor.replace_keywords(text)

    log.debug("Phase II: Split by space.")
    tokens_list = text.split()

    log.debug("Phase III: Replace back token id to its original form.")
    tokens_list = [
        lookup_dic.reverse_replace(token)
        if token in lookup_dic.lookup_dic_CODE else token
        for token in tokens_list
    ]

    return tokens_list
