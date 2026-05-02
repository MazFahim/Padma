from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["padma"]
cdst_collection = db["CDSt"]

def get_tracker_rows():
    doc = cdst_collection.find_one({"name": "CDSt"})
    return doc["D"]["rows"]


def update_tracker_row(category, last_stage, next_stage):
    cdst_collection.update_one(
        {"name": "CDSt", "D.rows.category": category},
        {"$set": {"D.rows.$.last_stage": last_stage, "D.rows.$.next_stage": next_stage}}
    )


def get_wishlist():
    doc = db["CDSt"].find_one({"name": "CDSt"})
    return doc["D"]["wishlist"]


def add_wish(category, wish):
    db["CDSt"].update_one(
        {"name": "CDSt", "D.wishlist.category": category},
        {"$push": {"D.wishlist.$.wishes": wish}}
    )


def delete_wish(category, wish):
    db["CDSt"].update_one(
        {"name": "CDSt", "D.wishlist.category": category},
        {"$pull": {"D.wishlist.$.wishes": wish}}
    )


def update_wish(category, old_wish, new_wish):
    delete_wish(category, old_wish)
    add_wish(category, new_wish)