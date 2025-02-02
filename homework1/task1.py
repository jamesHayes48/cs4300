def hello_world():
    print("Hello, World!")

def test_answer(capsys):
    # Test if the output captured was Hello, World!
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"