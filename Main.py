import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load .env variables
load_dotenv()

# Create model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Send prompt
response = llm.invoke(
    [HumanMessage(content="Explain LangChain in simple words.")]
)

# Print response
print("\nAI Response:\n")
print(response.content)