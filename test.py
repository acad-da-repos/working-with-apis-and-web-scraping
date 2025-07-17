
import unittest
import requests
from unittest.mock import patch, Mock
from assignment import get_data_from_api, scrape_data_from_website

class TestWebData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_from_api(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        data = get_data_from_api('http://fakeapi.com')

        self.assertEqual(data, {'key': 'value'})

    @patch('requests.get')
    def test_scrape_data_from_website(self, mock_get):
        # Mock the website response
        mock_response = Mock()
        mock_response.content = '<html><body><p>Item 1</p><p>Item 2</p></body></html>'
        mock_get.return_value = mock_response

        items = scrape_data_from_website('http://fakewebsite.com')

        self.assertEqual(items, ['Item 1', 'Item 2'])

if __name__ == '__main__':
    unittest.main()
