from datetime import datetime, date
import math
from Opening import Opening
import berserk

def sortOpenings(games):
    #Create frequency table of openings, win/loss rate and depth
    openingTable = {}
    openingScore = {}
    openingDepth = {}
    ecoMap = {}

    for game in games:
        opening = game['opening']
        # print(opening)
        name = opening['eco']
        if name not in openingTable:
            openingTable[name] = 0
            openingScore[name] = 0
            openingDepth[name] = 0
            ecoMap[name] = opening['name']

        openingTable[name] += 1
        openingDepth[name] = max(openingDepth[name], opening['ply'])

        if 'winner' in game:
            if game['players'][game['winner']]['user']['name']=='redchess656':
                openingScore[name] += 1 
            # else:
            #     openingScore[name] -= 1 
        else:
            openingScore[name] += 0.5


    #Create a score for each opening based on its win/loss rate and depth
    weightedScores = {'max' : 0, 'min' : 1}
    runningMax = 'max'
    runningMin = 'min'
    openings = []
    minDepth = 5

    for key in openingTable.keys():
        if openingTable[key] < minDepth:
            continue
        weightedScore = openingScore[key] / openingTable[key]
        weightedScores[key] = weightedScore

        if weightedScore > weightedScores[runningMax]:
            runningMax = key

        if weightedScore < weightedScores[runningMin]:
            runningMin = key

        #Store the data in an opening object
        openings.append(Opening(key, openingTable[key], openingScore[key], openingDepth[key], weightedScore))

    #Sort the openings by weighted score
    return sorted(openings), ecoMap

def scoreOpenings():
    #Set up api
    session = berserk.TokenSession("lip_DcekuZBitKMSNtho2eJN")
    client = berserk.Client(session=session)

    #Load last 20 games
    today = str(date.today()).split("-")
    today = [int(num) for num in today]

    start = berserk.utils.to_millis(datetime(2022, 1, 1))
    end = berserk.utils.to_millis(datetime(today[0], today[1], today[2]))

    whiteGames = list(
        client.games.export_by_player(
            'redchess656', 
            since=start, 
            until=end, 
            rated=True, 
            perf_type="rapid",
            color="white",
            opening=True,
            max=100)
        )

    blackGames = list(
        client.games.export_by_player(
            'redchess656', 
            since=start, 
            until=end, 
            rated=True, 
            perf_type="rapid",
            color="black",
            opening=True,
            max=100)
        )

    white, whiteEco = sortOpenings(whiteGames)
    black, blackEco = sortOpenings(blackGames)
    whiteEco.update(blackEco)

    return(white, black, whiteEco)

# Testcase prints
# white, black, ecoMap = scoreOpenings()
# print(ecoMap[white[0].name], ecoMap[black[0].name])

#Print the best/worst openings
# for i in range(len(white)):
#     opening = white[i]
#     print(i, " ", opening, " ", ecoMap[opening.name], " ", opening.depth, opening.weightedScore)
    
# print("Best scored opening: ", white[-1])
# print("Worst scored opening: ", white[0])

# for i in range(len(black)):
#     opening = black[i]
#     print(i, " ", opening, " ", ecoMap[opening.name], " ", opening.depth, opening.weightedScore)
    
# print("Best scored opening: ", black[-1])
# print("Worst scored opening: ", black[0])