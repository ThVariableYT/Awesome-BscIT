# Organizing and sorting

scores = [85, 92, 78, 96, 88, 79]
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

# Combine names and scores into a list of tuples
combined = list(zip(names, scores))
print("Combined (before sorting):", combined)

# Sort by scores (second element of the tuple)
combined.sort(key=lambda x: x[1])
print("Combined (after sorting):", combined)

# Unzip the combined list back into names and scores
names_sorted, scores_sorted = zip(*combined)
print("Names (sorted):", names_sorted)
print("Scores (sorted):", scores_sorted)