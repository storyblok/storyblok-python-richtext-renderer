# storyblok-python-richtext-renderer

The utility class for renderer HTML from Richtext component in Storyblok.

## Install

```sh
pip install storyblok_richtext
```

## Usage

### Class `Richtext`

Instantiate the `Richtext` class:

```py
from storyblok_richtext import Richtext

resolver = Richtext()
```

And now use the object with `render()` function

```py
# code below ...
data = {
    'type': 'doc',
    'content': [{
        'type': 'horizontal_rule'
    }]
}

resolver.render(data) # renders a html string: '<hr />'
```

### How to define a custom schema for resolver?

The Richtext class can be receive a single parameter called `schema`. This parameter must be a dictionary with the two fields, `nodes` and `marks`. This fields can be dictionaries like as `storyblok_richtext/html_schema.py` file.

### Testing

We use unittest module for tests. In terminal, execute:

```sh
python -m unittest discover storyblok_richtext/tests -v
```

## Contribution

Fork me on [Github](https://github.com/storyblok/storyblok-python-richtext-renderer)
