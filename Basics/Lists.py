# Create a sample list
fruits = ["apple", "banana", "orange", "mango", "grape", "apple"]

# Loop through the list
print("All fruits in the list:")
for fruit in fruits:
    print(fruit)

# Search for specific elements
search_item = "apple"
if search_item in fruits:
    # Count occurrences
    count = fruits.count(search_item)
    # Find first position
    position = fruits.index(search_item)
    print(f"\nFound '{search_item}' {count} times")
    print(f"First occurrence at position: {position}")
else:
    print(f"\n{search_item} not found in the list")

# Find all positions of an item
print("\nAll positions of 'apple':")
for index, fruit in enumerate(fruits):
    if fruit == search_item:
        print(f"Found at position: {index}")