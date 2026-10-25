from hko_api import HKOClient

def display_hk_weather():
    # Instantiate client in Traditional Chinese ('tc') as requested
    client = HKOClient(lang="tc")
    
    try:
        print("=" * 45)
        print("         香港天文台 - 即時天氣報告         ")
        print("=" * 45)
        
        current_data = client.get_current_weather()
        
        # Extract temperature
        temp_data = current_data.get("temperature", {}).get("data", [])
        hk_spot_temp = next((item for item in temp_data if item["place"] == "香港天文台"), None)
        temp_val = hk_spot_temp["value"] if hk_spot_temp else "N/A"
        
        # Extract humidity
        humidity_data = current_data.get("humidity", {}).get("data", [])
        humidity_val = humidity_data[0]["value"] if humidity_data else "N/A"

        print(f"🌡️  天文台氣溫: {temp_val}°C")
        print(f"💧 相當相對濕度: {humidity_val}%")
        
        # Display active warnings summary if available
        warnings = client.get_weather_warnings()
        print("\n⚠️  現正生效的警告:")
        if warnings:
            for code, warning in warnings.items():
                print(f" - {warning.get('name')}")
        else:
            print(" - 目前沒有特別天氣警告")

        # Display forecast overview
        forecast_data = client.get_weather_forecast()
        general_forecast = forecast_data.get("generalSituation", "無資料")
        print("\n📅 天氣概況:")
        print(f" {general_forecast}")

        print("=" * 45)

    except Exception as e:
        print(f"無法取得天氣資料: {e}")

if __name__ == "__main__":
    display_hk_weather()