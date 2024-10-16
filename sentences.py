"""
Author: Tirso Lopez
Activity cse111 week 02 -- sentences.py

A program that generate sentences with three parts:
a determiner
a noun
a verb
"""
import random

def main():

    def get_adjective():
        #function to add an adjective to the sentences produced by your program / strecht functions
        words = ["attractive","bald","beautiful","chubby","clean","dazzling","drab","elegant","fancy","fit","flabby","glamorous","gorgeous","handsome","long","magnificent","muscular","plain","plump","quaint","scruffy","shapely","short","skinny","stocky","ugly","unkempt","unsightly"]
        word = random.choice(words)
        return word

    def get_preposition():
        #Return a randomly chosen preposition from this list of prepositions:
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        word = random.choice(words)
        return word
    
    def get_prepositional_phrase(quantity):
#   Build and return a prepositional phrase composed
#   of three words: a preposition, a determiner, and a
#   noun by calling the get_preposition, get_determiner,
#   and get_noun functions.
#   Parameter
#       quantity: an integer that determines if the
#           determiner and noun in the prepositional
#           phrase returned from this function should
#           be single or pluaral.
#   Return: a prepositional phrase.
        prep = get_preposition()
        det = get_determiner(quantity)
        noun = get_noun(quantity)
        prep = prep.capitalize()
        det = det.capitalize()
        noun = noun.capitalize()
        
        return f"{prep} {det} {noun}"
  
     
    def get_determiner(quantity):
        # Return a randomly chosen determiner. A determiner is
        #   a word like "the", "a", "one", "some", "many".

        if quantity == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word

    def get_noun(quantity):
    #   Return a randomly chosen noun.
        if quantity == 1:
            words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
        else:
            words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word

    def get_verb(quantity, tense):
    #   Return a randomly chosen verb. depending of the verb
    #   Return: a randomly chosen verb.

        if tense == "past":
            words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        if tense == "future":
            words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

        if tense == "present":
            if quantity == 1:    
                words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
            else:
                words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
        
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word

    def make_sentence(quantity, tense):
    #   Build and return a sentence with three words:
    #   a determiner, a noun, and a verb. 
       a_determiner_word = get_determiner(quantity)
       noun = get_noun(quantity)
       verb = get_verb(quantity, tense)
       prep_phase = get_prepositional_phrase(quantity)
       adjective = get_adjective()
       
       print(f"{a_determiner_word.capitalize()} {noun.capitalize()} {adjective.capitalize()} {verb.capitalize()} {prep_phase}")
       

       

    #program outputs six sentences with the following characteristics:
    # Quantity Verb   Tense
    #     a.	single	past
    #     b.	single	present
    #     c.	single	future
    #     d.	plural	past
    #     e.	plural	present
    #     f.	plural	future

    # Four parallel lists, one list for each attribute of the item.
    item = [
        1,1,1,2,2,2
    ]
    verb_tense = [
        "past","present","future","past","present","future"
    ]
    
    # For each can in the parallel lists, unpack the values
    # into the variables item and verb tense.
    for i in range(len(item)):
        quantity = item[i]
        tense = verb_tense[i]
        make_sentence(quantity,tense)
    
main()



