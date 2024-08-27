import unittest
from src.lead_time_demand import calculate_lead_time_demand

class TestLeadTimeDemand(unittest.TestCase):

    def test_lead_time_demand(self):
        lead_times = 10
        products_sold = 200
        stock_levels = 50
        result = calculate_lead_time_demand(lead_times, products_sold, stock_levels)
        self.assertAlmostEqual(result, 40)

if __name__ == '__main__':
    unittest.main()
