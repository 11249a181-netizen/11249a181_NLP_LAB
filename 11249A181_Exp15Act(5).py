
start_p = {'DT': 0.6, 'NN': 0.3, 'VB': 0.1}

trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}

emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}

words = ['a', 'cat', 'runs']
tags = ['DT', 'NN', 'VB']

V = [{}]
path = {}

# Initialization
for tag in tags:
    V[0][tag] = start_p[tag] * emit_p[tag].get(words[0], 0)
    path[tag] = [tag]

# Recursion
for t in range(1, len(words)):
    V.append({})
    new_path = {}

    for current in tags:
        probabilities = [
            V[t-1][previous]
            * trans_p[previous][current]
            * emit_p[current].get(words[t], 0)
            for previous in tags
        ]

        best_index = probabilities.index(max(probabilities))
        best_previous = tags[best_index]

        V[t][current] = probabilities[best_index]
        new_path[current] = path[best_previous] + [current]

    path = new_path

# Termination
best_tag = max(V[-1], key=V[-1].get)

print("Viterbi table:")
for i, row in enumerate(V):
    print(words[i], row)

print("Best tag sequence:", path[best_tag])
print("Maximum probability:", V[-1][best_tag])