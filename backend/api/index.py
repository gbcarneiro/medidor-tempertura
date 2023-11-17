from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta, timezone 
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

password = "7vQXczaDesdGeJYb"

mongo_uri = f"mongodb+srv://gabrielcarneiro:{password}@cluster0.qfs6xtz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

db = client["teste"]
collection = db["temperature"]

@app.route('/add/temperature', methods=['POST'])
@cross_origin()
def add_temperature(): 
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        timestamp = datetime.now(timezone.utc)
        time_exchange = timedelta(hours=-3)
        time_zone = timezone(time_exchange)

        timestamp_brazil = timestamp.astimezone(time_zone)
        date = timestamp_brazil.strftime("%d/%m/%Y")
        hour = timestamp_brazil.strftime("%H:%M")

        data = {
            "temperatura": json['temperature'],
            "date": date,
            "hour": hour
        }
        result = collection.insert_one(data)
        return jsonify({"success": True, "message": "Document inserted successfully", "id": str(result.inserted_id)})

    
@app.route('/get/temperature', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_temperature():
    recent_document = collection.find_one(sort=[("_id", -1)])

    return jsonify({
        "temperature": recent_document.get("temperatura"),
        "date": recent_document.get("date"),
        "hour": recent_document.get("hour")
    })

@app.route('/get/temperature/avarage', methods=['POST'])
@cross_origin()
def get_temperature_avarage():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        target_date = datetime(2023, 11, 16)

        # Define the start and end of the day
        start_of_day = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = target_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Construct the query to fetch data for the specified day
        query = {
            "timestamp": {
                "$gte": start_of_day,
                "$lt": end_of_day
            }
        }

        # Fetch data from MongoDB based on the query
        data_for_specific_day = list(collection.find(query, {"_id": 0}))

        print(data_for_specific_day)

        return 'foi'