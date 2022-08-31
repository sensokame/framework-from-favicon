import argparse
from os import path
import sys
from framework_favicon.database import data
from utils import *
from grabbers import *

from framework_favicon.utils import update_hashes_database
def main_cli():
    """
    Main function. Expected to be run from CLI and used
    only in automated context.
    """
    parser = argparse.ArgumentParser(description="Framework Guesser from favicon")
    parser.add_argument('-h', '--help', action='store_true', help='Display help page')
    parser.add_argument('-u', '--url', action='append', help='website url from which to get favicon')
    parser.add_argument('-f', '--file', action='append', help='faveicon file, could be local or url')
    parser.add_argument('-d', '--data', action='append', help='faveicon file data, not recommended to use, but what the hell')
    parser.add_argument('-m', '--md5', action='append', help='faveicon md5 hash')
    parser.add_argument('--update', action='store_true', help='update the hashes database')
    parser.add_argument("show_database", action='store_true', help='show the current database')

    args = parser.parse_known_args()
    if len(sys.argv)==1 or args.help:
        parser.print_help()
        return 0
    if parser.update or not path.exists(database_location):
        update_hashes_database()
    # make sure data is up to date
    database.update_frameworks()
    if parser.show_database:
        show_database()
    
    if parser.url:
        for url in parser.url:
            handle_response(url, grab_favicon_from_website)
    if parser.file:
        for file in parser.file:
            handle_response(file, grab_favicon_from_file)
    if parser.data:
        for data in parser.data:
            handle_response(data, grab_favicon_from_data)
    if parser.md5:
        for md5 in parser.md5:
            handle_response(md5, grab_favicon_from_md5)

