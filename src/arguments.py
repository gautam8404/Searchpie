import argparse
import sys
from argparse import ArgumentParser
from _version import __version__


def arguments():
    parser = ArgumentParser(prog="searchpie",
                            description="A handy tool to search through Wikipedia, Tmdb and Mal from command line",
                            usage="%(prog)s [-h] [-v,--version]", formatter_class=argparse.RawDescriptionHelpFormatter)

    arg_help = parser.add_argument_group(title="Search Flags", description="""
    -a, --anime <query>   searches mal for anime name 
    -b --manga <query>   searches mal for manga name 
    -m --movies <query>   searches tmdb for movie name
    -t --tv <query>   searches tmdb for tv show name
    -w --wiki <query>   searches wiki for wikipedia article


    searching TMDB for movies or TV shows requires tmdb api key, get your api key here:
    https://developers.themoviedb.org/3/getting-started/introduction

    In order to set api key use `searchpie --set-tmdb-key <your api key>`
    """)

    identifiers = parser.add_mutually_exclusive_group()

    parser.add_argument("default_method", metavar="default_query", type=str, nargs='*',
                             help="Searches in Default Method if no Search Flag provided")
    identifiers.add_argument("-a", "--anime", dest="anime", help=argparse.SUPPRESS, action='store', metavar='',
                             type=str,
                             nargs='+')
    identifiers.add_argument("-b", "--manga", dest="manga", help=argparse.SUPPRESS, action='store', metavar='',
                             type=str,
                             nargs='+')
    identifiers.add_argument("-m", "--movie", dest="movie", help=argparse.SUPPRESS, action='store', metavar='',
                             type=str,
                             nargs='+')
    identifiers.add_argument("-t", "--tv", dest="tv", help=argparse.SUPPRESS, action='store', metavar='', type=str,
                             nargs='+')
    identifiers.add_argument("-w", "--wiki", dest="wiki", help=argparse.SUPPRESS, action='store', metavar='', type=str,
                             nargs='+')
    identifiers.add_argument("-v", '--version', action='version',
                             version='%(prog)s {version}'.format(version=__version__))

    options = parser.add_mutually_exclusive_group()

    options.add_argument("-o", "--open", dest="browser", action='store_true', help="Opens page in browser")
    options.add_argument("-p", dest="pages", action='store', metavar="pages", default=1,
                         help="Number of results to be displayed, displays upto 10 results")
    options.add_argument("--set-default", dest="default", action='store_true', help="changes default method")
    options.add_argument("--show-default", dest="show_def", action='store_true', help="shows default method")
    options.add_argument("--set-tmdb-key", dest="key", action='store', help="changes api key for tmdb")

    if not len(sys.argv) > 1:
        parser.print_help()
        return None

    return parser.parse_args()
