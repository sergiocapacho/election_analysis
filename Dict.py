counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for key, value in counties_dict.items():
    print(key, value)
for county, voters in counties_dict.items():
    x = county
    y = voters
    print(str(x) + " county has " + str(y) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")