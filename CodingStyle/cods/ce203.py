#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


def Test(tester):

    from Ft.Xml.XPath import Context
    context1 = Context.Context(DomTree.CHILD1, 1, 2)
    context2 = Context.Context(DomTree.CHILD2, 2, 2)
    plT = ParsedPredicateList.ParsedPredicateList([boolT])
    plF = ParsedPredicateList.ParsedPredicateList([boolF])

    tests = {
        ParsedExpr.ParsedFilterExpr: [
            ((nodeset2, plT), context1, list(
                nodeset2.val)), ((nodeset2, plF), context1, []), ], ParsedExpr.ParsedPathExpr: [
            ((0, nodeset2, nodeset1), context1, list(
                nodeset1.val)), ], ParsedExpr.ParsedUnionExpr: [
            ((nodeset2, nodeset1), context1, list(
                nodeset2.val)), ], }
