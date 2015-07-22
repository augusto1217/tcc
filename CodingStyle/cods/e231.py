#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

class timeType(_Ordered):
    def __init__(self,value):
        try:
            import datetime
            from TimeLib import parse_isotime
            self.value=parse_isotime(value)
            if not self.value:
                raise ValueError

        except:
            from Ft.Lib.Time import FromISO8601
            try:
                self.value=FromISO8601(value)
            except:
                raise ValueError
