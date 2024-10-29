import aiohttp
import asyncio
from datetime import datetime, timedelta

class ApiClient:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates"

    async def fetch_exchange_rates(self, date):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params={"date": date}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error fetching data: {response.status}")

async def fetch_rates(session, date):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
    try:
        async with session.get(url) as response:
            response_data = await response.json()
            if "exchangeRate" in response_data:
                rates = {}
                for rate in response_data["exchangeRate"]:
                    currency = rate["currency"]
                    if currency in ["EUR", "USD"]:
                        rates[currency] = {
                            "sale": rate.get("saleRate"),      
                            "purchase": rate.get("purchaseRate")  
                        }
                return {date: rates} if rates else None
            else:
                print(f"Unexpected response structure for {date}: {response_data}")
    except Exception as e:
        print(f"Failed to get rates for {date}: {e}")
    return None


    return rates
