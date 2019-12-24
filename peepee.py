import random

def gen():
    """
    generates a caption
    """

    vowel = ["ee", "oo", "ü", "ï", "ëę", "ee"]
    start_cons = ["p", "skl", "kl", "p", "pl", "ph", "f", "f", "sk", "g", "gh", "k"]
    end_cons = ["ng", "p", "pee", "pie", "nk"]

    sentence = "\""
    sentence += random.choice(start_cons) + random.choice(vowel) + random.choice(end_cons)

    for i in range(1, random.randint(2, 4)):
        sentence += " " + random.choice(start_cons) + random.choice(vowel) + random.choice(end_cons)

    sentence += "\""

    firstnames = ["fred", "nehemiah", "haggiah", "bill", "abbadon", "jepson", "obadiah",
                  "rachel", "jane", "susanna", "hera", "demeter", "michelle",
                  "sydney", "jordan", "alex", "ivanka", "cameron", "reese", "tyler",
                  "hayden", "roberta"]
    lastnames = ["carlson", "williamson", "davidson", "johnson", "gonzalez", "rodriguez",
                 "andrew-mcclain", "young", "glietz", "korytov", "mishra", "rudyak", "müller",
                 "mick", "banko", "hammons", "tomiç"]
    adjective = ["discursive", "removed", "furious", "flamboyant", "striking",
                 "morbid", "postmodern", "suprematist", "vindictive",
                 "centered", "draining", "tiring", "calm", "chilling", "polemic",
                 "frightening"]
    subjects = ["existentialism", "the gay experience in 20th century america",
                "nihilism", "everyday objects sitting on the table", "god",
                "the existence of aliens", "the protomolecule", "the Belt",
                "essentialism", "representation and taxation", "the Alps", "nature", "Paris",
                "the struggle between good and evil", "retaining humanity in autonomy"]

    sentence += "\n\t" + "a " + random.choice(adjective) + " piece on "
    sentence += random.choice(subjects) + " by \n\t\t"
    sentence += random.choice(firstnames) + " " + random.choice(lastnames)

    return sentence


if __name__ == '__main__':
    print(gen())
