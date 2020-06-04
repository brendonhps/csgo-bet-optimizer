import urllib.request
import datetime
import json
import csv

def set_datetime(time):
  start = datetime.datetime.strptime(time[0], "%Y-%m-%d")
  end = datetime.datetime.strptime(time[1], "%Y-%m-%d")
  date_generated = [(start+datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, (end-start).days)]
  return date_generated

def main():
  try:
    url = 'https://api.sportsdata.io/v3/csgo/scores/json/GamesByDate/'
    time = "2020-06-03", "2020-06-04"
    headers = {}
    headers['Ocp-Apim-Subscription-Key'] = "6abbd4e99e494e3d90edaaa48284ed82"
    dates = set_datetime(time)
    count = 0
    for date in dates:
      req = urllib.request.Request(url+str(date), headers= headers)
      resp = urllib.request.urlopen(req)
      
      respData = resp.read()
      encoding = resp.info().get_content_charset('utf8')
      data =json.loads(respData.decode(encoding))
      
      saveFile = open('games_bydate.csv','a+')      
      csvwriter = csv.writer(saveFile)
      for game in data:              
        if count == 0:
          header = game.keys()
          csvwriter.writerow(header)
          count += 1
        csvwriter.writerow(game.values())
      saveFile.close()
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  main()