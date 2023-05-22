# Radio Format

Batch process audio files for use in the
[Radio Music](https://github.com/TomWhitwell/RadioMusic) (virtual radio module
for Eurorack)

## Virtualenv

### Creating the virtualenv

```sh
pyenv virtualenv 3.11.2 radio_format
pyenv local radio_format
```

This will create a virtualenv named radio_format, and activate it automatically
when changing directory into the project.

### Managing Dependencies

Manage dependencies with pipenv

```sh
pipenv shell
pipenv install
...
```

## Running Tests

```sh
ptw #from inside pipenv shell
```
