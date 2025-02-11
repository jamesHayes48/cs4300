def count_words(file_name):
    file = open(file_name, 'r')
    content = file.read()
    num_lines = 0
    word_list = content.split(' ')

    for word in word_list:
        num_lines += 1
    return num_lines