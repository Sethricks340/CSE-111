import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    words_list = []

    print(numbers_list)

    append_random_numbers(numbers_list)
    print(numbers_list)
    
    append_random_numbers(numbers_list, 3)
    print(numbers_list)

    print(words_list)

    append_random_words(words_list)
    print(words_list)

    append_random_words(words_list, 3)
    print(words_list)

def append_random_numbers(numbers_list, quantity=1):

    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):
    
    random_words = ["Hello", "goodbye", "yo", "quiero", "vaya", "pues", "pucha", "entonces?", "nunca", "pelota", "lentes"]


    for _ in range(quantity):
        random_word = random.choice(random_words)
        words_list.append(random_word)


if __name__ == "__main__":
    main()
