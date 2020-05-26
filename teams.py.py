from typing import TextIO

import pandas as pd
import requests
import sys

raw_data = pd.DataFrame([])

r = requests.get("https://api-nba-v1.p.rapidapi.com/teams/teamId/1",
                 headers={
                     "X-RapidAPI-Host": 'api-nba-v1.p.rapidapi.com',
                     "X-RapidAPI-Key": '40acb201c1msh6923fe20958813ap14e306jsn6069eeea5d5f'
                 }
                 )
data = r.json()
raw_data = pd.json_normalize(data)
teams_series = raw_data["api.teams"]
teams_list = teams_series[0]
teams_dict = teams_list[0]


teamId = teams_dict["teamId"]
city = teams_dict["city"]
shortName = teams_dict["shortName"]
fullName = teams_dict["fullName"]
logo = teams_dict["logo"]

for item in teams_dict:
    print(teams_dict[item])

file_object: TextIO = open(r"print.txt", "a+")
file_object.write(teamId)
file_object.write("\n")
file_object.write(city)
file_object.write("\n")
file_object.write(shortName)
file_object.write("\n")
file_object.write(fullName)
file_object.write("\n")
file_object.write(logo)
file_object.close()