# Superpowers Kata π₯

This repository is for my work in the [Everyday Superpowers](https://everydaysuperpowers.dev/) [Python Growth Challenge](https://everydaysuperpowers.dev/python-growth-challenge/).

My goals for this challenge are:
* Use the [Python Standard Library](https://docs.python.org/3/library/) for all the code
* Use [pytest](https://docs.pytest.org/) for all the testing (because no one needs to fuss with [unittest](https://docs.python.org/3/library/unittest.html))
* Use as much [type hinting](https://docs.python.org/3/library/typing.html) as possible
  * Remember Python 3.9 allows use of [standard collections as types](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)

## About Everyday Superpowers π¦ΈββοΈ

Everyday Superpowers is a site about providing tools to empower others in their personal and professional journey, particuarly with Python.
The website belongs to my good buddy Chris May.
He's got some good [articles](https://everydaysuperpowers.dev/articles/) and [resources](https://everydaysuperpowers.dev/resources/) to checkout.
You should check him out on [github](https://github.com/Chris-May) or tweet him up at [@_chrismay](https://twitter.com/_chrismay) π.
I'm told putting this in the readme will not get me extra credit π.

Chris and I (and others) also organize [PyRVA](http://www.pyrva.org/), the Python User Group in Richmond, VA.
Feel free to join our group on [Meetup](https://www.meetup.com/PyRVAUserGroup/) or [Discord](https://discord.gg/fSGW7Jra4T)

# Lessons Learned From This Kata

## The [pre-commit framework](https://pre-commit.com/) is awesome

Pre-commit works off the `.pre-commit-config.yaml` file and runs before you can run `git commit`. Once you have the configuration file setup, you run `pre-commit install` and all your checks are ready to be used. If you notice your pre-commit hooks are updated, `pre-commit autoupdate` will make sure you're using the latest and greatest of the hooks. Some of the hooks won't just say "oh, you have an error," but it will fix the errors for you!

Hooks I've installed:
* `check-yaml`: Checks yaml files are parseable (like the config file).
* `end-of-file-fixer`: Ensures a single whitespace at the end of each file if not empty. Black will do this for Python code only.
* `trailing-whitespace`: Keep commits clean by trailing extra whitespace.
* `black`: Keeps Python code nice, tidy, and readable.
* `mypy`: Checks that my static typing is correct.

## Github Actions is not as scary as I thought

A while ago, I had played with Github Actions and I managed to get something to work for that repo, but it felt like magic and I was afraid to touch the config file. I took a look at [Building and testing Python](https://docs.github.com/en/actions/guides/building-and-testing-python) and either the documentation has improved since I last looked at it or my comprehension improved. Now I have CI/CD checks to make sure that all the tests pass and that black formatting is maintained.

Why have black in my pre-commit AND github actions? Well, it's possible I might clone the repo on another computer and forget to install the pre-commit hooks. This will help me realize that I missed the step on that computer.

## pytest has trouble with standard collection types

I had a function signature of `def announce(scores: list[int]) -> str:`. When running pytest, this caused an error of:

    ~~~~~ ERROR collecting src/kata-01-tennis/test_kata.py ~~~~~
    src/kata-01-tennis/test_kata.py:2: in <module>
        import kata
    src/kata-01-tennis/kata.py:25: in <module>
        def announce(scores: list[int]) -> str:
    E   TypeError: 'type' object is not subscriptable

I'm developing in Python 3.9, so I know that the syntax should work. `def announce(scores: list) -> str:` was not causing any errors.

Digging around, I came to [PEP 585: Type Hinting Generics in Standard Collections](https://www.python.org/dev/peps/pep-0585/) and found the following passage:

> Starting with Python 3.7, when from __future__ import annotations is used, function and variable annotations can parameterize standard collections directly. Example:
```python
from __future__ import annotations

def find(haystack: dict[str, list[int]]) -> int:
    ...
```

Adding the `__future__` import at the top of the file allowed pytest to run and all the tests passed.

## Defining custom exceptions can be really easy

All you need to do is wrap the `Exception` class or one of the derivative classes.

```python
class KataError(Exception):
    pass

class KataSubError(KataError):
    pass
```

With this, it's easier to make error message that are more useful. To test them, you can use [`pytest.raises`](https://docs.pytest.org/en/stable/reference.html#pytest-raises) to make sure that an error occurs when it is supposed to. You can also check that the error has the expected message or that it's subclasssed form another error class.

```python
def test_raises_error():
    with pytest.raises(KataSubError) as exc_info:
        raise KataSubError("something is wrong")
    assert "something is wrong" in exc_info.value.args[0]
    assert exc_info.type == kata.KataSubError
    assert issubclass(exc_info.type, kata.KataError)
```

## Decorators are useful once you figure them out

Real Python has a nice [primer on python decorators](https://realpython.com/primer-on-python-decorators/). However, it does not seem to touch on the idea of working with the values passed to the wrapped function.

If you want to work with the values, you need to account for them being passed in either by position *OR* keyword. Another option is to use [positional-only parameters](https://www.python.org/dev/peps/pep-0570/), but that requires Python 3.8+.

You can also create decorators with additional arguments, but where regular decorators are called without parenthesis `@decorator`, if you have parameters, you need to include the parenthesis `@decorator()`.

## The [inspect](https://docs.python.org/3/library/inspect.html) module can be fun if you play with `__name__` and `__file__`

For the second kata, there were a lot of function with the name `score_*`. To find the best score for a given roll, I wanted to see what the scores were for each possible condition. Rather than hard coding each function (which would have been fine for a fixed game), I wanted to dynamically load all the scoring functions.

I could find all the functions with the following snippet:

```python
scoring_functions = [
    func
    for name, func in inspect.getmembers(sys.modules[__name__])
    if inspect.isfunction(func)
    and inspect.getfile(func) == __file__
    and name[:6] == "score_"
]
```

## You can tell [coverage](https://coverage.readthedocs.io/) to ignore lines.

In my `test_kata02` file, I wanted to test my decorator function. I created a placeholder function with the following signature.

```python
def func(*args, **kwargs):
    pass
```

Clearly, I have no intention of the inside of this function to execute. But since I'm putting my test code in the `src` folder, running `pytest --cov src` saw it as a miss.

Looking at the [documentation](https://coverage.readthedocs.io/en/coverage-4.3.3/excluding.html), all you need is to put a comment that says `# pragma: no cover` on a line or the start of a block and it will be excluded like so.

```python
def func(*args, **kwargs):
    pass  # pragma: no cover
```

However, I am not a huge fan of putting these comments in unless necessary. So I dug deeper and found that you can make a [configuration file](https://coverage.readthedocs.io/en/coverage-4.3.3/config.html). In the `[report]` section of the `.coveragerc`, you can specify `exclude_lines`. As such, the configuration below allows me to ignore any line that just says `pass` in any file.

Furthermore, I specified that the source files are located in `src` so now I can just type `pytest --cov` instead of `pytest --cov=src`!

```
[run]
source = src

[report]
exclude_lines =
    pass
```

## You can parallelize pytest with `pytest-xdist`

[`pytest-xdist`](https://pypi.org/project/pytest-xdist/) can send your tests to multiple CPUs by running:

`pytest -n NUMCPUS`

There is a little bit of overhead so this may not yield much if the tests run fast enough. For Kata 03, I was testing all numbers 0 to 4,999 in both directions.

| Command        | CPUs  | Time    |
| -------------- | :---: | ------- |
| `pytest`       |   1   | 16.34 s |
| `pytest -n 6`  |   6   | 13.65 s |
| `pytest -n 12` |  12   | 15.63 s |

My computer has 6 cores / 12 threads. It appears that these tests ran best with one test per physical core.

## You can tell pytest which tests to incldue or ignore

If you use the `@pytest.mark.<name>` syntax, you can tell pytest which tests you want to run. You will have to [register your marks](https://docs.pytest.org/en/stable/mark.html) in the [configuration file](https://docs.pytest.org/en/stable/customize.html).

You can specify which tests to run with `pytest -m <name>`. This will find all tests that ***M***atch the provided name. If you have multiple marks with similar names and you want to run them all, you can use `pytest -k <name>` and it will run all marks li***K***e the name specified.
