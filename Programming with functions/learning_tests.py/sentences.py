"""
This program generates simple english sentences, 
with 6 different variations:
single past
single present
single future
plural past
plural present
plural future
-Seth Ricks 
CSE 111
"""

import random

def main():
    print()
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'past')}.")
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'present')}.") 
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 'future')}.")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'past')}.")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'present')}.") 
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 'future')}.")
    print()

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_adjective():
    """Return a randomly chosen adjective.
    Parameters: none
    Return: a randomly chosen adjective."""

    words = ["pretty", "funny", "clever", "smart", "amazing", "colorful", "crazy", "rich", "small", "large"]
    word = random.choice(words)
    return word

if __name__ == "__main__":
    main()