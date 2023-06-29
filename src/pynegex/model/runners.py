from os.path import join
from os import path
from .negex import *
# import csv
# from typing import List

pwd = path.dirname(path.abspath(__file__))


def run(text: str, ent_tag: str, triggerset_name: str, speculation=True):
    try:
        if triggerset_name.lower() in ["en", "chapman-en"]:
            triggers_path = join(pwd, "triggersets/chapman-en.txt")
        elif triggerset_name.lower() in ["de", "cotik-de"]:
            triggers_path = join(pwd, "triggersets/cotik-de.txt")
        else:
            raise ValueError(
                f"No trigger set available: {triggerset_name}")

        triggers_set = open(triggers_path)
        irules = sortRules(triggers_set.readlines())

        tagger = negTagger(sentence=text, phrases=[
            ent_tag], rules=irules, negP=speculation)
        return [tagger.getNegationFlag(), tagger.getNegTaggedSentence()]
    except Exception as e:
        print(e)
        # raise Exception("Exception raised at run() of negex model")
