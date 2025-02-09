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

