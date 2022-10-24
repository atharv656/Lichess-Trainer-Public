# Chess Trainer

## Note: 
In order to keep the discord key private, I have cloned this repository and deleted the discord bot token from discordbot.py — all the rest of the code is identical and when a valid discord bot token is used, the code would run identically to my private repo 

## Inspiration
My dad taught me and my brother how to play chess when we were just kids. At first, the only opening I knew was the 4-move checkmate and after my brother learned a few openings of his own, including one that countered my 4-move mate, I realized I need to expand my repertoire. But learning chess openings is hard—it requires research and studying to memorize a precise sequence of moves that can only be used if your opponent plays into it. I never found this interesting, so I didn’t get back into chess until very recently. I’ve gotten much better at chess since then, but I’ve still never bothered to learn openings and in an effort to justify my stubbornness, this became my focus in the API Challenge. 

## Process and Description
I started off by finding an API that let me get data on all of the online games I’ve played on Lichess—using the Lichess API let me find data on every detail of my games, including my best and worst openings. After sorting my openings by win percentage, I realized Lichess also has a puzzle bank that can be sorted by opening—you can get tactics that occurred in games that started off with the same sequence of moves. This prompted me to try reverse engineering how Lichess builds the url for puzzles in a specific opening so that my python script could take my 2 worst openings and spit out links that would help me improve in these openings. After this worked, I realized it would be much more convenient if I received these links as a notification on a daily basis (rather than having to run my script and copy/paste the links it outputted) and so I learned how to use the Discord API as well as Github Actions to run my discord bot every morning. Now, every morning my bot looks at the last 100 games I’ve played, finds my worst scoring Openings in them, and sends me puzzles to help! <br />
<br />
Now, I've made a Discord Channel where people can join and provide their Lichess account to the bot. Every morning (using GitHub Actions), the bot will go through the list of lichess accounts, scrape their last 100 games, and send them a Lichess tactics link personalized to their worst scoring openings for White and Black.


## Future Goals
This project was initially meant for me to improve my chess game. It was originally just the LichessHandler.py file which I would run in terminal and then look up tactics for manually. I ralized if I wanted to use this regularly or for my friends to be able to try it out I'd need to make a more robust UI, so I developed the Discord Bot and used GitHub Actions to send the tactics daily. I also created a Discord Guild where others can join and gain access to the bot. I am currently developing editing a couple things to make the bot fully usable for others as well including: <br />
- Removing the hardcoded username in dailyRatingScript.py to loop through all users in the userList.pkl to log every users rating data
- Add an actual backend to store the rating data, rather than storing it in this Github repo
- Check when the link has been clicked/tactics have been played and log this by user (to make sure any trends found are accurate)
- Build graphs/analysis from the logged data to see if it is actually helping
- Check if the window of games played (or any other variables) should be changed

## Video of it Running
