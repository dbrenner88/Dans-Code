programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

# adding a new value
programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# empty dictionary
empty_dict = {}

'''
# edit a dictionary item
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
'''

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille"],
    "Germany": ["Berlin", "Hamburg"],
}
visit = {}
for country in travel_log:
    cities = travel_log[country]
    travel_log[country] = {"cities_visited": cities,
                           "total_visits": len(country)}

print(travel_log)

travel_log_list = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille'],
        'total_visits': 6
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Hamburg'],
        'total_visits': 7
    }
]
print(travel_log_list[0])
