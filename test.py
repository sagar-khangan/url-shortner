import os
import unittest
from helper import *
from run import app
from db import *
import sqlite3


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass 

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_raw_url(self):
        raw_url = get_raw_url('http://localhost:5000/04A7')
        self.assertEqual(raw_url,'www.facebook.com')

    def test_get_all_url(self):
        urls = get_all_url()
        self.assertEqual(urls[0],'http://localhost:5000/04A7')

    def test_del_short_url(self):
        resp = del_short_url('http://localhost:5000/03EA')
        self.assertEqual(resp,None)



if __name__ == "__main__":
    init_db('test_db.db')
    unittest.main()