import csv
import logging


reveresd_array = []
lookup_reverse_dic_CODE = {}
lookup_dic_CODE = {}

log = logging.getLogger(f"pizza_nlp.{__name__}")


def read_phrases(phrase_file="data/phrases.csv"):
    log.debug("Populating phrase dictionary: started")
    global lookup_reverse_dic_CODE
    global lookup_dic_CODE
    log.debug("Reading phrase datafile: started")
    log.info("Reading phrase datafile: {}".format(phrase_file))
    with open(phrase_file) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                phrase, replace_with = row
                log.debug(f"  phrase: {phrase}, rw: {replace_with}")
            except ValueError:
                log.error("Bad input: {} - csv parser could not unpack properly.".format(repr(row)))
            lookup_dic_CODE.update({replace_with: [phrase]})
            lookup_reverse_dic_CODE.update({phrase: [replace_with]})
            log.debug(f"Phrase: {phrase} with id {replace_with} added to phrase dictionary.")
    log.debug("Populating phrase dictionary: finished")


def reverse_replace(_token_):
    log.debug(f'Reverse lookup call for "{_token_}".')
    global lookup_dic_CODE
    for item in lookup_dic_CODE.items():
        _token_ = str.replace(_token_, item[0], item[1][0])
    log.debug(f'Found "{_token_}".')

    return _token_
