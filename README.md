# storyblok-python-richtext-renderer

This package allows you to get an HTML string from the [richtext field](https://www.storyblok.com/docs/richtext-field) of Storyblok.

## Install

```sh
pip install storyblok-richtext
```

## Usage

### Class `Richtext`

Instantiate the `Richtext` class:

```py
from storyblok_richtext import Richtext

resolver = Richtext()
```

Use the function `render()` to get the html string from your richtext field.

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

Make a copy of the default schema [storyblok_richtext/html_schema.py](https://github.com/storyblok/storyblok-python-richtext-renderer/blob/master/storyblok_richtext/html_schema.py) and your own schema as parameter to the Richtext class.

```py
resolver = Richtext(your_custom_schema)
```

### Testing

We use unittest module for tests. You can execute the following task to run the tests:

```sh
$ python -m unittest discover storyblok_richtext/tests -v
```

## Contribution

Fork me on [Github](https://github.com/storyblok/storyblok-python-richtext-renderer)
