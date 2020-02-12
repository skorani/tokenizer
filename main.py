#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter

from tokenizer import _tokenizer as tok

counter = {}
clean_text = []


def main():
    clean_text = [input()]
    tok.init()
    for text in clean_text:
        tokens = tok.tokenize(text)
        print(tokens)
        counts = Counter(tokens)
        for token, count in counts.items():
            print(f"{token}: {count}")


if __name__ == "__main__":
    main()
