def word_break(s, word_dict):
    def backtrack(index, path):
        if index == len(s):
            result.append(" ".join(path))
            return
        for i in range(index + 1, len(s) + 1):
            word = s[index:i]
            if word in word_set:
                backtrack(i, path + [word])

    result = []
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    if dp[len(s)]:
        backtrack(0, [])
    return result

# Example usage with a larger dictionary:
word_dict = [
    "cat", "cats", "and", "sand", "dog", "dogs", "bird", "birds", "fish", "fishes",
    "run", "running", "jumps", "jumping", "plays", "playing", "walk", "walking",
    "swim", "swimming", "fly", "flying", "tree", "trees", "bush", "bushes",
    "car", "cars", "bike", "bikes", "train", "trains", "plane", "planes",
    "house", "houses", "building", "buildings", "book", "books", "pen", "pens",
    "computer", "computers", "phone", "phones", "tablet", "tablets", "lamp", "lamps"
]

# Print the word dictionary to ensure it makes sense:
print("Word Dictionary:", word_dict)

# Example string to test:
s = "catsanddogsrunning"

# Call the word_break function and print the results:
print(word_break(s, word_dict))
