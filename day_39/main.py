import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

def main():
    load_dotenv()

    home_iata = os.getenv("HOME_IATA", "DEL")
    months_ahead = int(os.getenv("SEARCH_MONTHS_AHEAD", "6"))
    min_nights = int(os.getenv("MIN_NIGHTS", "7"))
    max_nights = int(os.getenv("MAX_NIGHTS", "28"))

    data_manager = DataManager()
    flight_search = FlightSearch()
    notifier = NotificationManager()

    # 1) Get destinations from the sheet
    destinations = data_manager.get_destinations()

    # 2) Fill missing IATA codes
    for row in destinations:
        if not row.get("iataCode"):
            code = flight_search.get_iata(row["city"])
            if code:
                data_manager.update_iata_code(row["id"], code)
                row["iataCode"] = code
                print(f"✓ Filled IATA for {row['city']}: {code}")
            else:
                print(f"⚠️  Could not find IATA for {row['city']}")

    # 3) Search flights and notify when cheaper than target
    for row in destinations:
        dest_code = row["iataCode"]
        target_price = float(row["lowestPrice"])

        if not dest_code:
            continue

        result = flight_search.search_flight(
            fly_from=home_iata,
            fly_to=dest_code,
            months_ahead=months_ahead,
            nights_in_dst_from=min_nights,
            nights_in_dst_to=max_nights
        )

        if not result:
            print(f"— No results for {row['city']} ({dest_code})")
            continue

        price = float(result["price"])
        if price <= target_price:
            msg = (
                f"✈️ Low price alert! {flight_search.currency} {price} from "
                f"{result['origin_city']} ({result['origin_airport']}) to "
                f"{result['destination_city']} ({result['destination_airport']}).\n"
                f"Dates: {result['out_date']} → {result['return_date']}\n"
                f"Deal: {result['deep_link'] or '(open Kiwi app/site)'}"
            )
            notifier.send_sms(msg)
        else:
            print(f"Price too high for {row['city']}: found {flight_search.currency} {price} (limit {target_price})")

if __name__ == "__main__":
    main()
