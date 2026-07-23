import requests
import json
import time


def fetch_recalls(make, model, year):
    """Fetch recalls for one make/model/year from the NHTSA API."""
    params = {"make": make, "model": model, "modelYear": year}
    response = requests.get("https://api.nhtsa.gov/recalls/recallsByVehicle", params=params)
    data = response.json()
    return data["results"]


if __name__ == "__main__":
    VEHICLES = [
        ("acura", "rdx", 2012),
        ("honda", "civic", 2015),
        ("toyota", "camry", 2018),
        ("ford", "f-150", 2020),
        ("honda", "accord", 2013),
        ("honda", "cr-v", 2012),
        ("acura", "tl", 2010),
        ("toyota", "corolla", 2014),
        ("toyota", "rav4", 2016),
        ("nissan", "altima", 2015),
        ("chevrolet", "silverado", 2019),
        ("jeep", "grand cherokee", 2015),
        ("dodge", "ram", 2014),
        ("bmw", "3 series", 2012),
        ("ford", "escape", 2017),
        ("hyundai", "sonata", 2015),
        ("kia", "optima", 2014),
        ("subaru", "outback", 2016),
        ("volkswagen", "jetta", 2013),
        ("mazda", "cx-5", 2016),
        ("honda", "odyssey", 2011),
        ("toyota", "highlander", 2015),
        ("ford", "explorer", 2016),
        ("chevrolet", "malibu", 2016),
    ]

    all_recalls = []
    for make, model, year in VEHICLES:
        recalls = fetch_recalls(make, model, year)
        all_recalls.extend(recalls)
        time.sleep(0.5)
        print(f"{make} {model} {year}: {len(recalls)} recalls")

    print(f"Total: {len(all_recalls)}")

    with open("recalls_raw.json", "w") as f:
        json.dump(all_recalls, f, indent=2)
    print(f"Saved {len(all_recalls)} recalls to recalls_raw.json")