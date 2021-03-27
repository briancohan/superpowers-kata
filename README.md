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
