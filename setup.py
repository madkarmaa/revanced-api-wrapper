import pathlib
from setuptools import setup, find_packages

setup(
    name = 'revanced_api_wrapper',
    version = '0.0.1',
    author = 'MadKarma',
    description = 'Python wrapper for the ReVanced API.',
    long_description_content_type = 'text/markdown',
    long_description = pathlib.Path('README.md').read_text('utf-8'),
    packages = find_packages(),
    include_package_data = True,
    url = 'https://github.com/madkarmaa/revanced-api-wrapper',
    license = 'MIT',
    python_requires = '>=3.10',
    install_requires = pathlib.Path('requirements.txt').read_text('utf-8').split('\n')
)