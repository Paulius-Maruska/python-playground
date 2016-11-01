def test_pyhello_says_hello_to_all_names(script_runner):
    ret = script_runner.run("pyhello", "foo", "bar")
    assert ret.success
    assert ret.stdout == "Hello, foo!\nHello, bar!\n"
    assert ret.stderr == ""


def test_pyhello_says_hello_to_all_names_on_stderr_when_flag_given(script_runner):
    ret = script_runner.run("pyhello", "-e", "foo", "bar")
    assert ret.success
    assert ret.stdout == ""
    assert ret.stderr == "Hello, foo!\nHello, bar!\n"
