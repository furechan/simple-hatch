# noinspection PyUnresolvedReferences

import re

from pathlib import Path
from invoke import task  # type: ignore

PACKAGE = "simple-hatch"
ROOTDIR = Path(__file__).parent


@task
def setup(ctx):
    """Install package with extras"""
    ctx.run('pip install -e ".[dev]"')


@task
def clean(ctx):
    """Clean project dist"""
    ctx.run("rm -rf dist")


@task(clean)
def build(ctx):
    """Build project wheel"""
    ctx.run("pip install -q build")
    ctx.run("python -mbuild --wheel")
    ctx.run("python -mbuild --sdist")


@task
def dump(ctx):
    """Dump wheel contents"""
    for file in ROOTDIR.glob("dist/*.tar.gz"):
        ctx.run(f"tar -tf {file}")
    for file in ROOTDIR.glob("dist/*.whl"):
        ctx.run(f"unzip -l {file}")


