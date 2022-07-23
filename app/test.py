"""
Sample tests for bgp_router_config.py
"""
from django.test import SimpleTestCase
from app import bgp_router_config

class ConnectSshTests(SimpleTestCase):
    """" Test connect_ssh module """
    """Test whether the routers are configured with ssh"""
    def test_router_connect(self):
        router = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad', 'password':'cisco'}  
        res = bgp_router_config.connect_ssh(router)
        self.assertEqual(res,bgp_router_config.ssh_client)

    # Ping test
    # returning ssh_clinet object
