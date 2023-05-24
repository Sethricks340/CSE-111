from sentences import get_determiner, get_noun, get_verb, get_adjective
import random
import pytest


def test_get_determiner():
    
    #Test the single determiners.

    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    #Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(11):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(11):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_noun list.
        assert word in plural_nouns


def test_get_verb():


    #Test the past verbs. 
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(11):

        # Call the get_verb function which
        # should return a past verb. 
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_verbs list.
        assert word in past_verbs


    #Test the present singular verbs
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(11):
        
        # Call the get_verb function which
        # should return a present singular verb. 
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present singular verbs list.
        assert word in present_singular_verbs

    #Test the present plural verbs
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(11):
        
        # Call the get_verb function which
        # should return a present plural verb. 
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present plural verbs list.
        assert word in present_plural_verbs

    #Test the future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(11):
        
        # Call the get_verb function which
        # should return a future verb. 
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future verbs list.
        assert word in future_verbs

def test_get_adjective():

    #test adjectives
    adjectives = ["pretty", "funny", "clever", "smart", "amazing", "colorful", "crazy", "rich", "small", "large"]

    for _ in range(11):
        
        # Call the get_adjectivefunction which
        # should return a random adjective. 
        word = get_adjective()

        # Verify that the word returned from get_adjective
        # is one of the words in the advectives list.
        assert word in adjectives

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])