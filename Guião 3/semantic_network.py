

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
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
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
        