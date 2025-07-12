from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

import asyncio
async def main():
    client = MultiServerMCPClient(
        {
            "weather":{
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            },
        }
    )

    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    
    tools=await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(
        model,
        tools
    )

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user","content": "What is the weather in amritsar?"}]}
    )
    print(weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())





