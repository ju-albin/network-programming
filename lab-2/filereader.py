scores = {}

with open ("score2.txt", "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) == 5:
            firstname = parts[2]
            lastname = parts[3]
            score = int(parts[4])

            if (firstname, lastname) not in scores:
                scores[(firstname, lastname)] = score
            else:
                scores[(firstname, lastname)] += score

onlyScores = scores.values()
topScore = max(onlyScores)

for person, score in scores.items():
    if score == topScore:
        print(person, score)

# The winners are Maria Johansson and Kristina Larsson with 37 points each.