#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import lookup_dic as lk
import token as tok


def main():
    lk.read_phrases()
    tok.init()
    clean_text = [input()]
    counter = {}
    for text in clean_text:
        tokens = tok.tokenize(text)
        print(tokens)
        for token in tokens:
            if type(token) == list:
                token = token[0]
            if token in counter:
                counter[token] += 1
            else:
                counter[token] = 1
            for token, count in counter.items():
                print(token, count)


if __name__ == "__main__":
    main()
