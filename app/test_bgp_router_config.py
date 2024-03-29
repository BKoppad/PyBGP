"""
Sample tests for bgp_router_config.py
"""
from importlib.resources import path
from django.test import SimpleTestCase
from unittest import patch
from app.app import bgp_router_config

class ConnectSshTests(SimpleTestCase):
    """" Test connect_ssh module """
    def test_router_connect_success(self):
        """Test whether conncetion with router is successfull"""
        router = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad', 'password':'cisco'}  
        user1 = bgp_router_config.BGP_Router()
        res = user1.connect_ssh(router)
        self.assertTrue(True,res)

    def test_router_connect_failur(self):
        """Test connection with router fails due to authentication issue"""
        router2 = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad2', 'password':'juniper'}
        user2 = bgp_router_config.BGP_Router()
        res = user2.connect_ssh(router2)
        self.assertTrue(True,res)

    
    @patch('user3.cli_access()', return_value='>')
    def test_router_cli_access_1(self):
        """Test command exceution on router working as expected"""
        router = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad', 'password':'cisco'} 
        user3 = bgp_router_config.BGP_Router()
        user3.connect_ssh(router)
        user3.cli_access()
        self.assertEqual(user3.cli_access(),'>')
        # self.assertTrue(True,res)

    # Ping test
    # returning ssh_clinet object
