from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-specdec")
if __name__ == "__main__":
    response = llm.invoke("Create a email for my manager for asking leave due to fever ")
    print(response.content)
