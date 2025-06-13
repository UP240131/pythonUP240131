
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
#Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
ages.sort()
print(ages)
#Find the median age (one middle item or two middle items divided by two)
media = (ages[5]+ages[6])/2
print(media)
#Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(average)
#Find the range of the ages (max minus min)
min_age = min(ages)
max_age = max(ages)
range= (max_age-min_age)
print(range)
#Compare the value of (min - average) and (max - average), use abs() method
value = abs((min_age-average)and(max_age-average))
print(value)

#Find the middle country(ies) in the countries list
