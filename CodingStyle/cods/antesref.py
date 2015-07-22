#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

def censor(text,word):
    while word in text:
        text = text[:text.find(word)] + "*"*len(word) + text[text.find(word) + len(word):]
    return text
