#!/usr/bin/env python
#-*- encoding: utf-8 -*-


import lookup_dic as lk
import token as tok

counter = {}
clean_text = []
# read the text in list clean_text


def main():
    lk.create_dic_code()
    tok.init()
    for text in clean_text:
        tokens = tok.tokenize(text)
        for token in tokens:
            if type(token) == list:
                token = token[0]
            if token in counter:
                counter[token] += 1
            else:
                counter[token] = 1
            # print(counter)
            newCounter = {}
            for token, count in counter.items():
                # print(token)
                test = lk.reverse_replace(format(token))
                # print(test)


if __name__ == "__main__":
    main()
