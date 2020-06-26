from dotenv import load_dotenv
import urllib.request
import pandas as pd 
import csv
import json
import os

def get_team():
    df = pd.read_csv('teams.csv')
    
    return list(df["TeamId"])

def main():
      try:
        url = 'https://api.sportsdata.io/v3/csgo/scores/json/PlayersByTeam/'        
        headers = {}
        headers['Ocp-Apim-Subscription-Key'] = os.getenv("KEY_CSGO_DATA_API")
        count = 0
        teams = get_team()
        for team in teams:
            req = urllib.request.Request(url+str(team), headers= headers)
            resp = urllib.request.urlopen(req)
        
            respData = resp.read()
            encoding = resp.info().get_content_charset('utf8')
            data = json.loads(respData.decode(encoding))
        
            saveFile = open('players.csv','a+')      
            csvwriter = csv.writer(saveFile)
        
            for player in data:              
                if count == 0:
                    header = player.keys()
                    csvwriter.writerow([*(header), "TeamId"])
                count += 1
                values = player.values()
                csvwriter.writerow([*(values), team])
            saveFile.close()
      except Exception as e:
            print(str(e))

if __name__ == "__main__":
    load_dotenv()
    main()