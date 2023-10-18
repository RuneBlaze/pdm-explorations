# PDM explorations

This repo contains the following
Python packages `pdm-test` and `baser`, with the following dependency relationship.

```
pdm-test (lives in private index) ---> baser (lives in private index)
                                  |
                                  |-->  typer (lives in public pypi)
```

`staticserver` contains a minimal PyPI server hosting both private
packages. The goal here is to show that even though both
`pdm-test` and `baser` are hosted in the private PyPI index,
`pdm-test` can be installed via pip.

## Getting started

Start a Python >= 3.10 environment, and then:

```shell
cd staticserver
python server.py
```

In a new terminal window, install `pdm-test` from the private index (either input auth username `pusheen` with password `stormy` interactively or store the credentials in `.netrc`):

```shell
pip install --extra-index-url http://localhost:8000/ pdm-test
```

`pdm-test` exports a single CLI interface: `collatz`, which simulates the collatz conjecture. Use this CLI to check that the installation works:

```
$ collatz 10000
collatz number of 10000 is 29
```

## `staticserver`

In `staticserver`, run `server.py` to start a private PyPI index at

```
http://localhost:8000/
# with credentials:
http://pusheen:stormy@localhost:8000/
```

The username is `pusheen` and the password is `stormy`.

This index has `pdm-test` and `baser` pre-uploaded. (They can be
deleted and manually uploaded. This is not a "true" PyPI index
because one can only manually upload packages).

## `baser`

This is only a toy PDM-managed package exporting a single function to be used by `pdm-test`. Its only purpose
is to serve as a dependency to `pdm-test`.

## `pdm-test`

Main package. It has dynamic version (see `pdm-test/version.py`) and other public dependencies.

```toml
# dynamic version
[project]
dynamic = ["version"]

[tool.pdm.version]
source = "call"
getter = "version:get_version" # the getter of version
```

It also specifies a private index:

```toml
# private index
[[tool.pdm.source]]
name = "private"
url = "http://${PYPI_USERNAME}:${PYPI_PASSWORD}@localhost:8000/"
```

(`PYPI_USERNAME=pusheen PYPI_PASSWORD=stormy` will set the credentials for pdm commands).