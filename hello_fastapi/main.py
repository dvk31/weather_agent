from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()


class WeatherResponse(BaseModel):
    location: str
    temperature: float
    unit: str


@app.post("/get_current_weather/", response_model=WeatherResponse)
async def get_current_weather(
    location: str = Query(
        ..., description="The city and state, e.g., San Francisco, CA"
    ),
    unit: str = Query(
        "celsius", enum=["celsius", "fahrenheit"], description="The temperature unit"
    ),
):
    # In a real-world scenario, fetch real weather data here.
    hardcoded_data = {
        "San Francisco, CA": {"temperature": 20.0, "unit": "celsius"},
        "New York, NY": {"temperature": 15.0, "unit": "celsius"},
    }

    weather_data = hardcoded_data.get(location)
    if not weather_data:
        raise HTTPException(status_code=404, detail="Location not found")

    if unit == "fahrenheit":
        weather_data["temperature"] = weather_data["temperature"] * 9 / 5 + 32
        weather_data["unit"] = "fahrenheit"

    return {
        "location": location,
        "temperature": weather_data["temperature"],
        "unit": weather_data["unit"],
    }
