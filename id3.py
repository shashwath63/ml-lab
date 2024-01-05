import math
import csv

class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.children = []
        self.answer = ""  # NULL indicates children exist. Not NULL indicates this is a Leaf Node

    def subtables(self, data, col, delete):
        dic = {}
        coldata = [row[col] for row in data]
        attr = list(set(coldata))  # All values of attribute retrieved
        for k in attr:
            dic[k] = []
        for y in range(len(data)):
            key = data[y][col]
            if delete:
                del data[y][col]
            dic[key].append(data[y])
        return attr, dic

    def entropy(self, S):
        attr = list(set(S))
        if len(attr) == 1:  # if all are +ve/-ve then entropy = 0 return 0
            return 0
        counts = [0, 0]  # Only two values possible 'yes' or 'no'
        for i in range(2):
            counts[i] = sum([1 for x in S if attr[i] == x]) / (len(S) * 1.0)
        sums = 0
        for cnt in counts:
            sums += -1 * cnt * math.log(cnt, 2)
        return sums

    def compute_gain(self, data, col):
        att_values, dic = self.subtables(data, col, delete=False)
        total_entropy = self.entropy([row[-1] for row in data])
        for x in range(len(att_values)):
            ratio = len(dic[att_values[x]]) / (len(data) * 1.0)
            entro = self.entropy([row[-1] for row in dic[att_values[x]]])
            total_entropy -= ratio * entro
        return total_entropy

    def build_tree(self, data, features):
        last_col = [row[-1] for row in data]
        if len(set(last_col)) == 1:  # If all samples have the same labels, return that label
            node = Node("")
            node.answer = last_col[0]
            return node
        n = len(data[0]) - 1
        gains = [self.compute_gain(data, col) for col in range(n)]
        split = gains.index(max(gains))  # Find max gains and return the index
        node = Node(features[split])  # 'node' stores the selected attribute
        fea = features[:split] + features[split + 1:]
        attr, dic = self.subtables(data, split, delete=True)  # Data will be split into subtables
        for x in range(len(attr)):
            child = self.build_tree(dic[attr[x]], fea)
            node.children.append((attr[x], child))
        return node

    def print_tree(self, node, level):
        if node.answer != "":
            print(" " * level, node.answer)  # Displays leaf node yes/no
            return
        print(" " * level, node.attribute)  # Displays attribute Name
        for value, n in node.children:
            print(" " * (level + 1), value)
            self.print_tree(n, level + 2)

    def classify(self, node, x_test, features):
        if node.answer != "":
            print(node.answer)
            return
        pos = features.index(node.attribute)
        for value, n in node.children:
            if x_test[pos] == value:
                self.classify(n, x_test, features)

def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    headers = dataset.pop(0)
    return dataset, headers

if __name__ == "__main__":
    # Read the training dataset
    dataset, features = load_csv("data3.csv")

    # Build decision tree
    root_node = Node("").build_tree(dataset, features)

    print("The decision tree for the dataset using the ID3 algorithm is ")
    root_node.print_tree(root_node, 0)

    # Read the test dataset
    test_data, test_features = load_csv("data3_test.csv")

    # Classify test instances
    for x_test in test_data:
        print("The test instance:", x_test)
        print("The predicted label:", end="")
        root_node.classify(root_node, x_test, features)
