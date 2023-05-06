from model import DetailSale
from datetime import datetime


def create_detail_sale(data):
    detail_sale = DetailSale(**data)
    return detail_sale.save()

def read_detail_sale(vocono):
    detail_sale = DetailSale.find_by_vocono(vocono)
    return detail_sale

def all_detail_sale():
    detail_sales = DetailSale.find_all()
    detail_sales_list = list(detail_sales)
    return detail_sales_list

def update_detail_sale(vocono, data):
    detail_sale = DetailSale.find_by_vocono(vocono)
    return detail_sale.update(data)

def delete_detail_sale(vocono):
    detail_sale = DetailSale.find_by_vocono(vocono)
    if detail_sale:
        DetailSale.delete(detail_sale._id)
    else:
        return 0


def delete_By_id(id = {}) :
    detail_sale = DetailSale.delete(id)
    print(detail_sale)
    if detail_sale:
       return 1
    else:
        return 0

obj = {
    "daily_report_id": "1234",
    "vocono": "ABC123",
    "car_no": None,
    "vehicle_type": "car",
    "nozzle_no": 1,
    "fuel_type": "gasoline",
    "liter": 10,
    "amount": 100,
    "create_at": datetime.utcnow()
}
# create_detail_sale(obj)
# 6455d5a036cae0e22076bdeb
# print(delete_detail_sale('ABC123'))
# print(all_detail_sale())
# print(delete_By_id())



