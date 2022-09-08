from datetime import date
import csv
import berserk

session = berserk.TokenSession("lip_DcekuZBitKMSNtho2eJN")
client = berserk.Client(session=session)
today = date.today().strftime("%m/%d/%y")
rapid = client.users.get_by_id("redchess656")[0]['perfs']['rapid']
# writer.writerow([today, rapid['games'], rapid['rating']])
with open('dailyLog.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["ahhh", "WTF", "BITCHHHH"])