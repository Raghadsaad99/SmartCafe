SmartCafe Assistant – OOP Based Console Application ☕

📌 Project Overview:
SmartCafe Assistant is a beginner-friendly chatbot that runs in the terminal. It helps customers get quick answers about the café, such as:
- Ingredients of drinks
- Calories in menu items
- Opening hours for each day
- List of available drinks

This project uses **Object-Oriented Programming (OOP)** and a **JSON file** as its knowledge base. No internet or AI tools are used — just pure Python logic!

---

📁 Project Structure (Files):

1. `research_agent.py` – Handles all café data:
   - Loads data from `cafe_data.json`
   - Provides methods to get ingredients, calories, hours, and drinks

2. `chatbot_agent.py` – The chatbot that talks to the customer:
   - Greets the user
   - Understands questions using **regex**
   - Calls methods from `ResearchAgent`
   - Displays smart responses

3. `main.py` – The main file that runs the assistant:
   - Creates both agents
   - Starts the assistant using `assistant.run()`

4. `cafe_data.json` – The café’s menu and hours (required for the program to work)

---

🔍 How Regex is Used:
Regex helps the chatbot understand natural language. It searches for patterns in user input, such as:

- **Ingredients request**:  
  `what's in a Mocha?` → matches  
  `r"what'?s in (a |an )?(?P<item>[\w\s]+)"`

- **Calories**:  
  `how many calories in Hot Chocolate?`

- **Opening hours**:  
  `when are you open on Friday?`

- **Available drinks**:  
  `what drinks do you have?`

---

🧪 Sample Questions to Try:

- What's in a Hot Chocolate?
- How many calories in Mocha?
- What drinks do you have?
- When are you open on Monday?
- Exit (to quit)

---

✅ Notes:
- The `cafe_data.json` file must be in the same folder as the `.py` files.
- The code is written in simple, easy-to-read style with comments.
- The chatbot keeps running until the user types `exit` or `quit`.

---

🎬 Team Video Tips (if submitting):
- Each team member can explain one part: a class, method, or regex.
- Try to keep the explanation under 2 minutes.
- Bonus: Show a short demo with sample questions in the terminal!

(Optional: Add screenshots below if needed for submission.)

