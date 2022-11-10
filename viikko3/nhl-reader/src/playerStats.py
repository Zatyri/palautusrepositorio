class PlayerStats:
  def __init__(self, reader):
    self.players = reader.get_players()

  def printGoalsAndAssists(self, nationality):
    
    filtered = list(filter(lambda x: x.nationality == nationality, self.players))
    filtered.sort(reverse=True, key=lambda x: x.goals + x.assists)
    
    for player in filtered:
      print(
          f"{player.name:20} {player.team:2} {player.goals:2} + {player.assists:2} = {player.goals + player.assists}")
