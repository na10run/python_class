#  Assignment 1:

test_word = {'to': 0, 'her': 0, 'rabbit': 0, 'she': 0, 'adventures': 0, 'alice': 0, 'by': 0, 'in': 0}
text_file = open('pg11.txt', 'r')

# now we loop through each line
for line in text_file:

    for word in line.split():
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.replace("!", "")
        word = word.replace("?", "")

        for keys, values in test_word.items():

            if keys == word.lower():
                test_word[keys] += 1

print(test_word)
