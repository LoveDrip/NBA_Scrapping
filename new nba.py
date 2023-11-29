import requests, pandas
from bs4 import BeautifulSoup
from nba_api.stats.static import players

# Get all NBA players
all_players = players.get_players()

# Function to get player ID by name
def get_players_id(player_name):
    for player in all_players:
        if player['full_name'] == player_name:
            return player['id']
    return None 

url = "https://www.rotowire.com/basketball/nba-lineups.php"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

lineups = soup.find_all(class_="is-pct-play-100")
# print(lineups)
positions = [x.find('div').text for x in lineups]
# print(positions)
names = [x.find('a')['title'] for x in lineups]
# print(names)
ids = [get_players_id(name) for name in names]
print(ids)
teams = sum([[x.text] * 5 for x in soup.find_all(class_='lineup__abbr')], [])
# print(teams)


# df = pandas.DataFrame(zip(ids, names, teams, positions))
# print(df)
df = pandas.DataFrame(zip(ids))
print(df)