import csv

lines = csv.reader(open("trainingexamples.csv", "r"))
dataset = list(lines)

specific = dataset[1][:-1]
general = [["?" for i in range(len(specific))] for j in range(len(specific))]

print("S[0]: ", ["0" for i in range(len(specific))])
print("G[0]: ", ["?" for i in range(len(specific))])

for i in dataset:
    if i[-1] == "Y":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                specific[j] = "?"
                general[j][j] = "?"

    elif i[-1] == "N":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = "?"
    print("\nStep " + str(dataset.index(i) + 1) + " of candidate elimination : ")
    print("S[" + str(dataset.index(i) + 1) + "]: ", specific)
    print("G[" + str(dataset.index(i) + 1) + "]: ", general)

gh = []
for i in general:
    for j in i:
        if j != "?":
            gh.append(i)
            break
# gh=[i for i in general if '?' not in i]

print("\nFinal specific hypothesis is : ", specific)
print("\nFinal gneral hypothesis is : ", gh)