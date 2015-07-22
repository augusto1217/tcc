#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Implementation of '4xupdate' command
(functions defined here are used by the Ft.Lib.CommandLine framework)

Copyright 2006 Fourthought, Inc. (USA).
Detailed license and copyright information: http://4suite.org/COPYRIGHT
Project home, documentation, distributions: http://4suite.org/
"""

import sys
import cStringIO

from Ft.Lib import UriException, CloseStream
from Ft.Lib.CommandLine import CommandLineApp, Options, Arguments
from Ft.Lib.CommandLine.CommandLineUtil import SourceArgToInputSource
from Ft.Xml import Domlette, XUpdate
from Ft.Xml.InputSource import DefaultFactory

class XUpdateCommandLineApp(CommandLineApp.CommandLineApp):

    from Ft.__config__ import \
        NAME as project_name, VERSION as project_version, URL as project_url

    name = '4xupdate'
    summary = 'command-line tool for performing XUpdates on XML documents'
    description = """4XUpdate command-line application"""
    
