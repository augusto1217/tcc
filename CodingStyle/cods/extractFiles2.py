# -*- coding: iso-8859-1 -*-
'''
Created on Jan 17, 2015
Funcionalide para extração de arquivos e execução
das métricas do PEP8
@author: augusto
'''
import fnmatch
import glob
import os
import sys
import tarfile
import zipfile


class Extract:

    def __init__(self, path):
        self.path = path

    def getFiles(self, extension):
        path = self.path + extension
        files = glob.glob(path)
        return files

    def extractFiles(self, f, destdir):
        try:
            tar = tarfile.open(f)
            tar.extractall(destdir)
        tar.close()
        except tarfile.ReadError:
            z = zipfile.ZipFile(f)
            z.extractall(destdir)

    def matches(self, destdir):

        matches = []

        for dirpath, dirnames, filenames in os.walk(destdir):
            for filename in fnmatch.filter(filenames, '*.py'):
                matches.append(os.path.join(dirpath, filename))

        self.cleanVariaveis(dirnames)
        return matches

    def logProject(self, f, pys):
        print '[{}]'.format(os.path.basename(f))
        print '{} modules'.format(len(pys))
        sys.stdout.flush()

    def cleanVariaveis(self, var):
        self.var = None
