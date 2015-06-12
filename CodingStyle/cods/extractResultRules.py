# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2015

@author: augusto mariano
'''

ignore_list = ['E121', 'E123', 'E126', 'E133', 'E226', 'E241', 'E242', 'E704']
ignore_extra = ['', '']

errorCodes = {
    'E101': [0] * 4,
    'E111': [0] * 4,
    'E112': [0] * 4,
    'E113': [0] * 4,
    'E114': [0] * 4,
    'E115': [0] * 4,
    'E116': [0] * 4,
    'E121': [0] * 4,
    'E122': [0] * 4,
    'E123': [0] * 4,
    'E124': [0] * 4,
    'E125': [0] * 4,
    'E126': [0] * 4,
    'E127': [0] * 4,
    'E128': [0] * 4,
    'E129': [0] * 4,
    'E131': [0] * 4,
    'E133': [0] * 4,
    'E201': [0] * 4,
    'E202': [0] * 4,
    'E203': [0] * 4,
    'E211': [0] * 4,
    'E221': [0] * 4,
    'E222': [0] * 4,
    'E223': [0] * 4,
    'E224': [0] * 4,
    'E225': [0] * 4,
    'E226': [0] * 4,
    'E227': [0] * 4,
    'E228': [0] * 4,
    'E231': [0] * 4,
    'E241': [0] * 4,
    'E242': [0] * 4,
    'E251': [0] * 4,
    'E261': [0] * 4,
    'E262': [0] * 4,
    'E265': [0] * 4,
    'E266': [0] * 4,
    'E271': [0] * 4,
    'E272': [0] * 4,
    'E273': [0] * 4,
    'E274': [0] * 4,
    'E301': [0] * 4,
    'E302': [0] * 4,
    'E303': [0] * 4,
    'E304': [0] * 4,
    'E401': [0] * 4,
    'E501': [0] * 4,
    'E502': [0] * 4,
    'E701': [0] * 4,
    'E702': [0] * 4,
    'E703': [0] * 4,
    'E704': [0] * 4,
    'E711': [0] * 4,
    'E712': [0] * 4,
    'E713': [0] * 4,
    'E714': [0] * 4,
    'E721': [0] * 4,
    'E731': [0] * 4,
    'E901': [0] * 4,
    'E902': [0] * 4,
    'W191': [0] * 4,
    'W291': [0] * 4,
    'W292': [0] * 4,
    'W293': [0] * 4,
    'W391': [0] * 4,
    'W601': [0] * 4,
    'W602': [0] * 4,
    'W603': [0] * 4,
    'W604': [0] * 4,
}


class MetricsFiles:

    def read_project(self, path):

        infile = open(path)
        projects = dict()
        project = None
        modules = -1
        module = None

        for line in infile:
            if not (line.startswith('/tcc-unb')):
                if line[0] == '[':
                    project = line[1:-2]
                    projects[project] = [0, 0, dict()]
                    modules = -1
                    continue
    
                if modules == -1:
                    x, _ = line.split(' ')
                    modules = int(x)
                    projects[project][0] = modules
                    continue
    
                if line[0:2] == '--':
                    x, module = line.split(' ', 1)
                    projects[project][2][module] = dict()
                    continue
    
                line = ' '.join(line.split())
                tokens = line.split(' ')
    
                if not(line.startswith('unknown option')):
    
                    qtd = int(tokens[0])
                    code = tokens[1]
    
                    if code in ignore_list:
                        continue
    
                    if code in ignore_extra:
                        continue
    
                    projects[project][1] += qtd
    
                    if code in projects[project][2][module]:
                        projects[project][2][module][code] += qtd
                    else:
                        projects[project][2][module][code] = qtd
    
                    self.projects = projects

    def printMetrics(self):
        messages = [
            '[Global] Numero de projetos: {}',
            '[Global] Numero de projetos com erros: {}',
            '[Global] Numero de modulos: {}',
            '[Global] Numero de modulos com erros: {}',
            '[Global] Total de ocorrencias de erros: {}',
            '[Global] Quantidade de erros distintos: {}',
            '[Projeto] Número médio de módulos: {}',
            '[Projeto] Projeto com maior numero de modulos: {} ({} modulos)',
            '[Projeto] Projeto com maior numero de erros: {} ({} erros)',
            '[Projeto] Porcentagem de módulos com erro: {}',
            '[Projeto] Número médio de módulos com erro: {}',
            '[Projeto] Número médio de erros distintos: {}',
        ]

        print '\n'.join(messages).format(self.gNumberProjects,
                                         self.gNumberProjectsError,
                                         self.gNumberModule,
                                         self.gNumberModulesError,
                                         self.gNumberOccurrenceTotalError,
                                         self.gAmountDistinctErros,
                                         self.pMeanModules,
                                         ', '.join(self.pMaxModulesProjects),
                                         self.pMaxModules,
                                         ', '.join(self.pMaxErrorsProjects),
                                         self.pMaxErrors,
                                         self.pPercentModulesError,
                                         self.pMeanModulesError,
                                         self.pMeanAmountDistinctErros)

        messages = [
            '\n[{}] Numero de Projetos: {}',
            '[{}] Número de módulos: {}',
            '[{}] Total de ocorrências: {}',
            '[{}] Porcentagem em relação ao total de erros: {}',
        ]

        for k, v in errorCodes.items():
            for i in range(4):
                print messages[i].format(k, v[i])

    def extractMetrics(self):
        projects = self.projects

        self.gNumberProjects = len(projects)
        self.gNumberProjectsError = 0
        self.gNumberModule = 0
        self.gNumberModulesError = 0
        self.gNumberOccurrenceTotalError = 0
        self.pMaxModules = -1
        self.pMaxModulesProjects = []
        self.pMaxErrors = -1
        self.pMaxErrorsProjects = []
        self.e121Count = 0

        errors = set()

        for k, v in projects.items():
            self.gNumberModule += v[0]

            projectsErrors = set()

            if v[0] > self.pMaxModules:
                self.pMaxModules = v[0]
                self.pMaxModulesProjects = [k]
            elif v[0] == self.pMaxModules:
                self.pMaxModulesProjects.append(k)

            self.gNumberOccurrenceTotalError += v[1]

            if v[1] > self.pMaxErrors:
                self.pMaxErrors = v[1]
                self.pMaxErrorsProjects = [k]
            elif v[1] == self.pMaxErrors:
                self.pMaxErrorsProjects.append(k)

            if v[1] > 0:
                self.gNumberProjectsError += 1

            for _, y in v[2].items():

                for errCode, metrics in errorCodes.items():
                    if errCode in y:
                        metrics[1] += 1
                        metrics[2] += y[errCode]

                if len(y) > 1:
                    self.gNumberModulesError += 1

                for error in y:
                    errors.add(error)
                    projectsErrors.add(error)

            for code, metrics in errorCodes.items():
                if code in projectsErrors:
                    metrics[0] += 1

        self.gAmountDistinctErros = len(errors)
        self.pMeanModules = 1.0 * self.gNumberModule / self.gNumberProjects
        temp = 100.0 * self.gNumberModulesError / self.gNumberModule
        self.pPercentModulesError = temp
        temp = 1.0 * self.gNumberModulesError / self.gNumberProjects
        self.pMeanModulesError = temp
        temp = 1.0 * self.gAmountDistinctErros / self.gNumberProjects
        self.pMeanAmountDistinctErros = temp

        for code, metrics in errorCodes.items():
            metrics[3] = 100.0 * metrics[2] / self.gNumberOccurrenceTotalError


if __name__ == '__main__':

    metricsFile = MetricsFiles()
    metricsFile.read_project('resultado-flake8.txt')
    metricsFile.extractMetrics()
    metricsFile.printMetrics()

