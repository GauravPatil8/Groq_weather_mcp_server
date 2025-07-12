from mcp.server.fastmcp import FastMCP
import httpx
import os
mcp = FastMCP("weather")
weather_api_key = os.getenv("WEATHER_API_KEY")
@mcp.tool()
async def get_weather(city: str):
    """Get the weather for a given city"""
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"
        )
        data = res.json()
        return {
            "location": data["location"]["name"],
            "temp_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"]
        }
if __name__ == "__main__":
    mcp.run(transport="streamable-http")