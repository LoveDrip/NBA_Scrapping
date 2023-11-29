import requests
import json
from bs4 import BeautifulSoup


# Function to fetch player statistics from NBA API
def get_player_stats(player_id, season):
    print("GET PLAYER STATUS")
    print("PLAYERID: " + player_id + ", SAESON: " + season)

    url = f'https://www.nba.com/stats/player/{player_id}'


    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    player_image_div = soup.find('div', {'class': 'PlayerSummary_mainInnerTeam____nFZ'})
    
    if player_image_div:
        img_tag = player_image_div.find('img', {'class': 'PlayerImage_image__wH_YX PlayerSummary_playerImage__sysif'})
        if img_tag:
            img_src = img_tag['src']
            print("imageSRC: ")
            print(img_src)
            return img_src

    return None

    print("resonse: ")
    print(response)

    # Construct API URL
    # url = f"https://data.nba.com/prod/v1/players/{player_id}/stats?season={season}?api_key=ddEpNB63kFwdMG424MWxhbmirAlMX5V0"

    # print(url)

    # # Send GET request and parse JSON response
    # response = requests.get(url)
    # print("RESPONSE", response)
    # if response.status_code == 200:
    #     data = response.json()
    #     ppg = data["league"]["standard"]["ppg"]

    #     return ppg
    # else:
    #     print(f"Error in API request. Status code: {response.status_code}")
    #     return None

    # data = json.loads(response.text)
    # print("JSON TO DATA", data)

    # Extract average points per game (ppg)
    

# Function to fetch head-to-head (H2H) data from NBA API
def get_h2h_stats(player_id, opponent_id, season):
    # Construct API URL
    url = f"https://data.nba.com/prod/v1/games?playerID={player_id}&opponentTeamID={opponent_id}&season={season}"

    # Send GET request and parse JSON response
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract average ppg against opponent in past 10 games
    h2h_ppg = 0
    count = 0
    for game in data["games"]:
        if count < 10:
            player_stats = game["playerStats"][0]
            h2h_ppg += player_stats["pts"]
            count += 1
        else:
            break

    h2h_ppg /= count

    return h2h_ppg

# Function to calculate player performance percentage
def calculate_performance_percentage(season_ppg, h2h_ppg):
    # Calculate percentage contribution for 70% factor
    percent_70 = 0 if h2h_ppg < season_ppg else 100

    # Calculate percentage contribution for 20% factor
    percent_20 = 0 if abs(h2h_ppg - season_ppg) > 5 else 100

    # Calculate percentage contribution for 10% factor
    percent_10 = 0 if abs(h2h_ppg - season_ppg) > 8 else 100

    # Calculate overall performance percentage
    performance_percentage = 0.7 * percent_70 + 0.2 * percent_20 + 0.1 * percent_10

    return performance_percentage

# Main program
if __name__ == "__main__":
    # Replace with current NBA season
    season = "2023-24"

    # Replace with player IDs and opponent IDs for games tonight
    player_ids = ["1630209", "54321"]
    opponent_ids =  ["23456", "65432"]

    # Iterate through player IDs and calculate performance percentages
    for i in range(len(player_ids)):
        player_id = player_ids[i]
        opponent_id = opponent_ids[i]

        # Get player statistics for the season
        print("START GET PLAYER STATUS")
        season_ppg = get_player_stats(player_id, season)

        # Get head-to-head (H2H) statistics against opponent
        h2h_ppg = get_h2h_stats(player_id, opponent_id, season)

        # Calculate player performance percentage
        performance_percentage = calculate_performance_percentage(season_ppg, h2h_ppg)

        # Print player name and performance percentage
        print(f"Player: {player_id} | Performance Percentage: {performance_percentage:.2f}%")
