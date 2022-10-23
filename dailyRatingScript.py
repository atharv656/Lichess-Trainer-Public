from datetime import date
import csv
import berserk

# Initialize lichess client
session = berserk.TokenSession("lip_DcekuZBitKMSNtho2eJN")
client = berserk.Client(session=session)
today = date.today().strftime("%m/%d/%y")

# Get the user's (redchess656) rapid rating today
rapid = client.users.get_by_id("redchess656")[0]['perfs']['rapid']

# Log the user's rating to a csv file for future analysis
with open('dailyLog.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([today, rapid['games'], rapid['rating']])