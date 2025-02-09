import task1 as t1

def test_answer(capsys):
    # Test if the output captured was Hello, World!
    t1.hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"