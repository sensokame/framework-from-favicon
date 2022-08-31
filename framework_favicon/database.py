import enum
from utils import deserialize_hashes

# the website url from where to grab the favicon hashes.
hashes_url = "https://wiki.owasp.org/index.php/OWASP_favicon_database"

class FrameworkHash:
    def __init__(self, framework: str, hash: str)-> None:
        self.framework = framework
        self.hash = hash

class Status(enum.Enum):
    STATUS_OK = 0
    STATUS_NOT_FOUND = -1

class GrabResult:
    def __init__(self, status: Status, data: str):
        self.status = status
        self.data = data

class database:
    framworks = deserialize_hashes()
    def update_frameworks():
        database.framworks = deserialize_hashes()