#Lichess Puzzle Recommender
import re
import LichessHandler as lichess

# Turn an opening name string into a lichess puzzle link in that opening
def getLichessPuzzles(openingName):
    # Special character checker
    def specialChar(c):
        return c == "'" or c == ","

    # Turn a formatted opening name into a link
    def splitToUrl(base_url, openingSplit):
        for word in openingSplit:
            # Join the words with a dash and removing special characters
            word = "".join([letter if not specialChar(letter) else "" for letter in word])
            if len(word) > 0:
                base_url += word + "_"
        return base_url[:-1]

    base_url = "https://lichess.org/training/"
    openingSplit = re.split(":| ", openingName)

    url = splitToUrl(base_url, openingSplit)
    r = requests.head(url)
    i=1
    
    # If the url is not valid, try removing the last word until it is valid
    # If the opening is not found at all, the base_url is returned
    # In many cases, the opening variation is too specific, but a more general opening is found
    while r.status_code != requests.codes.ok and url != base_url:
        # print(url)
        url = splitToUrl(base_url, openingSplit[:-i])
        i+=1
        r = requests.head(url)

    return url

def getPuzzles():
    # Sort users openings by games won and pick out the worst openings for white and black
    white, black, ecoMap = lichess.scoreOpenings()
    whiteWorst = ecoMap[white[0].name]
    blackWorst = ecoMap[black[0].name]

    # Get the lichess puzzle links for the worst openings
    return (whiteWorst, getLichessPuzzles(whiteWorst)+"/white"), (blackWorst, getLichessPuzzles(blackWorst)+"/black")


# For testing
def main():
    puzzles = getPuzzles()
    print(puzzles)

if __name__ == "__main__":
    main()