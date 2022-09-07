from datetime import datetime
import math
from Opening import Opening
import berserk

session = berserk.TokenSession("lip_DcekuZBitKMSNtho2eJN")
client = berserk.Client(session=session)

start = berserk.utils.to_millis(datetime(2021, 9, 1))
end = berserk.utils.to_millis(datetime(2022, 6, 25))

games = list(
    client.games.export_by_player(
        'redchess656', 
        since=start, 
        until=end, 
        rated=True, 
        perf_type="rapid",
        opening=True,
        max=200)
    )

openingTable = {}
openingScore = {}
openingDepth = {}

for game in games:
    opening = game['opening']
    # print(opening)
    name = opening['name']
    if name not in openingTable:
        openingTable[name] = 0
        openingScore[name] = 0
        openingDepth[name] = 0

    openingTable[name] += 1
    openingDepth[name] = max(openingDepth[name], opening['ply'])

    if 'winner' in game:
        if game['players'][game['winner']]['user']['name']=='redchess656':
            openingScore[name] += 1 
        else:
            openingScore[name] -= 1 



# print("Freq table: ")
# print(openingTable)

# print("Depth table:")
# print(openingDepth)

# print("Score table:")
# print(openingScore)

weightedScores = {'' : 0}
runningMax = ''
runningMin = ''
openings = []
minDepth = 5

for key in openingTable.keys():
    weightedScore = openingScore[key] / openingTable[key] +  math.copysign(openingTable[key]/pow(10, len(str(openingTable[key]))), openingScore[key])
    weightedScores[key] = weightedScore

    if weightedScore > weightedScores[runningMax]:
        runningMax = key

    if weightedScore < weightedScores[runningMin]:
        runningMin = key

    openings.append(Opening(key, openingTable[key], openingScore[key], openingDepth[key], weightedScore))

openings = sorted(openings)

for i in range(len(openings)):
    opening = openings[i]
    print(i, " ", opening, " ", opening.depth, opening.weightedScore)
    
print("Best scored opening: ", runningMax, weightedScores[runningMax])
print("Worst scored opening: ", runningMin, weightedScores[runningMin])

# for i in range(10):
#     opening = openings[i]
#     print(i+1, " ", opening, " ", opening.depth)