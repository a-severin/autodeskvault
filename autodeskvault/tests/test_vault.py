from unittest import TestCase

from autodeskvault import generate_service_urls, VaultServices, connect


class TestAutodeskvault(TestCase):
    def test_generate_service_urls(self):
        services = generate_service_urls('test.com', 'test_resource', 8787, 'http2', 32)

        self.assertIsNotNone(services)
        self.assertTrue(all([key.value in services for key in VaultServices]))
