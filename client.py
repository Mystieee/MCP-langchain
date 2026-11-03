#create mcp client:

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], #absolute path
                "transport": "stdio"
            },
            "weather":{
                "url": "http://localhost:8000/mcp", #ensure server is running here
                "transport":"streamable_http",

            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.environ["GROQ_API_KEY"]

    tools= await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-20b")
    agent=create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages":[{
            "role":"user",
            "content":"what is 2+2"
        }]}
    )

    print(f"Math response: ", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {
            "messages":[
                {"role": "user",
                 "content": "what is the weather in dubai"}
            ]
        }
    )
    print(f"Weather response: ", weather_response['messages'][-1].content)
    
asyncio.run(main())

# run weather.py and then client.py