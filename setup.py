import pathlib
import os
from setuptools import setup, find_packages

# FIXME: "python -m build" not working

ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

def parse_requirements() -> list[str]:
    return pathlib.Path(os.path.join(ROOT_DIR, 'requirements.txt')).read_text('utf-8').split('\n')

setup(
    name = 'revanced_api_wrapper',
    version = '0.0.1',
    author = 'MadKarma',
    description = 'Python wrapper for the ReVanced API.',
    long_description_content_type = 'text/markdown',
    long_description = pathlib.Path(os.path.join(ROOT_DIR, 'README.md')).read_text('utf-8'),
    packages = find_packages(),
    include_package_data = True,
    url = 'https://github.com/madkarmaa/revanced-api-wrapper',
    license = 'MIT',
    python_requires = '>=3.10',
    install_requires = parse_requirements()
)