# Chess Trainer

Bot to assist with chess progress. In an attempt to "seriously" start learning openings, this bot evaluates the previous games played, ranks the openings by how well I play them. It then finds the opening with the lowest win percentage for both white and black. Lichess Puzzles (Tactics) can be sorted based on the opening that they came out of, so the bot then builds a link to a library of Lichess Puzzles based out of my worst 2 openings. These link is then sent via Discord Bot to me every morning.

## Goals
This project was initially meant for me to improve my chess game. It was originally just the LichessHandler.py file which I would run in terminal and then look up tactics for manually. I ralized if I wanted to use this regularly or for my friends to be able to try it out I'd need to make a more robust UI, so I developed the Discord Bot and used GitHub Actions to send the tactics daily. I also created a Discord Guild where others can join and gain access to the bot. I am currently developing editing a couple things to make the bot usable for others as well including: <br />
- Removing the hardcoded username in dailyRatingScript.py to loop through all users in the userList.pkl to log every users rating data
- Add an actual backend to store the rating data, rather than storing it in this Github repo
- Check when the link has been clicked/tactics have been played and log this by user (to make sure any trends found are accurate)
- Build graphs/analysis from the logged data to see if it is actually helping
- Check if the window of games played (or any other variables) should be changed