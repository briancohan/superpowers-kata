# Superpowers Kata 🥋

This repository is for my work in the [Everyday Superpowers](https://everydaysuperpowers.dev/) [Python Growth Challenge](https://everydaysuperpowers.dev/python-growth-challenge/).

My goals for this challenge are:
* Use the [Python Standard Library](https://docs.python.org/3/library/) for all the code
* Use [pytest](https://docs.pytest.org/) for all the testing (because no one needs to fuss with [unittest](https://docs.python.org/3/library/unittest.html))
* Use as much [type hinting](https://docs.python.org/3/library/typing.html) as possible
  * Remember Python 3.9 allows use of [standard collections as types](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)

## About Everyday Superpowers 🦸‍♂️

Everyday Superpowers is a site about providing tools to empower others in their personal and professional journey, particuarly with Python.
The website belongs to my good buddy Chris May.
He's got some good [articles](https://everydaysuperpowers.dev/articles/) and [resources](https://everydaysuperpowers.dev/resources/) to checkout.
You should check him out on [github](https://github.com/Chris-May) or tweet him up at [@_chrismay](https://twitter.com/_chrismay) 👋.
I'm told putting this in the readme will not get me extra credit 😔.

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
