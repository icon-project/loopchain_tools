import os

from setuptools import setup, find_packages

version = os.environ.get('VERSION')

if version is None:
    with open(os.path.join('.', 'VERSION')) as version_file:
        version = version_file.read().strip()

setup_options = {
    'name': 'loopchain tools',
    'description': 'CLI tools for loopchain',
    'long_description': open('README.md').read(),
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/icon-project/loopchain_tools',
    'version': version,
    'author': 'ICON foundation',
    'author_email': 't_core@iconloop.com',
    'packages': find_packages(),
    'license': "Apache License 2.0",
    'install_requires': list(open('requirements.txt')),
    'classifiers': [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only'
    ]
}

setup(**setup_options)
