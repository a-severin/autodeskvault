import unittest
from autodeskvault import generate_service_urls, VaultServices, connect


class TestAutodeskvault(unittest.TestCase):
    def test_generate_service_urls(self):
        services = generate_service_urls('test.com', 'test_resource', 8787, 'http2', 32)

        self.assertIsNotNone(services)
        self.assertTrue(all([key.value in services for key in VaultServices]), f'services = {len(services)} VaultServices = {len(VaultServices)}')

if __name__ == "__main__":
    unittest.main()
