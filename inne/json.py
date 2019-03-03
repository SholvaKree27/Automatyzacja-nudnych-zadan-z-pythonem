import json
import requests

response = requests.get("https://games.crossfit.com/competitions/api/v1/competitions/open/2019/leaderboards?division=1&region=0&scaled=0&sort=0&occupation=0&page=1")
open19 = json.loads(response.text)

open19 == response.json()
type(open19)

n = 0
for x in open19["leaderboardRows"][n]["entrant"]["height"]:
    print(open19["leaderboardRows"][0]["entrant"]["competitorName"],open19["leaderboardRows"][n]["entrant"]["height"],open19["leaderboardRows"][n]["scores"][0]["scoreDisplay"])
    n = n+1
