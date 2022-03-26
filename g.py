import csv

rows = []
planet_data = []
with open("main.csv", "r") as f:
 csvreader = csv.reader(f)
 for row in csvreader:
  rows.append(row)
headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []

for planet_data in planet_data_rows:
  planet_masses.append(planet_data[5])
  planet_radiuses.append(planet_data[6])
  planet_names.append(planet_data[3])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])* 1.989e+30) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.657e+8
  planet_gravity.append(gravity)

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planet_data_rows[index])

print(len(low_gravity_planets))