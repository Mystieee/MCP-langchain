from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

#take input and return weather of specific location
@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the weather location
    """
    return "Its always rainy in dubai"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

'''
transport="streamable-http"
    this server will run on a particular host url.. http://localhost:8000

    it will run in the form  of api..

'''
