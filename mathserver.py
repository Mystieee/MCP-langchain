from mcp.server.fastmcp import FastMCP

#initialize
mcp=FastMCP("Math") #server name

#add doc string so that mcp will understand which tool to use
@mcp.tool()
def add(a:int, b:int)-> int:
    """
    _summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def subtract(a:int, b:int) -> int:
    """
    _summary_
    Subtract two numbers
    """
    return a-b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """
    _summary_
    multiply two numbers
    """
    return a*b


#run this file:
if __name__ == "__main__":
    mcp.run(transport="stdio") #transport: stdio -->


'''
The transport="stdio" argument tells the server to:
Use standard input/output(stdin and stdout) to receive and respond
to tool function calls.
'''