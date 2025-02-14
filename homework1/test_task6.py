import task6 as t6

# Dictionary to hold name of file and the word count
files_to_test = {
    'task6_read_me.txt':104,
    'hi.txt':4,
}

# Generate pytest functions based off the name of the file
def generate_pytest(files):
    for name, word_count in files.items():
        
        # Remove replace . with _ in function name
        function_name = f"test_{name.replace('.', '_')}"

        # Create function and call it soon after
        exec(f"def {function_name}(): assert t6.count_words('{name}') == {word_count}", globals())


generate_pytest(files_to_test)