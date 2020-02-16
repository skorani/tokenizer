import csv
import logging


log = logging.getLogger(f"pizza_nlp.{__name__}")


class _PhraseDictionary(object):
    def __init__(self, phrase_file="data/phrases.csv"):
        self._phrase_file = phrase_file
        log.debug("Populating phrase dictionary: started")
        self.lookup_reverse_dic_CODE = dict()
        self.lookup_dic_CODE = dict()
        log.debug("Reading phrase datafile: started")
        log.info("Reading phrase datafile: {}".format(phrase_file))
        with open(phrase_file) as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    phrase, replace_with = row
                    log.debug(f"  phrase: {phrase}, rw: {replace_with}")
                except ValueError:
                    log.error(
                            "Bad input: {} - "
                            "csv parser could not unpack properly.".format(
                                repr(row)))
                self.lookup_dic_CODE.update({replace_with: [phrase]})
                self.lookup_reverse_dic_CODE.update({phrase: [replace_with]})
                log.debug(
                        f"Phrase: {phrase} with id {replace_with}"
                        "added to phrase dictionary.")
        log.debug("Populating phrase dictionary: finished")

    def reverse_replace(self, _token_):
        log.debug(f'Reverse lookup call for "{_token_}".')
        for item in self.lookup_dic_CODE.items():
            _token_ = str.replace(_token_, item[0], item[1][0])
        log.debug(f'Found "{_token_}".')

        return _token_
