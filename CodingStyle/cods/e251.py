#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def _select(self,context,expr):

	#Copy the context
        con = self._copyContext(context)
        try:
            return Ft.Xml.XPath.Evaluate(expr,context = con)
        except (CompiletimeException, RuntimeException):
            try:
                etype, value, tb = sys.exc_info()
                traceback.print_exception(etype, value, None)
            finally:
                etype = value = tb = None
