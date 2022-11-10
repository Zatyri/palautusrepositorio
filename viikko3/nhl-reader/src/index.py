import requests
from player import Player
from playerReader import PlayerReader
from playerStats import PlayerStats

def main():    

    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    stats.printGoalsAndAssists("FIN")

if __name__ == "__main__":
    main()
