colors = ["red", "green", "blue"]
print(colors)
print(colors[1]) # Prints green because red is [0]

fruits = ["apple", "banana", "orange", "kiwi", "balkan rage"]
# For-each loop
for item in fruits:
	print(item)
print("")

# For loop
for index in range(len(fruits)):
	print(fruits[index])
print("")

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1]
print(lastfruit)
input()
