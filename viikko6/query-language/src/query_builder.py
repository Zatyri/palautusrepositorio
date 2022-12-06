from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn

class QueryBuilder:
    def __init__(self, query = All()):
        self.queries = query

    def playsIn(self, team):
      return QueryBuilder(And(self.queries, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
      return QueryBuilder(And(self.queries, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
      return QueryBuilder(And(self.queries, HasFewerThan(value, attr)))

    def oneOf(self, *queries):      
      return QueryBuilder(Or(*queries))

    def build(self): 
      return self.queries