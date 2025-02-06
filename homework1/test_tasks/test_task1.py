import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import task1

def test_answer(capsys):
    # Test if the output captured was Hello, World!
    task1.hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"