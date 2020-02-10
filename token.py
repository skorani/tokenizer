import KeywordProcessor
import lookup_dic


def init():
    global __keyword_processor
    global __reverse_lookup_dict
    global lookup_dic_CODE

    lookup_dic.init()
    __keyword_processor = KeywordProcessor()
    __keyword_processor.add_keywords_from_dict(lookup_dic.lookup_dic_CODE)

    #__reverse_lookup_dict = lookup_dic.create_reverse_dic_code()
    lookup_dic.release()

def tokenize(text):
    global __keyword_processor
    global __reverse_lookup_dict
    #print(text)
    text = __keyword_processor.replace_keywords(text)
    #print(text)
    #print('###')

    tokens_list = text.split()

    tokens_list = [lookup_dic.lookup_dic_CODE[token] if token in lookup_dic.lookup_dic_CODE.keys() else token for token in tokens_list]

    return tokens_list
