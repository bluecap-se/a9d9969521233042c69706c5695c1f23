# a9d9969521233042c69706c5695c1f23

[![Travis](https://img.shields.io/travis/bluecap-se/a9d9969521233042c69706c5695c1f23.svg)](https://travis-ci.org/bluecap-se/a9d9969521233042c69706c5695c1f23)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue.svg)
![Platform](https://img.shields.io/badge/platform-docker-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Install and run

### Run with Docker

The preferred method is to run the project inside a Docker container.

```
$ git clone git@github.com:bluecap-se/a9d9969521233042c69706c5695c1f23.git
$ cd a9d9969521233042c69706c5695c1f23
$ docker-compose up -d
$ open http://127.0.0.1:8000/
```

## Run tests

Tests can be run in Docker with this command:

```
$ docker exec poker_app python manage.py test
```

## License

Published under [MIT License](https://github.com/bluecap-se/a9d9969521233042c69706c5695c1f23/blob/develop/LICENSE).
