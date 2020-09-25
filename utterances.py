#!/usr/bin/env

"""
list out the possible combinations of words users can use when triggering
the Doppler Alexa skill.

"""
verbs = ['make', 'turn']
articles = ['the', 'my']
adjectives = ['doppler']
nouns = ['buttons']

for verb in verbs:
    for article in articles:
        for adjective in adjectives:
            print(verb + " " + article + " " + adjective)
        print(verb + " " + article)

