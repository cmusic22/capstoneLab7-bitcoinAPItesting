import unittest
from unittest import TestCase
from unittest.mock import patch,call

import bitcoinAPI

class TestBitcoinAPI(TestCase):
	@patch('bitcoinAPI.request_rates')
	def test_dollars_to_target(self, mock_rates):
		mock_rate = 15.69420
		example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'EUR': mock_rate}}
		mock_rates.side_effect = [example_api_response]
		converted = bitcoinAPI.convert_dollars_to_target(100, 'EUR')
		self.assertEqual(1569.420,converted)

if __name__ == '__main__':
	unittest.main()