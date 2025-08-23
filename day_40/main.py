import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

def prompt_new_user(data_manager: DataManager):
    print("Welcome to Flight Club.")
    print("We find the best flight deals and email you.")
    join = input("Do you want to join the club? (y/n): ").strip().lower()
    if join == "y":
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        email = input("Email: ").strip()
        if first and last and email:
            data_manager.add_user(first, last, email)
            print("🎉 You're in! You'll start receiving deals soon.")
        else:
            print("⚠️ Skipped signup (missing information).")

def main():
    load_dotenv()

    data_manager = DataManager()
    flight_search = FlightSearch()
    notifier = NotificationManager()

    # 1) Optional: let a new user join from CLI
    prompt_new_user(data_manager)

    # 2) Get destinations (prices tab)
    try:
        destinations = data_manager.get_destinations()
    except Exception as e:
        print(f"❌ Could not fetch destinations from Sheety: {e}")
        return

    # 3) Fill IATA codes if missing
    for row in destinations:
        if not row.get("iataCode"):
            code = flight_search.get_iata(row["city"])
            if code:
                try:
                    data_manager.update_iata_code(row["id"], code)
                    row["iataCode"] = code
                    print(f"✔ Filled IATA for {row['city']}: {code}")
                except Exception as e:
                    print(f"⚠️ Failed to update IATA for {row['city']}: {e}")
            else:
                print(f"⚠️ Could not find IATA for {row['city']}")

    # 4) Get users list (emails)
    try:
        users = data_manager.get_users()
        emails = [u["email"] for u in users if u.get("email")]
    except Exception as e:
        print(f"❌ Could not fetch users: {e}")
        emails = []

    if not emails:
        print("ℹ️ No users found to notify (add some via CLI next run).")

    # 5) Search flights & notify when below threshold
    home_iata = os.getenv("HOME_IATA", "DEL")
    months_ahead = int(os.getenv("SEARCH_MONTHS_AHEAD", "6"))
    min_nights = int(os.getenv("MIN_NIGHTS", "7"))
    max_nights = int(os.getenv("MAX_NIGHTS", "28"))

    for row in destinations:
        dest_code = row.get("iataCode")
        if not dest_code:
            continue

        target = float(row.get("lowestPrice", 0))
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
        if price <= target:
            msg = (
                f"✈️ Low price alert! {flight_search.currency} {price} from "
                f"{result['origin_city']} ({result['origin_airport']}) to "
                f"{result['destination_city']} ({result['destination_airport']}).\n"
                f"Dates: {result['out_date']} → {result['return_date']}\n"
                f"Book: {result['deep_link'] or '(Open Kiwi app/site)'}"
            )
            notifier.send_emails(emails, msg)
        else:
            print(f"Price high for {row['city']}: found {flight_search.currency} {price} (limit {target})")

if __name__ == "__main__":
    main()
