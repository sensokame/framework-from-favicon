from framework_favicon.database import *
import os 
from typing import Callable
import logging
from rich.logging import RichHandler
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
default_logger = logging.getLogger("framework_favicon_logger")
default_logger.setLevel()
dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, "database.json")

def obj_dict(obj):
    return obj.__dict__

hash = str
framework = str
def deserialize_hashes(logger: logging.Logger = default_logger) -> dict[hash, framework]:
    import json
    res = {}
    for framework in json.load(open(database_location, 'r').read()).items():
        res[framework["hash"]] = framework["framework"]
    found = len(res) 
    if found:
        logger.info(f'database has {found} hashes.')
    else:
        logger.warn(f'no hash is found in the database, results may be invalid.')
    return res

def get_error(resource: str) -> str:
    return f'could not determine framework for {resource} based on favicon provided' \
        "please try other ways to determine the framework, "\
        "if you do manage to determine the favicon, update the OWASP database if possible\n" \
            'database can be found in {hashes_url}'

def get_info(resource: str, name: str) -> str:
    return f'framework {name} found for resource {resource}'



def handle_response(resource: str, action: Callable[[str], GrabResult],logger: logging.Logger= default_logger ) -> None:
    response = action(resource)
    if response.status == Status.STATUS_OK:
        logger.info(get_info(resource, response.data))
    if response.status == Status.STATUS_NOT_FOUND:
        logger.error(get_error(resource))

def serialize_hashes(frameworks: list[FrameworkHash]) -> None:
    import json
    open(database_location, "w").write(json.dumps(frameworks, default=obj_dict))

def get_hashes(logger: logging.Logger = default_logger) -> str:
    import urllib.request
    logger.info(f'attempting to get hash database from {hashes_url}')
    content = urllib.request.urlopen(hashes_url).read()
    if content: 
        logger.info(f'managed to retrieve answer from website, parsing data')
    else:
        logger.warn(f'unable to update, falling back on existing database version, results may be invalid')
        return ''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    return str(soup.pre)

def update_hashes_database(logger: logging.Logger = default_logger) -> None:
    logger.info("updating database")
    lis = []
    for line in get_hashes().splitlines():
        hash, framework = line.split(':')
        lis.append(FrameworkHash(framework, hash))
    found = len(lis)
    if (found):
        logger.info(f'found {found} hashes, overwriting existing database')
        serialize_hashes(lis)
        logger.info("database updated")
    else:
        logger.warn(f'could not find any database, falling back on previous database version')

def show_database(logger: logging.Logger = default_logger) -> None:
    logger.info(f'database contains {len(database.framworks)} entries: ')
    res = ""
    for h, f in database.framworks:
        res += f"\t{f}:{h}\n"
    logger.info(res)
    logger.info("happy hacking")
