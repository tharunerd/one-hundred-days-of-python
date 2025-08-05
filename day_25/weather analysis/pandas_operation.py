import pandas as pd
import csv
import matplotlib.pyplot as plt

# Using just file methods
with open("day_25\weather analysis\weather_data.csv") as data_file:
    data_lines = data_file.readlines()
    print(data_lines)

# Using csv library
with open("day_25\weather analysis\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Using pandas
data = pd.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp.iloc[0])  # Fixed warning
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
students_df = pd.DataFrame(data_dict)
students_df.to_csv("new_data.csv", index=False)

# 1. View the data
print("Full Data:")
print(data)
print("\nFirst 5 rows:")
print(data.head())

# 2. Get summary statistics
print("\nSummary statistics:")
print(data.describe())

# 3. Access columns
print("\nTemperature column:")
print(data["temp"])

# 4. Filter data
print("\nDays with temperature > 20:")
print(data[data["temp"] > 20])

# 5. Calculate averages
print("\nAverage temperature:")
print(data["temp"].mean())

# 6. Find max/min values
print("\nDay with highest temperature:")
print(data[data["temp"] == data["temp"].max()])

# 7. Convert data (Celsius to Fahrenheit)
data["temp_F"] = data["temp"] * 9/5 + 32
print("\nData with Fahrenheit column:")
print(data)

# 8. Create new columns
data["is_warm"] = data["temp"] > 20
print("\nData with 'is_warm' column:")
print(data)

# 9. Plot data (requires matplotlib)
data.plot(x="day", y="temp", kind="line", marker="o", title="Temperature by Day")
plt.show()

# 10. Export data
data.to_csv("weather_data_modified.csv", index=False)

# 11. Group and aggregate (if you have a 'condition' column)
if "condition" in data.columns:
    print("\nAverage temp by condition:")
    print(data.groupby("condition")["temp"].mean())

# 12. Handle missing data
print("\nData with missing values filled (if any):")
print(data.fillna(0))