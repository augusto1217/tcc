#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def dom_from_file(tester, uri):
    tester.startTest("Reading Document")
    isrc = InputSource.DefaultFactory.fromUri(uri)
    result=tester.test_data['parse'](isrc)
    tester.testDone()
    return result
