subjects = ["John", "Mary", "Student"]
objects = ["John", "Mary", "Student"]
print("Generated Sentences:\n")
for subject in subjects:
    # Rule: VP → eats NP
    for obj in objects:
        print(f"{subject} eats {obj}")
    print(f"{subject} studies NLP")-