# Declare an empty list
emp_list = []

# Declare a list with more than 5 items
cosas = ['manzana', 'platano', 'fresa', 'uva', 'higo', 'hoja', 'plato']

# Find the length of your list
print("Length of the list:", len(cosas))

# Get the first item, the middle item and the last item of the list
print("Primera cosa:", cosas[0])
print("Cosa de enmedio:", cosas[len(cosas) // 2])
print("Ultima cosa:", cosas[-1])

# Declare a list called mixed_data_types
mixed_data_types = ['Luis amor', 18, 1.75, 'Soltero', 'Vicente suarez, Calvillo']

# Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print("IT Companies:", it_companies)

# Print the number of companies in the list
print("Numero de compañias:", len(it_companies))

# Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

# Modify one of the companies
it_companies[1] = 'Alfa'  # Changed Google to Alfa
print("despues de la modificacion:", it_companies)

# Add an IT company
it_companies.append('Tesla')
print("despues de añadir una compañia:", it_companies)

# Insert an IT company in the middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Intel')
print("After inserting in the middle:", it_companies)

# Change one company name to uppercase (excluding IBM)
it_companies[0] = it_companies[0].upper()  # Facebook -> FACEBOOK
print("After changing to uppercase:", it_companies)

# Join the companies with '#; '
joined_companies = '#; '.join(it_companies)
print("Joined companies:", joined_companies)

# Check if a certain company exists
company_to_check = 'Apple'
print(f"Is {company_to_check} in the list?", company_to_check in it_companies)

# Sort the list
it_companies.sort()
print("Sorted companies:", it_companies)

# Reverse the list
it_companies.reverse()
print("Reversed list (descending):", it_companies)

# Slice out the first 3 companies
print("First 3 companies:", it_companies[:3])

# Slice out the last 3 companies
print("Last 3 companies:", it_companies[-3:])

# Slice out the middle IT company or companies
length = len(it_companies)
if length % 2 == 0:
    middle = it_companies[length // 2 - 1: length // 2 + 1]
else:
    middle = [it_companies[length // 2]]
print("Middle company/companies:", middle)

# Remove the first IT company
it_companies.pop(0)
print("After removing first company:", it_companies)

# Remove the middle company or companies
length = len(it_companies)
if length % 2 == 0:
    del it_companies[length // 2 - 1: length // 2 + 1]
else:
    del it_companies[length // 2]
print("After removing middle company/companies:", it_companies)

# Remove the last IT company
it_companies.pop()
print("After removing last company:", it_companies)

# Remove all IT companies
it_companies.clear()
print("After clearing all companies:", it_companies)

# Destroy the IT companies list
del it_companies
# print(it_companies)  # This will raise an error since the list is deleted

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.append('Python' + 'SQL')
full_stack = front_end + back_end