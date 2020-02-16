import logging

from flashtext import KeywordProcessor


log = logging.getLogger(f"pizza_nlp.{__name__}")


class Tokenizer(object):
    def __init__(self):
        log.info("Tokenizer initialization")

        from .lookup_dic import _PhraseDictionary as __PD
        log.debug("Tokenizer: calls lookup_dic.read_phrases")
        self.lookup_dic = __PD()

        log.debug("Instanciate flashtext.KeyworkProcessor")
        self.__keyword_processor = KeywordProcessor()
        log.debug("Insert data into flashtext.KeyworkProcessor instance.")
        self.__keyword_processor.add_keywords_from_dict(
                self.lookup_dic.lookup_dic_CODE)
        log.info("Tokenizer initialization successful")


    def tokenize(self, text):
        log.debug(f"Tokenizer called on {text}")

        log.debug("Phase I: Replacing phrases.")
        text = self.__keyword_processor.replace_keywords(text)

        log.debug("Phase II: Split by space.")
        tokens_list = text.split()

        log.debug("Phase III: Replace back token id to its original form.")
        tokens_list = [
            self.lookup_dic.reverse_replace(token)
            if token in self.lookup_dic.lookup_dic_CODE else token
            for token in tokens_list
        ]

        return tokens_list

    def __call__(self, text):
        return self.tokenize(text)
