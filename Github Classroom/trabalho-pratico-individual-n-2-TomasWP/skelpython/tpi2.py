#encoding: utf8

# YOUR NAME: Tomás Sousa Fonseca
# YOUR NUMBER: 107245

# COLLEAGUES WITH WHOM YOU DISCUSSED THIS ASSIGNMENT (names, numbers):
# - ...
# - ...

from semantic_network import *
from constraintsearch import *

class MySN(SemanticNetwork):

    def __init__(self):
        SemanticNetwork.__init__(self)
        # ADD CODE HERE IF NEEDED
        self.assoc_stats = {}

    def query_local(self,user=None,e1=None,rel=None,e2=None):
        # IMPLEMENT HERE
        self.query_result = []
        for d in self.declarations:
            for type in self.declarations[d]:
                value = self.declarations[d][type]
                if (isinstance(value, set)):
                    for item in value:
                        if (e1 == None or e1 == type[0]) and (rel == None or rel == type[1]) and (e2 == None or e2 == item):
                            self.query_result.append(Declaration(d, Association(type[0], type[1], item)))
                else:
                    if (e1 == None or e1 == type[0]) and (rel == None or rel == type[1]) and (e2 == None or e2 == value):
                        self.query_result.append(Declaration(d, Association(type[0], type[1], value)))
        return self.query_result

    def query(self,entity,assoc=None):
        # IMPLEMENT HERE
        mbr = self.query_local(e1=entity, rel="member")
        self.query_result = []

        for m in mbr:
            self.query_result.append(self.query_local(e1=m.relation.entity2, rel=assoc))

        return self.query_result

    def update_assoc_stats(self,assoc,user=None):
        # IMPLEMENT HERE
        stats = {}
        for usr in (self.declarations.keys() if user is None else [user]):
            for rel in self.declarations[usr]:
                if rel[1] == assoc:
                    val = self.declarations[usr][rel]
                    if isinstance(val, set):
                        val = tuple(val)
                        for item in val:
                            if item in stats:
                                stats[item] += 1
                            else:
                                stats[item] = 1
                    if val in stats:
                        stats[val] += 1
                    else:
                        stats[val] = 1
        obj = sum(stats.values())
        results = {}
        for val in stats.values():
            if val > 1:
                results.update({val: val})
        nkn = len(stats) - len(results)
        total = obj - nkn + nkn **(1/2)
        freq = {key: value / total for key, value in stats.items()}
        self.assoc_stats[(assoc, user)] = (stats, freq)

class MyCS(ConstraintSearch):

    def __init__(self,domains,constraints):
        ConstraintSearch.__init__(self,domains,constraints)
        # ADD CODE HERE IF NEEDED
        pass

    def search_all(self,domains=None,xpto=None):
        # If needed, you can use argument 'xpto'
        # to pass information to the function
        #
        # IMPLEMENTAR AQUI
        if domains is None:
            domains = self.domains

        def search(assignment):
            if len(assignment) == len(domains):
                solutions.append(assignment.copy())
                return
            
            not_assigned = []

            for v in domains:
                if v not in assignment:
                    not_assigned.append(v)

            var = not_assigned[0]
            min_domain_length = len(domains[var])

            for value in not_assigned:
                if len(domains[value]) < min_domain_length:
                    var = value
                    min_domain_length = len(domains[value]) 

            for value in domains[var]:
                if all(self.constraints.get((var, v), lambda *args: True)(var, value, v, assignment.get(v, None)) for v in assignment if (var, v) in self.constraints):
                    assignment[var] = value
                    search(assignment)
                    del assignment[var]
        solutions = []
        search({})
        return solutions