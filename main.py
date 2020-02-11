#!/usr/bin/env python
#-*- encoding: utf-8 -*-


from tokenizer import _tokenizer as tok
from tokenizer import lookup_dic as lk 

counter = {}

def main():
    clean_text = [input()]
    tok.init()
    lk.create_dic_code()
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
