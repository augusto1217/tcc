#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def Test(tester):
    tester.startGroup('CDATA sections in doc')
    
    isrc = InputSource.DefaultFactory.fromString(SRC_1,
                                                 Uri.OsPathToUri(os.getcwd()))
    doc = NonvalidatingReader.parse(isrc)
    con = Context.Context(doc, 1, 1)

    EXPR = '/doc/elem/text()'
    expr = Compile(EXPR)
    tester.startTest(EXPR)
    actual = [ node.data for node in expr.evaluate(con) ]
    tester.compare(actual, ["abc"]*3)
    tester.testDone()

    return tester.groupDone()
