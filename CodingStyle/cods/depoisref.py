#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

def censor(text, word):
    censor_string = '*' * len(word)
    return censor_string.join(text.split(word))

