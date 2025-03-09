from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
if __name__ == "__main__":
    response = llm.invoke("give email for permission from my teacher for a leave , for my brothers marriage ")
    print(response.content)
