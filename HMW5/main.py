import asyncio
import sys
from currency_rates import ApiClient, get_daily_rates
from colorama import Fore, Style

async def main():
    if len(sys.argv) < 2:
        print("Укажите количество дней.")
        return
    
    try:
        days = int(sys.argv[1])  # Преобразуем аргумент в целое число
    except ValueError:
        print("Количество дней должно быть целым числом.")
        return

    api_client = ApiClient()
    rates = await get_daily_rates(api_client, days)

    # Сохраняем данные в файл
    with open('exchange_rates.txt', 'w', encoding='utf-8') as file:
        for date, values in rates.items():
            file.write(f"Дата: {date}\n")
            for currency, rate_info in values.items():
                file.write(f"  {currency}:\n")
                file.write(f"    Продажа: {rate_info['sale']}\n")
                file.write(f"    Покупка: {rate_info['purchase']}\n")
            file.write("=" * 40 + "\n")

    # Выводим данные на экран с цветами
    for date, values in rates.items():
        print(f"{Fore.GREEN}Дата: {date}{Style.RESET_ALL}")
        for currency, rate_info in values.items():
            print(f"  {currency}:")
            print(f"    {Fore.MAGENTA}Продажа: {rate_info['sale']}{Style.RESET_ALL}")
            print(f"    {Fore.MAGENTA}Покупка: {rate_info['purchase']}{Style.RESET_ALL}")
        print("=" * 40)

if __name__ == "__main__":
    asyncio.run(main())
