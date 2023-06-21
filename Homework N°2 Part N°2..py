# Federico Teijeiro.
# June 8, 2023.
# Homework N°2 Part N°2.

# Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order.
countries = ["United States", "Austria", "Italy", "Denmark", "Belgium", "Argentina", "Japan"]

# Using a for loop, print each element of the list.
for list in range(0, len(countries)):
  print(countries[list])
print("")

# Sort the list permanently.
countries.sort()
print(countries)
print("")

# Display the first element of the list.
print(countries[0])
print("")

# Display the second-to-last element of the list.
print(countries[-2])
print("")

# Delete one of the countries from the list using its name.
countries.remove("Japan")
print(countries)
print("")

# Using a for loop, print each country's name in all caps.
elements = [country.upper() for country in countries]
print(elements)
print("")
print("======================================================================")
print("")

# Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. 
# Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
tree = {
  "name": "Jōmon Sugi",
  "species": "Sugi Cryptomeria japonica",
  "age": 1811,
  "location name": "Yakushima Island",
  "latitude": 30.310155,
  "longitude": 130.594957
}

# Print the sentence "{name} is a {years} year old tree that is in {location_name}".
print("The", tree["name"], "is", tree["age"], "old tree that is in", tree["location name"])
print("")

# The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print 
# "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC".
if tree["latitude"] < 40.7128:
  print("The tree", tree["name"], "in", tree["location name"], "is south of New York city.")
else:
  print("The tree", tree["name"], "in", tree["location name"], "is north of New York city.")
print("")

# Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." 
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."

age = int(input("How old are you?: "))
print(type(age))
if age > tree["age"]:
  difference1 = age - tree["age"]
  print("You are", difference1, "older than", tree["name"])
elif age < tree["age"]:
  difference2 = tree["age"] - age
  print(tree["name"], "was", difference2, "years old when you were born.")
else:
  print("You have the same age than the tree.")
print("")
print("======================================================================")
print("")

# Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. 
# Each dictionary should include each city's name and latitude/longitude (see note above).
cities = [
  { "name": "Moscow", "latitude": 55.7558, "longitude": 37.6173 },
  { "name": "Tehran", "latitude": 35.6892, "longitude": 51.3890 },
  { "name": "Falkland Islands", "latitude": -51.7963, "longitude": -59.5236 },
  { "name": "Seoul", "latitude": 37.5665, "longitude": 126.9780 },
  { "name": "Santiago", "latitude": -33.4489, "longitude": -70.6693 }
]

# Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). 
# When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," 
# which is a sentence I stole from Wikipedia.
for city in cities:
  if city["latitude"] > 0:
    print(city["name"], "is above the ecuator line.")
  elif city["latitude"] < 0:
    print(city["name"], "is below the ecuator line.")
  if city["name"] == "Falkland Islands":
    print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
print("")

# Loop through the list, printing whether each city is north of south of your tree from the previous section.
for city in cities:
  if tree["latitude"] > city["latitude"]:
    print("The tree is to the north of", city["name"])
  elif tree["latitude"] < city["latitude"]:
    print("The tree is to the south of", city["name"])
  