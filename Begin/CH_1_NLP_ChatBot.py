# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the ChatBot class for interaction.
class ChatBot():
    def __init__(self):
        # Analyzing the sentiment of the user's message.
        self.sentiment_analyzer = TextBlob("")  
    def start_chat(self):
        print("Chatbot Hi How can I help U?")
        while True:
            user_message=input("You: ").strip()

            self.sentiment_analyzer=TextBlob(user_message)
            sentiment_score=self.sentiment_analyzer.sentiment.polarity

            # Generating the chatbot's response based on sentiment.
            if sentiment_score>0:
                chatbot_message=f"Chatbot That's great to hear! \n Sentiment Score: {sentiment_score}\n "
            elif sentiment_score<0:
                chatbot_message=f"Chatbot: I'm sorry to hear that,would you like me to transfer you to a live agent \n Sentimate Score:{sentiment_score}\n"
            else:
                  chatbot_message=f"Chatbot: Hmm I see, Can you please provide more information? \n Sentimate Score:{sentiment_score}\n"
              

            # Printing the chatbot's response and sentiment.

            print(chatbot_message)
          


if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = ChatBot()
    chatbot.start_chat()
