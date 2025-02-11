import task6 as t6

# Generate pytest functions based off the name of the file
def generate_pytest(file_name, word_count):
    function_name = f"test_{file_name[:-4]}"
    exec(f"def {function_name}(): assert t6.count_words('{file_name}') == {word_count}", globals())
    globals()[function_name]()

generate_pytest("task6_read_me.txt", 104)