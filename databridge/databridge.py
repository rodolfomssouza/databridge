"""
Create a bridge between the data and the application.
"""

# Packages
import geopandas as gpd  # noqa
import pandas as pd  # noqa
import polars as pl  # noqa
import json
import os
from prettytable import PrettyTable


# %% Classes ------------------------------------------------------------------

class ConfigUpdater:
    def __init__(self, config_file='config.json'):
        # Get directory module
        module_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct path to config file
        self.config_file_path = os.path.join(module_dir, config_file)
        self.config_data = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file_path, 'r') as config_file:
                config_data = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Create file if it does not exist
            with open(self.config_file_path, 'w') as config_file:
                config_file.write("{}")
            config_data = {}
        return config_data

    def save_config(self):
        with open(self.config_file_path, 'w') as config_file:
            json.dump(self.config_data, config_file, indent=2)

    def update_config(self, environment, dataset_name, path, file, function):
        """
        Update config file

        Parameters
        ----------
        environment : str
            Environment name (e.g., local or server)
        dataset_name : str
            Dataset name (e.g., texas_county)
        path : str
            Absolute file path
        file : str
            File name
        function : str
            Function name to load data (e.g., pd.read_csv)
        """
        if environment not in self.config_data:
            self.config_data[environment] = {}

        self.config_data[environment][dataset_name] = {
            "path": path,
            "file": file,
            "function": function
        }

        self.save_config()


class DataBridge:
    def __init__(self, config_file='config.json'):
        # Get directory module
        module_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct path to config file
        self.config_file_path = os.path.join(module_dir, config_file)
        self.config_data = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file_path, 'r') as config_file:
                config_data = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Create file if it does not exist
            with open(self.config_file_path, 'w') as config_file:
                config_file.write("{}")
            config_data = {}
        return config_data

    def load_dataset(self, environment, dataset_name):
        """
        Load dataset from the config file

        Parameters
        ----------
        environment : str
            Environment name (e.g., local or server)
        dataset_name : str
            Dataset name (e.g., texas_county)
        """
        try:
            dataset_config = self.config_data[environment][dataset_name]
            dataset_path = dataset_config["path"]
            dataset_file = dataset_config["file"]
            dataset_function = dataset_config["function"]

            full_path = f"{dataset_path}{dataset_file}"
            dataset = eval(f"{dataset_function}('{full_path}')")

            return dataset
        except KeyError:
            raise ValueError(
                f"Dataset {dataset_name} in env {environment} not found.")

    def get_available_datasets(self, environment):
        return list(self.config_data.get(environment, {}).keys())

    def list_datasets(self):
        """
        Print a table with all datasets in the config file
        """
        table = PrettyTable()
        table.field_names = ["Environment",
                             "Dataset", "Path", "File"]
        for env, datasets in self.config_data.items():
            for dataset, config in datasets.items():
                table.add_row([env, dataset, config["path"], config["file"]])
        print(table)


# Create an instance of the class
config_updater = ConfigUpdater()
data_bridge = DataBridge()
