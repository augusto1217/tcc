# -*- coding: iso-8859-1 -*-
'''
Created on Jan 17, 2015
Funcionalide para extração de arquivos e execução
das métricas do PEP8
@author: augusto
'''
import os
import shutil
import sys
import tempfile

from ExtractFiles import Extract


if __name__ == '__main__':

    sys.setrecursionlimit(2147483647)

    originPathFiles = '/tcc-unb/arquivos/'
    destPathFiles = '/tcc-unb/arquivos_orig/whl/'

    e = Extract(originPathFiles)

    files = e.getFiles('*.whl')
    files.sort()

    count = 0

    for f in files:

        f2 = f
    print f2
        count = count + 1
        destdir = tempfile.mkdtemp()
        e.extractFiles(f, destdir)
        pys = e.matches(destdir)
        e.logProject(f, pys)

        for f in pys:
            print '--', f
            sys.stdout.flush()
            command = 'flake8 {} -qq --statistics'.format(f)
            os.system(command)
            sys.stdout.flush()

        shutil.rmtree(destdir)
        os.system("mv " + f2 + " " + destPathFiles)
    command = None
    f2 = None
    pys = None

    print 'qtd file =' + str(count)
    path = os.path.abspath('.')
    e = Extract(path)

    files = e.getFiles('/*.pyc')
    for f in files:
        os.remove(f)
