favorite_books = [("The Witcher: The Sword of Destiny", "Andrzej Sapkowski"), ("Dune", "Frank Herbert"),
 ("The Catcher in the Rye", "J.D. Salinger"), ("Frankenstein", "Mary Shelley"), ("Children of Dune", "Frank Herbert")]

student_database = {"James": {"id": 1234, "major": "CS"}, "Joel": {"id": 5679, "major": "EE"}, "Bob": {"id":1043, "major": "CHEM"}, 
"Billy": {"id": 5632, "major": "MATH"}}

# Get the shortest name in the student database and return
# The student's information
def get_lowest_name(students):
   lowest = 0
   lowest_name = ""
   for student_name in students.keys():
      name_len = len(student_name)
      # Check if any name is shorter than current
      # shortest
      if lowest > name_len:
         lowest = name_len
         lowest_name = student_name

      # Assign lowest to be the first name
      elif lowest == 0:
         lowest = name_len
         lowest_name = student_name
   return students[lowest_name]

# Test list slicing and other operations with book list
def test_list(capsys):
    # Test that list slicing of books is as expected
    print(favorite_books[0:3])
    capture_three_books = capsys.readouterr()
    assert capture_three_books.out == ("[('The Witcher: The Sword of Destiny', 'Andrzej Sapkowski'), ('Dune', 'Frank Herbert'), "
   "('The Catcher in the Rye', 'J.D. Salinger')]\n") 

    assert favorite_books[4] == ("Children of Dune", "Frank Herbert")
    
    # Test that the list backwards is correct
    assert favorite_books[::-1] == [("Children of Dune", "Frank Herbert"), ("Frankenstein", "Mary Shelley"), 
    ("The Catcher in the Rye", "J.D. Salinger"), ("Dune", "Frank Herbert"), 
    ("The Witcher: The Sword of Destiny", "Andrzej Sapkowski")]

# Test student Dictionary keys and search function
def test_dict():
   assert student_database["James"] == {"id": 1234, "major": "CS"}
   assert student_database["Joel"]["major"] == "EE"
   assert get_lowest_name(student_database) == {"id":1043, "major": "CHEM"}