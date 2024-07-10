friendList = ["Suraj", "Aniket", "Rakesh", "Rohit", "Darshan"]

print(friendList[1:])   # it will print from index 1 to last
print(friendList[1:4])  # it will print up to index 3 not including 4

# insert one list to another list
newList = ["Chandra", "Sandip"]
friendList.extend(newList)
print(friendList)

# append one data to list
friendList.append("Manas")
print(friendList)

# insert into specific index
friendList.insert(1, "Raju")
print(friendList)

# remove
friendList.remove("Manas")
print(friendList)

# clear the list -> friendList.clear()

# remove last element in the list
friendList.pop()

# find index of the present data in the list
print(friendList.index("Raju"))

# reverse list
friendList.reverse()
print(friendList)
