import os
import json
rent=3942
wifi=55.94
parking=285

her_proportion_rent=float(48.73)

her_rent=float(rent*her_proportion_rent/100)

def water(file_path):
    water_fee=[]
    with open(file_path,"r") as f:
             for line in f:
                  line = line.strip()
                  water_fee.append(float(line))
    return water_fee

def gas(file_path):
    gas_fee=[]
    with open(file_path, "r") as f:
             for line in f:
                  line = line.strip()
                  gas_fee.append(float(line))
    return gas_fee

def electricity(file_path):
    electricity_fee=[]
    with open(file_path, "r") as f:
             for line in f:
                  line = line.strip()
                  electricity_fee.append(float(line))
    return electricity_fee


base_dir = os.path.dirname(__file__)  
water_path = os.path.join(base_dir, "water_fee.txt")
gas_path=os.path.join(base_dir, "gas_fee.txt")
electricity_path=os.path.join(base_dir, "electricity_fee.txt")


water_fee=water(water_path)
gas_fee=gas(gas_path)
electricity_fee=electricity(electricity_path)

months=len(water_fee)
result=[]
for i in range(months):
      money_send = her_rent + (water_fee[i] + gas_fee[i] + electricity_fee[i]) / 2 + parking - (wifi / 2)
      result.append(f"month:{i+1}----------she send me: {money_send:.2f}")

result_path = os.path.join(base_dir, "result.json")
with open(result_path, "w") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)