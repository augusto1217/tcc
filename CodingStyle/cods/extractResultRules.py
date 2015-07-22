# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2015
Analisa arquivo com as violações obtidas de projetos 
do repositório do PYPI.
@author: augusto mariano
'''

ignore_list = ['E121', 'E123', 'E126', 'E133', 'E226', 'E241', 'E242', 'E704']
ignore_extra = ['', '']

error_codes = {
    'E101': [0] * 4, 'E111': [0] * 4, 'E112': [0] * 4, 'E113': [0] * 4,
    'E114': [0] * 4, 'E115': [0] * 4, 'E116': [0] * 4, 'E121': [0] * 4,
    'E122': [0] * 4, 'E123': [0] * 4, 'E124': [0] * 4, 'E125': [0] * 4,
    'E126': [0] * 4, 'E127': [0] * 4, 'E128': [0] * 4, 'E129': [0] * 4,
    'E131': [0] * 4, 'E133': [0] * 4, 'E201': [0] * 4, 'E202': [0] * 4,
    'E203': [0] * 4, 'E211': [0] * 4, 'E221': [0] * 4, 'E222': [0] * 4,
    'E223': [0] * 4, 'E224': [0] * 4, 'E225': [0] * 4, 'E226': [0] * 4,
    'E227': [0] * 4, 'E228': [0] * 4, 'E231': [0] * 4, 'E241': [0] * 4,
    'E242': [0] * 4, 'E251': [0] * 4, 'E261': [0] * 4, 'E262': [0] * 4,
    'E265': [0] * 4, 'E266': [0] * 4, 'E271': [0] * 4, 'E272': [0] * 4,
    'E273': [0] * 4, 'E274': [0] * 4, 'E301': [0] * 4, 'E302': [0] * 4,
    'E303': [0] * 4, 'E304': [0] * 4, 'E401': [0] * 4, 'E501': [0] * 4,
    'E502': [0] * 4, 'E701': [0] * 4, 'E702': [0] * 4, 'E703': [0] * 4,
    'E704': [0] * 4, 'E711': [0] * 4, 'E712': [0] * 4, 'E713': [0] * 4,
    'E714': [0] * 4, 'E721': [0] * 4, 'E731': [0] * 4, 'E901': [0] * 4,
    'E902': [0] * 4, 'W191': [0] * 4, 'W291': [0] * 4, 'W292': [0] * 4,
    'W293': [0] * 4, 'W391': [0] * 4, 'W601': [0] * 4, 'W602': [0] * 4,
    'W603': [0] * 4, 'W604': [0] * 4,
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

    def print_metrics(self):
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
            '[Projeto] Não Houve erros: {}',
        ]

        print '\n'.join(messages).format(self.g_number_projects,
                                         self.g_number_projects_error,
                                         self.g_number_module,
                                         self.g_number_modules_error,
                                         self.g_number_occurrence_total_error,
                                         self.g_amount_distinct_erros,
                                         self.p_mean_modules,
                                         ', '.join(self.p_max_modules_projects),
                                         self.p_max_modules,
                                         ', '.join(self.p_max_errors_projects),
                                         self.p_max_errors,
                                         self.p_percent_modules_error,
                                         self.p_mean_modules_error,
                                         self.p_mean_amount_distinct_erros,
                                         self.p_mean_amount_not_erros)

        messages = [
            '\n[{}] Numero de Projetos: {}',
            '[{}] Número de módulos: {}',
            '[{}] Total de ocorrências: {}',
            '[{}] Porcentagem em relação ao total de erros: {}',
        ]

        for k, v in error_codes.items():
            for i in range(4):
                print messages[i].format(k, v[i])

    def extract_metrics(self):
        projects = self.projects

        self.g_number_projects = len(projects)
        self.g_number_projects_error = 0
        self.g_number_module = 0
        self.g_number_modules_error = 0
        self.g_number_occurrence_total_error = 0
        self.p_max_modules = -1
        self.p_max_modules_projects = []
        self.p_max_errors = -1
        self.p_max_errors_projects = []
        self.e121Count = 0

        errors = set()

        for k, v in projects.items():
            self.g_number_module += v[0]

            projectsErrors = set()

            if v[0] > self.p_max_modules:
                self.p_max_modules = v[0]
                self.p_max_modules_projects = [k]
            elif v[0] == self.p_max_modules:
                self.p_max_modules_projects.append(k)

            self.g_number_occurrence_total_error += v[1]

            if v[1] > self.p_max_errors:
                self.p_max_errors = v[1]
                self.p_max_errors_projects = [k]
            elif v[1] == self.p_max_errors:
                self.p_max_errors_projects.append(k)

            if v[1] > 0:
                self.g_number_projects_error += 1

            for _, y in v[2].items():

                for errCode, metrics in error_codes.items():
                    if errCode in y:
                        metrics[1] += 1
                        metrics[2] += y[errCode]

                if len(y) > 1:
                    self.g_number_modules_error += 1

                for error in y:
                    errors.add(error)
                    projectsErrors.add(error)

            for code, metrics in error_codes.items():
                if code in projectsErrors:
                    metrics[0] += 1

        self.g_amount_distinct_erros = len(errors)
        self.p_mean_modules = 1.0 * self.g_number_module / self.g_number_projects
        temp = 100.0 * self.g_number_modules_error / self.g_number_module
        self.p_percent_modules_error = temp
        temp = 1.0 * self.g_number_modules_error / self.g_number_projects
        self.p_mean_modules_error = temp
        temp = 1.0 * self.g_amount_distinct_erros / self.g_number_projects
        self.p_mean_amount_distinct_erros = temp
        
        temp = self.g_number_projects - self.g_number_projects_error
        self.p_mean_amount_not_erros = temp

        for code, metrics in error_codes.items():
            metrics[3] = 100.0 * metrics[2] / self.g_number_occurrence_total_error


if __name__ == '__main__':

    metricsFile = MetricsFiles()
    metricsFile.read_project('resultado-flake8.txt')
    metricsFile.extract_metrics()
    metricsFile.print_metrics()

