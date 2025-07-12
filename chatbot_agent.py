import re    # we imported re (regular expressions) to understand what the customer is asking by analyzing patterns in their sentence

# now we create our chatbot agent — the one who talks to the customer
class ChatBotAgent:
    def __init__(self, researcher):
        # this connects the chatbot with the ResearchAgent class
        self.researcher = researcher

    # now we welcome the user and show them the drinks
    def greet_user(self):
        print("👋 Welcome to SmartCafe Assistant!")
        print("Ask me anything about our drinks, ingredients, or hours.")
        print("Type 'exit' or 'quit' to end the chat.\n")
        drinks = self.researcher.get_available_drinks()
        print("🥤 Available drinks:")
        for drink in drinks:
            print(f" - {drink}")

    # this keeps the chatbot running in a loop until the user types exit
    def run(self):
        self.greet_user()  # show the welcome message

        while True:
            user_input = input("🗨️ You: ").strip().lower()

            if user_input in ['exit', 'quit']:
                print("👋 Goodbye! Have a great day!")
                break  # stop the chatbot

            self.handle_query(user_input)  # check what the user wants

    # here the chatbot tries to understand the question and give the answer
    def handle_query(self, user_input):
        # if the user is asking "what's in a ___"
        if match := re.search(r"what'?s in (a |an )?(?P<item>[\w\s]+)", user_input):
            item = match.group("item")
            ingredients = self.researcher.get_ingredients(item)
            if ingredients:
                print(f"✅ Ingredients in {item.title()}: {', '.join(ingredients)}")
            else:
                print("❌ Sorry, I couldn't find that item.")

        # if the user is asking "how many calories in ___"
        elif match := re.search(r"how many calories in (?P<item>[\w\s]+)", user_input):
            item = match.group("item")
            calories = self.researcher.get_nutrition(item)
            if calories:
                print(f"🔥 {item.title()} has {calories} calories.")
            else:
                print("❌ Sorry, I couldn't find that item's nutrition info.")
        elif match := re.search(r"how much sugar in (?P<item>[\w\s]+)", user_input):
            item = match.group("item")
            sugar_g = self.researcher.get_nutrition(item)
            if sugar_g:
                print(f"🔥 {item.title()} has {sugar_g} sugar.")
            else:
                print("❌ Sorry, I couldn't find that item's nutrition info.")


        # if the user is asking "when are you open on ___"
        elif match := re.search(r"when (are|do) you open on (?P<day>\w+)", user_input):
            day = match.group("day")
            hours = self.researcher.get_opening_hours(day)
            if hours:
                print(f"🕒 On {day.title()}, we’re open: {hours}")
            else:
                print("❌ Sorry, I don't have info for that day.")

        # if the user is asking "what drinks do you have"
        elif re.search(r"what drinks (do you have|are available)", user_input):
            drinks = self.researcher.get_available_drinks()
            print("🥤 Our available drinks:")
            for drink in drinks:
                print(f" - {drink}")

        # if we don’t understand the question
        else:
            print("🤖 I'm not sure how to answer that. Try asking about drinks, ingredients, calories, or hours.")