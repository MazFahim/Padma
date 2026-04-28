from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["padma"]
portfolio_collection = db["portfolio"]

def get_portfolio():
    data = portfolio_collection.find_one({}, {"_id": 0})
    if not data:
        data = {"type": "portfolio", "freelancing": [], "trading": []}
        portfolio_collection.insert_one(data)
    else:
        updated_fields = {}
        if "freelancing" not in data:
            updated_fields["freelancing"] = []
        if "trading" not in data:
            updated_fields["trading"] = []
        if updated_fields:
            portfolio_collection.update_one({"_id": data["_id"]}, {"$set": updated_fields})
            data.update(updated_fields)
    return data


def add_portfolio_item(category, item):
    portfolio_collection.update_one({}, {"$push": {category: item}}, upsert=True)


def update_portfolio_item(category, old_item, new_item):
    portfolio_collection.update_one({}, {
        "$set": {f"{category}.$[elem]": new_item}
    }, array_filters=[{"elem": old_item}])


def delete_portfolio_item(category, item):
    portfolio_collection.update_one({}, {"$pull": {category: item}})
