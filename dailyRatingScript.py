from datetime import date
import csv
import berserk

log = open('dailyLog.csv', 'w+')
writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

session = berserk.TokenSession("lip_DcekuZBitKMSNtho2eJN")
client = berserk.Client(session=session)
today = date.today().strftime("%m/%d/%y")
rapid = client.users.get_by_id("redchess656")[0]['perfs']['rapid']
writer.writerow([today, rapid['games'], rapid['rating']])

log.close()