import logging as __logging

from ._tokenizer import init, tokenize

__logging.getLogger(f"pizza_nlp.{__name__}").addHandler(__logging.NullHandler())
