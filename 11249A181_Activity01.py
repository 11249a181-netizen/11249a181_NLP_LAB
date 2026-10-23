subjects = ["John", "Mary"]
objects = ["John", "Mary"]
verb = "eats"
print("Generated Sentences:\n")
for subject in subjects:
    for obj in objects:
        sentence = f"{subject} {verb} {obj}"
        print(sentence)