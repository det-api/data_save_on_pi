# MODEL
import pymongo

class MyModel:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.col = self.db["mycollection"]

    def create(self, data):
        self.col.insert_one(data)

    def read(self, query):
        return self.col.find_one(query)

    def update(self, query, new_values):
        self.col.update_one(query, new_values)

    def delete(self, query):
        self.col.delete_one(query)


# VIEW
class MyView:
    def get_input(self, message):
        return input(message)

    def display_output(self, message):
        print(message)


# CONTROLLER
class MyController:
    def __init__(self):
        self.model = MyModel()
        self.view = MyView()

    def create(self):
        name = self.view.get_input("Enter name: ")
        age = self.view.get_input("Enter age: ")
        data = {"name": name, "age": age}
        self.model.create(data)
        self.view.display_output("Record created successfully")

    def read(self):
        name = self.view.get_input("Enter name to search: ")
        query = {"name": name}
        result = self.model.read(query)
        if result:
            self.view.display_output(f"Name: {result['name']}, Age: {result['age']}")
        else:
            self.view.display_output("Record not found")

    def update(self):
        name = self.view.get_input("Enter name to update: ")
        age = self.view.get_input("Enter new age: ")
        query = {"name": name}
        new_values = {"$set": {"age": age}}
        self.model.update(query, new_values)
        self.view.display_output("Record updated successfully")

    def delete(self):
        name = self.view.get_input("Enter name to delete: ")
        query = {"name": name}
        self.model.delete(query)
        self.view.display_output("Record deleted successfully")


# MAIN PROGRAM
def main():
    controller = MyController()

    while True:
        action = input("Enter action (create/read/update/delete): ")
        if action == "create":
            controller.create()
        elif action == "read":
            controller.read()
        elif action == "update":
            controller.update()
        elif action == "delete":
            controller.delete()
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
