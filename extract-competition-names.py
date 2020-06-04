from dotenv import load_dotenv
import urllib.request
import json
import csv
import os


def main():
  try:
    url = 'https://api.sportsdata.io/v3/csgo/scores/json/Competitions'
    headers = {}
    headers['Ocp-Apim-Subscription-Key'] = os.getenv("KEY_CSGO_DATA_API")
    count = 0
    
    req = urllib.request.Request(url, headers= headers)
    resp = urllib.request.urlopen(req)
    
    respData = resp.read()
    encoding = resp.info().get_content_charset('utf8')
    data =json.loads(respData.decode(encoding))
    
    saveFile = open('competitions.csv','a+')      
    csvwriter = csv.writer(saveFile)
    for competition in data:              
        if count == 0:
            header = [competition['CompetitionId'],competition['AreaId'], competition['Name'], competition['Gender'],competition['Type'],'SeasonId','RoundId']
            csvwriter.writerow(header)
            count += 1
        for season in competition['Seasons']:
            for seasonRound in season['Rounds']:
                csvwriter.writerow([competition['CompetitionId'],competition['AreaId'], competition['Name'], competition['Gender'],competition['Type'],season['SeasonId'],seasonRound['RoundId']])
    saveFile.close()
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  load_dotenv()
  main()