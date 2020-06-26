from dotenv import load_dotenv
import urllib.request
import csv
import os
import json

def main():
    try:
        url = 'https://api.sportsdata.io/v3/csgo/scores/json/Teams'
        headers = {}
        headers['Ocp-Apim-Subscription-Key'] = os.getenv("KEY_CSGO_DATA_API")
        req = urllib.request.Request(url, headers= headers)
        resp = urllib.request.urlopen(req)

        respData = resp.read()
        encoding = resp.info().get_content_charset('utf8')
        data =json.loads(respData.decode(encoding))
        
        saveFile = open('teams.csv','w')      
        csvwriter = csv.writer(saveFile)
        count = 0
        for team in data:              
            if count == 0:
                header = team.keys()
                csvwriter.writerow(header)
            count += 1
            csvwriter.writerow(team.values())
        saveFile.close()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    load_dotenv()
    main()