#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

from random import randint
import string
import sys

def get_input():
    # fname = "text_samples/neuromancer.txt"
    # fname = "text_samples/wasteland.txt"
    # fname = "text_samples/cat_in_hat.txt"
    # fname = "text_samples/green_eggs_ham.txt"
    # fname = "text_samples/obama.txt"
    fname = sys.argv[1]

    #output_len = 20
    output_len = int(sys.argv[2])

    return (fname, output_len)

def main():
    (fname, output_len) = get_input()
    text = open(fname, 'r').read()
    text = clean(text)
    markov_chain_length = 3

    # Simulate markov speech
    (output, nbranches) = doMarkov(text, output_len, markov_chain_length)

    print ' '.join(output)
    print nbranches

def doMarkov(text, output_len, chain_n):
    # Get all words
    words = text.split()

    ### PART 1: Start the text ###
    # Choose a random place in the text
    randno = randint(0,len(words)-chain_n)
    output = words[randno:randno+chain_n]

    ### PART 2: generate the rest ###
    # Keep track of the number of times the code actually made a decision
    nbranches = 0

    # Find all occurences of this string of words, and collect the next word
    while len(output) < output_len:
        state = output[-chain_n:]
        history = []

        # Collect stats on past states like this
        validCount = 0
        for i in range(len(words)-chain_n-1):
            isValid = True
            for j in range(chain_n):
                isValid &= state[j]==words[i+j]
            if isValid:
                history.append(words[i+chain_n])

        # Keep track of the number of times the simulation made a choice
        if len(history) > 1:
            nbranches += 1

        # Pick a next word at random from the list
        randno = randint(0, len(history)-1)  
        output.append(history[randno])

    return (output, nbranches)

# I tested several methods of cleaning the text
def clean(text):
    text.replace('\n', ' ')
    #text = text.lower()
    #text = ''.join([let if let in string.printable else ' ' for let in text])
    #letset = string.letters + ".-,!'?"
    #text = ''.join([let if let in letset else ' ' for let in text])
    return text

if __name__ == '__main__':
    main()

