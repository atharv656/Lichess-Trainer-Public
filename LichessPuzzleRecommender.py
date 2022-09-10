#Lichess Puzzle Recommender
import re
import LichessTest as lichess

def getLichessPuzzles(openingName):
    base_url = "https://lichess.org/training/"

    for i in range(len(openingName)):
        if openingName[i] == ",":
            break
    openingName = openingName[:i+1]
    openingSplit = re.split(":| ", openingName)

    # print(openingSplit)
    for word in openingSplit:
        word = "".join([letter if letter!="'" else "" for letter in word])
        if len(word) > 0:
            base_url += word + "_"

    return base_url[:-1]

def getPuzzles():
    white, black, ecoMap = lichess.scoreOpenings()
    whiteWorst = ecoMap[white[0].name]
    blackWorst = ecoMap[black[0].name]

    return (whiteWorst, getLichessPuzzles(whiteWorst)), (blackWorst, getLichessPuzzles(blackWorst))