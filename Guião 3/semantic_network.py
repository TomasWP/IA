

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from collections import Counter


class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)
    
class AssocOne(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

class AssocNum(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,float(e2))


#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return str(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None, rel_type=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2)
                and (rel_type == None or isinstance(d.relation, rel_type)) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
    def list_associations(self):
        return sorted({ d.relation.name for d in self.declarations if type(d.relation)==Association })
    def list_objects(self):
        return sorted({ d.relation.entity1 for d in self.declarations if type(d.relation)==Member })
    def list_users(self):
        return sorted({ d.user for d in self.declarations })
    def list_types(self):
        return sorted(list(set([d.relation.entity2 for d in self.declarations if type(d.relation)==Member] + [d.relation.entity1 for d in self.declarations if type(d.relation)==Subtype] + [d.relation.entity2 for d in self.declarations if type(d.relation)==Subtype])))
    def list_local_associations(self,obj):
        return sorted({ d.relation.name for d in self.declarations if type(d.relation)==Association and d.relation.entity1==obj })
    def list_relations_by_user(self,user):
        return sorted({ d.relation.name for d in self.declarations if d.user==user })
    def associations_by_user(self,user):
        return len(sorted({ d.relation.name for d in self.declarations if type(d.relation)==Association and d.user==user }))
    def list_local_associations_by_entity(self,obj):
        return sorted(list(set([(d.relation.name,d.user) for d in self.declarations if type(d.relation)==Association and d.relation.entity1==obj])))
    def predecessor(self,entity1,entity2):

        if entity1 == entity2:
            return True
        if entity1 not in self.list_types():
            return False
        for declaration in self.declarations:
             if declaration.relation.entity1 == entity2 and isinstance(declaration.relation, Member):
                return True
        return False
    def predecessor_path(self,entity1,entity2):

        pds = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity2]
        if entity1 in pds:
            return [entity1, entity2]
        for declaration in pds:
             path = self.predecessor_path(entity1, declaration)
             if path is not None:
                 return  path+[entity2]
             
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) 
            ]
        return self.query_result
    def query(self, entity, ass_name=None):
        declarations = [declaration for declaration in self.declarations
                        if not isinstance(declaration.relation, Association)
                        and declaration.relation.entity1 == entity
                        ]
        associations = [association for association in self.query_local(e1=entity, rel=ass_name)
                        if isinstance(association.relation, Association)]
        for declaration in declarations:
            associations += self.query(declaration.relation.entity2, ass_name)
        return associations
    def query2(self, entity, ass_name=None):

        local = [query for query in self.query_local(e1=entity, rel=ass_name)
                    if isinstance(query.relation, Member) or isinstance(query.relation, Subtype)
                ]

        herdadas = self.query(entity=entity, ass_name=ass_name)

        return local+herdadas
    
    def query_cancel(self, entity, association_name):
        ldeclartions = self.query_local(e1=entity)
        lparents = [ d.relation.entity2 for d in ldeclartions if not isinstance(d.relation, Association) ]

        lassoc = [ d for d in ldeclartions if isinstance(d.relation, Association) and d.relation.name == association_name ]
        
        if lassoc == []:
            for p in lparents:
                lassoc += self.query_cancel(p, association_name)

        print(f'lassoc: {lassoc}')
        return lassoc
    
    def query_down(self, entity, association_name, child=False):
        ldeclartions = self.query_local(e2=entity)
        lchildren = [ d.relation.entity1 for d in ldeclartions if not isinstance(d.relation, Association) ]

        lassoc = []
        if child:
            lassoc = [ d for d in self.query_local(e1=entity) if isinstance(d.relation, Association) 
                                                                and d.relation.name == association_name ]
    
        for c in lchildren:
            lassoc += self.query_down(c, association_name, child=True)

        return lassoc
    
    def all_descendants(self, rel):
        # Similar to all_predecessors, but in reverse direction
        visited = set()

        def dfs(entity):
            if entity in visited:
                return []
            visited.add(entity)
            descendants = []
            for d in self.declarations:
                if type(d.relation) in [Member, Subtype] and d.relation.entity1 == entity:
                    descendants.append(d.relation.entity2)
                    descendants.extend(dfs(d.relation.entity2))
            return descendants

        return dfs(rel)

    def query_induce(self, entity, assocName):
        query = self.query_down(entity, assocName)

        if not query:
            return None

        # Start counter for association values (entity2)
        c = Counter([d.relation.entity2 for d in query])
        
        # Return the most common one        
        return c.most_common(1)[0][0]
        
    def query_local_assoc(self, entity, assocName):
        # Make local query for assoName Associations for entity
        localQueryAssoc = self.query_local(e1=entity, rel=assocName, rel_type=(Association, AssocOne, AssocNum))

        # Get values for entity
        values = [d.relation.entity2 for d in localQueryAssoc]

        if not localQueryAssoc:
            pass

        elif isinstance(localQueryAssoc[0].relation, AssocOne):
            # Get most common
            val, count = Counter(values).most_common(1)[0]
            # Return most frequent value and its frequency
            return (val, count/len(values))

        elif isinstance(localQueryAssoc[0].relation, AssocNum):
            # Find average value
            return sum(values)/len(values)

        elif isinstance(localQueryAssoc[0].relation, Association):
            # Get most common
            mc = Counter(values).most_common()
            # Return list of frequencies
            # Only return  values until frequency sum reaches 0.75
            frequencies = []
            frequency = 0
            for val, count in mc:
                frequencies.append((val, count/len(localQueryAssoc)))
                frequency += count/len(localQueryAssoc)
                if frequency >= 0.75:
                    return frequencies
        
        return None

    # 2.16.
    def query_assoc_value(self, entity, assocName):
        # Make local query for assocName Associations for entity
        localQueryAssoc = self.query_local(e1=entity, rel=assocName, rel_type=(Association, AssocOne, AssocNum))

        # Get values for entity
        lvalues = [d.relation.entity2 for d in localQueryAssoc]

        # a) If all local associations have the same value, return it
        if len(set(lvalues)) == 1:
            return lvalues[0]

        # b) Otherwise, ...
        # Get predecessor values
        predecessorsPlusLocal = self.query(entity=entity, rel=assocName)
        # Because it includes locals, remove them
        predecessors = [a for a in predecessorsPlusLocal if a not in localQueryAssoc]
        # Get values from relations (entity2)
        pvalues = [p.relation.entity2 for p in predecessors]

        # Define method to find the percentage of a value inside a list of values
        def perc(list, value):
            if list == []: return 0
            return len([l for l in list if l ==  value]) / len(list)
        
        # Return the most common value between local and predecessor relations 
        return max(lvalues + pvalues, key=lambda v: (perc(lvalues, v) + perc(pvalues, v)) / 2)
        