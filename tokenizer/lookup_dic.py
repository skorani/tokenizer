import csv


reveresd_array = []
lookup_reverse_dic_CODE = {}
lookup_dic_CODE = {}


def read_phrases(phrase_file="data/phrases.csv"):
    global lookup_reverse_dic_CODE
    global lookup_dic_CODE
    with open(phrase_file) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                phrase, replace_with = row
            except ValueError:
                pass
            lookup_dic_CODE.update({replace_with: [phrase]})
            lookup_reverse_dic_CODE.update({phrase: [replace_with]})


def reverse_replace(_token_):
    global lookup_dic_CODE
    for item in lookup_dic_CODE.items():
        _token_ = str.replace(_token_, item[0], item[1][0])

    return _token_
