import pandas as pd
from datetime import datetime
import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Get MongoDB URI securely
mongo_uri = os.getenv("MONGO_URI")


# Extract Data



# Get the URL
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"


# Get the URL 
response = requests.get(URL)


# Check the statuscode of the webAPI

print(response)


# Get the data from the web into json format
data = response.json()


print(data)

#Transform Data

records = []

for coin , price in data.items():
    records.append({
        "coin" : coin,
        "price_usd" : price["usd"],
        "timestamp" : datetime.now()
    })


# Create DataFrame
df = pd.DataFrame(records)

# Print DataFrame
print(df)



 # Load Data


 # Connect the MongoDB

client = MongoClient(mongo_uri)


# create  the DB

db = client["crypto_db"]
collection = db["crypto_prices"]

# Convert DataFrame to dictionary
data_to_insert = df.to_dict(orient="records")

# Insert into MongoDB
collection.insert_many(data_to_insert)

print("Data inserted into MongoDB!")