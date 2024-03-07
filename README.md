# databridge

The `databridge` package streamlines the management of common datasets across diverse projects.
It facilitates the setup of paths, file names, and Python commands to access centralized files efficiently.

## Why Use databridge?

Managing common datasets across multiple projects often involves repetitive tasks such as saving files, configuring paths, and importing libraries.
The `databridge` package aims to simplify this process by offering a centralized data bucket.

Instead of manually saving files and configuring paths for each project, `databridge` allows you to create a `config.json` file.
This file guides Python on where to locate common datasets locally, reducing redundancy and enhancing efficiency.

## Example 1 - Without databridge

```python
# Import geopandas package
import geopandas as gpd

# Import data
texas_boundaries = gpd.read_file("myproject_data_folder/Texas_boundaries.shp")
```

This method is straightforward but can become repetitive when dealing with multiple projects.


## Example 2 - with databrigde

```python
# Import databridge package
from databridge.databridge import data_bridge as db

# List all available datasets
db.list_datasets()

# Load dataset
texas_boundaries = db.load_dataset("local", "texas_boundaries")
```

Although Example 2 has the same number of line of code as Example 1, it significantly reduces redundancy.
When dealing with multiple projects, you no longer need to save the file multiple times or manually set different paths.

Explore the power of `databridge` to enhance your workflow and centralize your datasets effortlessly.

## How to configure databridge?

To configure `databridge`, you need to create a `config.json` file in the same location where the `databridge` package is installed.
The `config.json` file should contain the following structure:

```json
{
  "local": {
    "dataset_name": {
        "path": "absolute path to dataset file",
        "file": "file name including extension",
        "function": "function to load the dataset (e.g., gpd.read_file)"
    },
    "texas_boundaries": {
        "path": "C:/Users/username/Documents/myproject_data_folder",
        "file": "Texas_boundaries.shp",
        "function": "gpd.read_file"
  }
}
```

The package has a built-in method to create the `config.json` file.

```python
# Import databridge package
from databridge.databridge import config_updater as cfu

# Update config.json file
cfu.update_config(
    environment="local",
    dataset_name="texas_boundaries",
    path="C:/Users/username/Documents/myproject_data_folder",
    file="Texas_boundaries.shp",
    function="gpd.read_file"
    )

# Save the updated config.json file
cfu.save_config()
```

The `config.json` file is now updated with the new dataset information.

## How to use databridge?

To use `databridge`, you need to install the package and import the `DataBridge` class.

```python
# Import databridge package
from databridge.databridge import data_btidge as db

# List all available datasets
db.list_datasets()

# Load dataset
df = db.load_dataset("local", "texas_boundaries")
```