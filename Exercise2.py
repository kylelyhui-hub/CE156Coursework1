def group_by_length(words):
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    return length_dict

# Ask the user for a line of text
text = input("Enter a line of text: ")

# Split into a list of words
word_list = text.split()

# Call the function
result = group_by_length(word_list)

# Output the dictionary
print(result)
