import requests 
import time 

def fetch_recalls (make,model, year): 
    #a function which can give u the recall data when plugging in make, model, and year
    params = {"make": make, "model": model, "modelYear": year}
    response = requests.get("https://api.nhtsa.gov/recalls/recallsByVehicle", params= params) #get request to nhtsa 
    data = response.json()        # parse the response body as JSON into a Python dict
    return data["results"]         # return results list 


recalls = fetch_recalls ("acura", "rdx", 2012)
print (len(recalls))

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