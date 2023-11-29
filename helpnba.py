import requests, pandas
import pandas as pd
import json_normalize
import json
from bs4 import BeautifulSoup
#import NBAScheduleToday
from bs4 import BeautifulSoup as bs
import numpy as np
import datetime
import time
from datetime import date, timedelta
from sqlalchemy import create_engine
import pymysql
import mysql.connector
pymysql.install_as_MySQLdb()
today = datetime.date.today()
from nba_api.stats.static import players
players_dict = players.get_players()
from nba_api.stats import endpoints
from nba_api.stats.endpoints import playbyplayv2
from nba_api.stats.endpoints import leaguegamelog
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import leaguedashptstats
from nba_api.stats.endpoints import teamplayerdashboard
# Set date variables
day = date.today()
day_m1 = date.today() - timedelta(1)
print("Date")
print(day_m1)

# Vs Orlando Magic
try:
    response = endpoints.LeagueDashPlayerStats(season = '2023-24' ,last_n_games = '10', opponent_team_id ='1610612765',per_mode_detailed= 'PerGame')
    # url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2023-24&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
    # headers = {
    #     'Host': 'stats.nba.com',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     'Referer': 'https://stats.nba.com/',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Connection': 'keep-alive',
    #     'x-nba-stats-origin': 'stats',
    #     'x-nba-stats-token': 'true'
    # }
    # response = requests.get(url=url, headers=headers).json()
    print("respose")
    print(response)
    Player_vsOrlando22_df = response.get_data_frames()
    print("Player_vsOrlando22_df")
    print(Player_vsOrlando22_df)
    Player_vsOrlando22_df = Player_vsOrlando22_df[0]
    Player_vsOrlando22_df.insert(0, 'VsTeam', 'vs.ORL')
except requests.exceptions.Timeout:
    print("TimeOut Occured")
