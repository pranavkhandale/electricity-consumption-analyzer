import numpy as np
houses = np.array(["H1", "H2", "H3", "H4", "H5", "H6"])
units = np.array([120, 250, 180, 90, 310, 150])

print()
print("-"*5, "Total Electricity unit consumed", "-"*5)
total = np.sum(units)
print("Total units consumed:", total)

print()
print("-"*5, "Average Consumption", "-"*5)
avg = np.round(np.mean(units),2)
print(f"Avearge Consumption: {avg}")

print()
print("-"*5, "High Consumption Houses", "-"*5)
high_consumption = units > 200
print(f"Houses consuming more than 200: {houses[high_consumption]}")

print()
print("-"*5, "Highest Consumption", "-"*5)
highest = np.argmax(units)
print(f"House -> {houses[highest]}\nUnits -> {units[highest]} ")

print()
print("-"*5, "Houses below average consumption", "-"*5)
houses_name = houses[units < avg]
print(f"Houses whose electricity consumption below is below the avearge consumption: {houses_name}")

print()
print("-"*5, "Consumption percentage", "-"*5)
for i in range(len(units)):
    percentage = np.round((units[i] / total) * 100, 2)
    print(f"{houses[i]} -> {percentage}")

print()
print("-"*5, "lowest Consumption", "-"*5)
lowest = np.argmin(units)
print(f"House with lowest electricity consumption:\n House name -> {houses[lowest]}\n Unit consumed -> {units[lowest]}")
