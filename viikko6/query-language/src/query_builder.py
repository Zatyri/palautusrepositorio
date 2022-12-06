from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn


class QueryBuilder:
    def __init__(self, query = [All()]):
        self.queries = query

    def playsIn(self, team):
      self.queries.append(PlaysIn(team))      
      return QueryBuilder(self.queries)

    def hasAtLeast(self, value, attr):
      self.queries.append(HasAtLeast(value, attr))   
      return QueryBuilder(self.queries)

    def hasFewerThan(self, value, attr):
      self.queries.append(HasFewerThan(value, attr))
      return QueryBuilder(self.queries)

    def oneOf(self, *queries):      
      for query in queries:
        self.queries.append(Or(query._matchers))

      return QueryBuilder(self.queries)

    def build(self): 
      return And(*self.queries)