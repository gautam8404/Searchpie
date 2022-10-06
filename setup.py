from setuptools import setup
from src._version import __version__

setup(
    name='searchpie',
    version=__version__,
    author='Gautam Dhingra',
    author_email="gautamdhingra8404@gmail.com",
    download_url='http://pypi.python.org/pypi/searchpie',
    description='A handy tool to search through Wikipedia, Tmdb and Mal.',
    long_description=open("README.md").read(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/gautam8404/Searchpie"
    },
    install_requires=[
        'wikipedia'
    ],
    entry_points={
        'console_scripts': ['searchpie=main:main']
    },
    python_requires='>=3.5'
)
