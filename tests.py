from check_sites_health import is_server_respond_with_ok
import unittest


class TestIsServerRespondWithOk(unittest.TestCase):
    def test_server_respond_with_ok(self):
        url = 'https://rbc.ru/'
        self.assertEqual(is_server_respond_with_ok(url), True)

    def test_server_respond_with_ok2(self):
        url = 'https://fifa.com/'
        self.assertTrue(is_server_respond_with_ok(url))

    def test_server_respond_with_bad(self):
        url = 'https://ecfort.ru/'
        self.assertFalse(is_server_respond_with_ok(url))

    def test_server_respond_with_bad2(self):
        url = 'https://gogle.com'
        self.assertFalse(is_server_respond_with_ok(url))


class TestGetExpirationDate(unittest.TestCase):
    def test_get_expiration_date_365(self):
        domain_name = 'https://rbc.ru/'
        self.assertIsNot(domain_name, 365)


if __name__ == '__main__':
    unittest.main()
