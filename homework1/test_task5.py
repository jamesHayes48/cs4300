import task5 as t5

# Test list slicing and other operations with book list
def test_list(capsys):
    # Test that list slicing of books is as expected
    print(t5.favorite_books[0:3])
    t5.capture_three_books = capsys.readouterr()
    assert t5.capture_three_books.out == ("[('The Witcher: The Sword of Destiny', 'Andrzej Sapkowski'), ('Dune', 'Frank Herbert'), "
   "('The Catcher in the Rye', 'J.D. Salinger')]\n") 

    assert t5.favorite_books[4] == ("Children of Dune", "Frank Herbert")
    
    # Test that the list backwards is correct
    assert t5.favorite_books[::-1] == [("Children of Dune", "Frank Herbert"), ("Frankenstein", "Mary Shelley"), 
    ("The Catcher in the Rye", "J.D. Salinger"), ("Dune", "Frank Herbert"), 
    ("The Witcher: The Sword of Destiny", "Andrzej Sapkowski")]

# Test student Dictionary keys and search function
def test_dict():
   assert t5.student_database["James"] == {"id": 1234, "major": "CS"}
   assert t5.student_database["Joel"]["major"] == "EE"
   assert t5.get_lowest_name(t5.student_database) == {"id":1043, "major": "CHEM"}