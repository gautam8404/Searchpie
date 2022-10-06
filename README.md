# Searchpie
A handy tool to search through Wikipedia, Tmdb and Mal.

# Table Of Contents

- [Searchpie](#searchpie)
- [Table Of Contents](#table-of-contents)
- [Installation](#installation)
    - [Install From Pip](#install-using-pip)
    - [Install From Source](#install-from-source)
- [Usage](#usage)
- [Credits](#credits)


# Installation

## Install Using Pip
    
    pip install searchpie

## Install From Source

    python3 -m pip install --upgrade build
    git clone https://github.com/gautam8404/Searchpie
    cd Searchpie


    python3 -m build
    cd dist

This will create a dist package in directory

    dist/
    ├── searchpie_gautam8404-0.0.1-py3-none-any.whl
    └── searchpie_gautam8404-0.0.1.tar.gz

After that install using pip

    pip install searchpie_gautam8404-0.0.1-py3-none-any.whl

# Usage

Searchpie requires TMDb Api Key to search for movies and tv shows you can get it [here](https://www.themoviedb.org/settings/api) although you can use searchpie without that too





    searchpie [identifier_flag] <query> [option_flag]

Example:
    
    searchpie -m fight club -p 2

- `-m` flag tells searchpie to look into movies data
- `-p` flag tells searchpie to fetch 2 results, upto 10 results can be fetched

Incase identifier flag is not provided searchpie will look into default search method, it can be changed using:


    searchpie --set-default

For full help use

    searchpie --help



# Credits

- [wikipedia module](https://github.com/goldsmith/Wikipedia/)
- [jikan.moe](https://github.com/jikan-me)