# Federico Teijeiro.
# June 8, 2023.
# Homework N°2 Part N°1.

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48.
numbers = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list.
print("The amount of elements in the list is:", len(numbers))

# Display the 4th element of this list.
print("The forth element is:", numbers[3])

# Display the sum of the 2nd and 4th element of the list.
sss = numbers[1] + numbers[3]
print("The sum of the second and forth element is", sss)

# Display the 2nd-largest value in the list.
numbers2 = list(set(numbers))
numbers2.sort()
print("The second largest element is:", numbers2[-2])

# Display the last element of the original unsorted list
print("The last elemet is:", numbers[-1])

# Display the sum of all of the numbers divided by two.
print("The sum of all elements is:", sum(numbers))

# Print whether the median or the mean of the numbers is higher.
n = len(numbers)
get_sum = sum(numbers)
mean = get_sum / n
print("Mean/Average is: " + str(mean))

n = len(numbers)
numbers.sort()
if n % 2 == 0:
    median1 = numbers[n//2]
    median2 = numbers[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = numbers[n//2]
print("Median is: " + str(median))

if median > mean:
  print("The median is greater than the mean.")
else:
  print("The mean is greater than the median.")

print("")
print("======================================================================")
print("")

# Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. 
# Define a dictionary called movie that works with the following code.
movie = {
  "title": "Before Sunrise",
  "year": 1995,
  "director": "Richard Linklater"
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
print("")

# On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), 
# and print out the difference between the two.
print("The original dictionary is: ", movie)
movie['budget'] = 10000000  
movie['revenue'] = 50000000  
print("The new dictionary is: ", movie)

if movie['budget'] == movie['revenue']:
  print("The budget and the revenue are the same.")
elif movie['budget'] <= movie['revenue']:
  print(movie['revenue'] - movie['budget'])
  print("The revenue is greater than the budget.")
else:
  print(movie['budget'] - movie['revenue'])
  print("The budget is greater than the revenue.")
print("")

# If the movie cost more to make than it made in theaters, print "That was a bad investment". 
# If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." 
# Otherwise print "That was an okay investment."
movie['cost'] = 30000000  
print("The new dictionary is: ", movie)

if movie['cost'] == movie['revenue']:
  print("The film did not make a profit, nor a loss.")
elif movie['budget'] <= movie['revenue']:
  print(movie['revenue'] - movie['budget'])
  print("The revenue is greater than the budget.")
else:
  print(movie['budget'] - movie['revenue'])
  print("The budget is greater than the revenue.")
print("")

# Sometimes dictionaries are used to describe the same aspects of many different objects. 
# Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
# Tip: keeping it all in either millions or thousands is a good idea.
nyc_boroughs = {
  "Manhattan": 1600000,
  "Brooklyn": 2600000,
  "Bronx": 1400000,
  "Queens": 2300000,
  "Staten Island": 470000
}
print("")

# Display the population of Brooklyn.
for key, value in nyc_boroughs.items():
  if key == "Brooklyn":
    print(key, value)  
print("")     

# Display the combined population of all five boroughs.
for key, value in nyc_boroughs.items():
  print(key, value)  
print("")    

# Display what percent of NYC's population lives in Manhattan.
nyc_percent = sum(nyc_boroughs.values())
for key, value in nyc_boroughs.items():
  percent = value * 100.0 / nyc_percent
  if str(key).startswith('Man'):
    print(key, round(percent, 2))
print("")  
  
