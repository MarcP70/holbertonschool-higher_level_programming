#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        letter = sentence[0]
    else:
        letter = None
    return len(sentence), letter