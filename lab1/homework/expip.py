from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
customers = db["customers"]

all_customers=customers.find()
eventscount = 0
adscount = 0
wobcount = 0
for customer in all_customers:
    if customer["ref"] == "events":
        eventscount = eventscount+1
    elif customer["ref"] == "ads":
        adscount = adscount+1
    elif customer["ref"] == "wob":
        wobcount = wobcount+1

print (eventscount, adscount, wobcount)

ref_counts = [eventscount, adscount, wobcount]
ref_names = ["EVENTS", "ADS", "WOB"]
pyplot.pie(ref_counts, labels = ref_names, autopct="%.1f%%", shadow=True, explode =[0, 0.2, 0])
pyplot.title("REF COUNT HAHAA")
pyplot.axis("equal")
pyplot.show()
