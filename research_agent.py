import json  # we imported json to read the menu from the file "cafe_data.json"

# We define a class to represent our café agent
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
                return json.load(file)  # Reads the file and turns it into a Python dictionary
        except FileNotFoundError:
            print("File not found 😢")
            return {}

    # Finds the ingredients of a specific item
    def get_ingredients(self, item):
        item = item.title()
        return self.data.get("menu", {}).get(item, {}).get("ingredients", None)

    # Finds the calories of a specific item
    def get_calories(self, item):
        item = item.title()
        return self.data.get("menu", {}).get(item, {}).get("nutrition", {}).get("calories", None)

    # Finds the sugar content (in grams) of a specific item
    def get_sugar(self, item):
        item = item.title()
        return self.data.get("menu", {}).get(item, {}).get("nutrition", {}).get("sugar_g", None)

    # Returns the full weekly opening hours
    def get_all_opening_hours(self):
        return self.data.get("opening_hours", {})

    # Returns opening hours for a specific day
    def get_opening_hours_by_day(self, day):
        day = day.title()
        return self.data.get("opening_hours", {}).get(day, None)

    # Returns the list of drink names
    def get_drinks_names(self):
        
        return self.data.get("drinks", [])
