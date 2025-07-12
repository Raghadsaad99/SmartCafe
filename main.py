from research_agent import ResearchAgent
from chatbot_agent import ChatBotAgent

# this is where the whole program starts
if __name__ == "__main__":
    researcher = ResearchAgent("cafe_data.json")  # we give the data file to the café agent
    assistant = ChatBotAgent(researcher)          # we give the researcher to the chatbot
    assistant.run()                               # and now the chatbot runs!
ـ   