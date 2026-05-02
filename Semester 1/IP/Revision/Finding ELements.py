# Finding ELements

animals = ["cat", "dog", "rabbit", "cat", "hamster"]

# index() - Returns the index of the first occurrence of a specified value.
cat_index = animals.index("cat")
print("Index of first cat:", cat_index)                      # Output: 0

# count() - Returns the number of occurrences of a specified value.
cat_count = animals.count("cat")
print("Number of cats:", cat_count)                          # Output: 2

# in operator - Checks if a specified value exists in the list.
has_dog = "dog" in animals
has_bird = "bird" in animals
print("Is there a dog?", has_dog)                             # Output: True
print("Is there a bird?", has_bird)                           # Output: False