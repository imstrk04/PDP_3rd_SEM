import re


def check_sent(str):
    verbs = [
        "cut", "cuts",
        "sing", "sings",
        "dance", "dances",
        "fell", "falls",
        "ate", "eats",
        "drink", "drinks",
        "beat", "beats",
        "like", "likes",
        "run", "runs",
        "jump", "jumps",
        "see", "sees",
        "read", "reads",
        "play", "plays",
        "write", "writes",
        ]
    verbs = "|".join(verbs)
    pattern = rf"(^[a-z\s].+)\s({verbs})\s([a-z\s]+$)"
    return bool( re.fullmatch(pattern, str.lower()))


if __name__ ==  '__main__':
    if check_sent(input('Enter sentence: ')):
        print('Sentence is valid')
    else:
        print('Sentence is not valid')
    