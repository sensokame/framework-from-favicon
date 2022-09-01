import unittest
from framework_favicon.grab_result import Status
from framework_favicon.grabbers import grab_favicon_from_file
from framework_favicon.utils import update_hashes_database
from framework_favicon.database import database
from values import *

class TestGrabbers(unittest.TestCase):
    def setUp(self):
        # make sure that the database is up to date
        update_hashes_database()
        database.update_frameworks()
        
    def test_local_file_grabber(self):
        result = grab_favicon_from_file(favicon_file_location_test)
        self.assertEqual(result.status, Status.STATUS_OK)
        pass

if __name__ == "__main__":
    unittest.main()