#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

if self.value[2] == 29 and self.value[1] == 2 and ((self.value[0] % 4 != 0) or (self.value[0] % 100 == 0)):
	raise ValueError
