import io

import pytest

import hello.hello_func as hello_func


@pytest.mark.parametrize("name", ["John", "Jane"])
def test_hello_says_hello_to_whatever_you_pass_as_a_name(name):
    stream = io.StringIO()
    hello_func.hello(name, stream)
    assert stream.getvalue() == "Hello, " + name + "!\n"


def test_hello_says_hello_in_standard_output_when_no_custom_stream_given(capsys):
    hello_func.hello("Python")
    out, _ = capsys.readouterr()
    assert out == "Hello, Python!\n"


def test_hello_says_hello_to_the_world_when_no_custom_name_given(capsys):
    hello_func.hello()
    out, _ = capsys.readouterr()
    assert out == "Hello, World!\n"
