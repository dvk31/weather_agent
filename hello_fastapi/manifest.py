{
    "name": "WeatherAgent",
    "description": "An AI agent that provides weather information and understands user intents related to weather queries.",
    "intents": {
        "weather_query": {"state": "weather", "function": "get_current_weather"}
    },
    "functions": [
        {
            "name": "get_current_weather",
            "api_url": "/get_current_weather/",
            "api_method": "POST",
            "parameters": {
                "type": "object",
                "required": ["location"],
                "properties": {
                    "unit": {"enum": ["celsius", "fahrenheit"], "type": "string"},
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                },
                "description": "Get the current weather in a given location",
                "ui_component": "WeatherCard",
            },
        },
        {
            "name": "extract_intent",
            "parameters": {
                "type": "object",
                "required": ["message", "manifest"],
                "properties": {
                    "message": {"type": "string", "description": "The user's message"},
                    "manifest": {
                        "type": "object",
                        "description": "The conversation manifest",
                    },
                },
            },
            "description": "Extract the intent from the user's message",
            "return_type": {"type": "string", "description": "The extracted intent"},
        },
    ],
    "ui_manifest": "https://your-server.com/ui_manifest.json",
    "welcome_message": "Hello! How can I assist you today?",
    "default_response": "I'm sorry, but I couldn't understand your request. Could you please provide more details or rephrase it?",
}
