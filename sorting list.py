
# Initialize an empty list to store the names
names = []

# Prompt the user to enter a list of names, one per line
print("Enter a list of names, one per line (type 'done' when finished):")
while True:
    name = input()
    if name.lower() == "done":
        break
    names.append(name)

# Sort the names in alphabetical order and remove duplicates
names = sorted(set(names))

# Print the sorted list of names and the total number of entries
print("\nSorted list of names (duplicates removed):")
for name in names:
    print(name)
print(f"Total number of entries: {len(names)}")
