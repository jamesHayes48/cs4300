def count_words(file_name):
    # Open file in read mode
    file = open(file_name, 'r')
    content = file.read()
    num_lines = 0

    # Split the file into an array by whitespace
    word_list = content.split(' ')

    # Count and return number of words
    for word in word_list:
        num_lines += 1
    return num_lines