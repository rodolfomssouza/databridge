# tests/test_config_updater.py

import unittest
import json
import os
from databridge.databridge import ConfigUpdater
from databridge.databridge import DataBridge


class TestConfigUpdater(unittest.TestCase):
    def setUp(self):
        # Set up any initial conditions for the tests
        self.config_updater = ConfigUpdater(
            config_file='test_config.json')

    # def tearDown(self):
    #     # Clean up after each test (e.g., remove created files)
    #     if os.path.exists('databridge/test_config.json'):
    #         os.remove('databridge/test_config.json')

    def test_update_config(self):
        # Add or update a dataset
        self.config_updater.update_config(
            environment="test",
            dataset_name="test_dataset",
            path="databridge/datasets/",
            file="demo.csv",
            function="pd.read_csv"
        )

        # Check if the config file is created
        self.assertTrue(os.path.isfile('databridge/test_config.json'))

        # Load the content of the config file
        with open('databridge/test_config.json', 'r') as config_file:
            config_data = json.load(config_file)

        # Check if the dataset is added or updated
        expected_data = {
            "test": {
                "test_dataset": {
                    "path": "databridge/datasets/",
                    "file": "demo.csv",
                    "function": "pd.read_csv"
                }
            }
        }
        self.assertEqual(config_data, expected_data)


class TestLoadData(unittest.TestCase):
    def setUp(self):
        # Set up any initial conditions for the tests
        self.data_bridge = DataBridge(
            config_file='test_config.json')

    def tearDown(self):
        # Clean up after each test (e.g., remove created files)
        if os.path.exists('databridge/test_config.json'):
            os.remove('databridge/test_config.json')

    def test_load_dataset(self):
        df = self.data_bridge.load_dataset(
            environment="test",
            dataset_name="test_dataset"
        )
        self.assertEqual(df.shape, (6, 2))


if __name__ == '__main__':
    unittest.main()
