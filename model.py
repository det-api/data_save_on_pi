from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client['mydatabase']
collection = db['detailsales']

class DetailSale:
    def __init__(self, daily_report_id, vocono, nozzle_no, fuel_type, liter=0, amount=0, car_no=None, vehicle_type='car', start_point=0, end_point=0, create_at=None):
        self.daily_report_id = daily_report_id
        self.vocono = vocono
        self.nozzle_no = nozzle_no
        self.fuel_type = fuel_type
        self.liter = liter
        self.amount = amount
        self.car_no = car_no
        self.vehicle_type = vehicle_type
        self.start_point = start_point
        self.end_point = end_point
        self.create_at = create_at or datetime.now()

    def save(self):
        result = collection.insert_one(self.__dict__)
        return result.inserted_id

    @staticmethod
    def find_by_vocono(vocono):
        return collection.find_one({'vocono': vocono})

    def update(self, data):
        result = collection.update_one({'_id': self._id}, {'$set': data})
        return result.modified_count

    def delete(income):
        result = collection.delete_many(income)
        return result.deleted_count
    
    def find_by_daily_report_id(daily_report_id):
        return collection.find_one({'daily_report_id': daily_report_id})

    @staticmethod
    def find_all():
        return collection.find({})