#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

from collections import Counter

from tokenizer import Tokenizer

logging.basicConfig()


def main():
    clean_text = [input()]
    tok = Tokenizer()
    for text in clean_text:
        tokens = tok(text)
        print(tokens)
        counts = Counter(tokens)
        for token, count in counts.items():
            print(f"{token}: {count}")


if __name__ == "__main__":
    main()
