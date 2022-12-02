# Write a program to find the most repeated character in the sentence
sentence = "Now you've gone and bent the wheel Ezekiel."
char_rep = {}
for char in sentence:
    if char in char_rep:
        char_rep[char] += 1
    else:
        char_rep[char] = 1

most_repeated = sorted(char_rep.items(), key=lambda kv:kv[1], reverse = True)
print(most_repeated[0])