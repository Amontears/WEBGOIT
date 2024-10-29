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

async def get_daily_rates(api_client: ApiClient, days: int):
    rates = {}
    for day in range(days):
        date = (datetime.now() - timedelta(days=day)).strftime('%d.%m.%Y')  
        daily_rates = await api_client.fetch_exchange_rates(date)

        if daily_rates and "exchangeRate" in daily_rates:
            rates[date] = {
                rate["currency"]: {
                    "sale": rate.get("saleRate"),
                    "purchase": rate.get("purchaseRate")
                }
                for rate in daily_rates["exchangeRate"]
                if rate["currency"] in ["EUR", "USD"]  
            }
    return rates
