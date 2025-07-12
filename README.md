# 🌤️ MCP Weather Temperature Server

This is a simple **MCP (Model Context Protocol)** server built using **Python**, **Langchain**, **LangGraph**, and **uv** that provides real-time weather temperature data using:

- **GROQ API** (for LLM-based query understanding)
- **WeatherAPI** (for real-time weather data)

---

## 🚀 Features

- Natural language queries like _"What's the weather in Tokyo?"_
- GROQ LLM parses the query
- WeatherAPI fetches the real-time data
- MCP handles structured agentic interaction

---

## 🛠️ Tech Stack

- `Python`
- `uv` (MCP server runner)
- `langchain`
- `langgraph`
- `dotenv`
- `GROQ API`
- `WeatherAPI`

---

## 🧪 Setup Instructions

1. **Clone this repository**

```bash
git clone https://github.com/yourusername/mcp-weather-server.git
cd mcp-weather-server
```

2. **Create a virtual environment (optional but recommended)**

```bash
uv venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
```

3. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

4. **Create a `.env` file in the root folder and add your API keys**

```dotenv
GROQ_API_KEY=your_groq_api_key_here
WEATHER_API_KEY=your_weatherapi_key_here
```
5. **Run the Weather server**
```bash
python weather_server.py
```

6.**Run the main file**
```
python main.py
```
## 📌 Notes

- Make sure your `.env` is correctly configured.
- The server won't start if the environment variables are missing or invalid.
- MCP-based servers are great for AI-native workflows. Feel free to extend this with LangGraph nodes for more complex weather workflows (e.g., 7-day forecast, alerts, etc).

