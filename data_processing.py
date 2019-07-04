import pandas as pd
import numpy as np

list = ["Designated smoking area", "Refreshments", "Landscape features", "Guest item storage", "Dining",
        "Conference/Business", "Fitness centre/Gym", "Newspapers in lobby", "Porter/Bellhop",
        "Air-conditioning in public areas", "Pool", "Laundry", "Bar", "Live entertainment", "Connectivity/Devices",
        "On-site shopping", "Private event hosting", "Designated non-smoking area", "Front desk services",
        "Onsite parking", "Internet (Public areas)", "Transfers", "Security", "Lift", "Accessible property",
        "Housekeeping", "Babysitting/Childcare/Young ones", "Wellness centre/club", "Spa/Sauna", "Ticketing/Tours",
        "Cash services", "Wake-up service", "Social spaces", "Onsite car/limo rental", "Leisure/Entertainment",
        "Check-in/out", "Offsite parking", "Salon", "Indoor games", "Fireplace", "Ground sports facilities",
        "Medical service", "Sunbathing", "Smoking rooms available", "Bicycles", "Golf", "Multimedia loan",
        "Watersports activities", "Skiing", "Theme/water park", "Places of worship", "Tours and activities",
        "Welcome Drink Pack", "Gambling facilities", "Private beach", "business", "shopping", "urban", "family",
        "budget", "luxury", "romantic", "spaWellness", "gourmet", "design", "golf", "sport", "green", "wildlife",
        "rural", "adventure", "ski", "petFriendly", "boutique", "beach", "casino", "otherPolicy", "checkInOutPolicy",
        "petPolicy", "serviceAnimalPolicy", "Hotel", "Apartment", "Aparthotel", "Resort", "Villa", "Guesthouse",
        "Private vacation home", "Hostel", "Undefined", "Capsule hotels", "Lodge", "Condo", "Inn", "Motel",
        "Bed and breakfast", "americanExpress", "dinersClub", "jcbInternational", "mastercard", "visa", "creditCards",
        "carteBlanche", "discover", "maestro", "visaElectron", "unionPay", "cash"]

db = pd.read_csv('./db1.csv')

db_clone = [[], [], [], [], []]

for i, row in enumerate(db.values):
         print(row)


# a = np.array([[5, 6, 7, 8], [2, 3, 4, 3]])
# for x, i in np.nditer(a, order='C'):
#     print(type(i))

# a = np.arange(0,60,5)
# a = a.reshape(3,4)
#
# print(a)