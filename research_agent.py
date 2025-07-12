# 1 we used import to bring the tools we need
import json  # we imported json to read the menu from the file "cafe_data.json"

# 2 we call our café agent who will load the file and let us ask questions
class ResearchAgent:
    def __init__(self, file_path):
        # This function runs automatically when we create a new ResearchAgent object
        # It stores the file path and loads the JSON data into memory
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        # This function tries to open the JSON file and load the data inside it
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)  # it reads the file and turns it into a Python dictionary
        except FileNotFoundError:
            # if the file isn't found, show an error message and return an empty dictionary
            print("File not found 😢")
            return {}

    # now we give the agent a skill to find ingredients of a specific item
    def get_ingredients(self, item):
        item = item.title()  # make sure the item name starts with a capital letter like in the file
        return self.data.get("menu", {}).get(item, {}).get("ingredients", None)

    # this function finds the calories of a drink
    def get_nutrition(self, item):
        item = item.title()
        return self.data.get("menu", {}).get(item, {}).get("nutrition", {}).get("calories", None)

    def get_nutrition(self, item):
        item = item.title()
        return self.data.get("menu", {}).get(item, {}).get("nutrition", {}).get("sugar_g", None)
    # this function finds the opening hours of a specific day
    def get_opening_hours(self, day):
        day = day.title()
        return self.data.get("opening_hours", {}).get(day, None)

    # this function returns the list of drinks from the file
    def get_available_drinks(self):
        return self.data.get("drinks", [])