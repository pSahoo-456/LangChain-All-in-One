from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_history=[]


while True:
    user_input=input("You:")
    chat_history.append(user_input)
    if user_input.lower()=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("Chatbot:",result.content)
print(chat_history)