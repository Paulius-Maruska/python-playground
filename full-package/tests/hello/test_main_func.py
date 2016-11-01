import io
import sys

import hello.main_func as main_func


def test_get_parser_parser_defaults():
    parser = main_func.get_parser()
    parsed = parser.parse_args(["Python"])
    assert parsed.names == ["Python"]
    assert parsed.stream == sys.stdout


def test_get_parser_parser_adds_all_names_to_the_list():
    parser = main_func.get_parser()
    parsed = parser.parse_args(["Python", "Linux", "Internet"])
    assert parsed.names == ["Python", "Linux", "Internet"]


def test_get_parser_parser_uses_stderr_as_stream_if_stderr_flag_provided():
    parser = main_func.get_parser()
    parsed = parser.parse_args(["--stderr", "Python"])
    assert parsed.names == ["Python"]
    assert parsed.stream == sys.stderr


def test_get_parser_parser_uses_stderr_as_stream_if_short_stderr_flag_provided():
    parser = main_func.get_parser()
    parsed = parser.parse_args(["-e", "Python"])
    assert parsed.names == ["Python"]
    assert parsed.stream == sys.stderr


class DummyParser():
    def __init__(self, names=None, stream=None):
        self.names = names
        if self.names is None:
            self.names = ["Python"]
        self.stream = stream
        if self.stream is None:
            self.stream = io.StringIO()

    def parse_args(self, *args, **kwargs):
        return self


def test_main_calls_hello_for_each_name_and_uses_the_stream_from_parsed_object(mocker):
    stream = io.StringIO()
    parser = DummyParser(["foo", "bar"], stream)
    mocker.patch("hello.main_func.get_parser", return_value=parser)
    hello = mocker.patch("hello.main_func.hello")
    main_func.main()
    assert hello.call_count == 2
    assert hello.call_args_list == [(("foo", stream),), (("bar", stream),)]
