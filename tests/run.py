"""
Run tests
"""

# %% Packages -----------------------------------------------------------------
from databridge.databridge import ConfigUpdater


# Update config file
cfg = ConfigUpdater()

cfg.update_config(
    "local",
    "texas_boundaries",
    "/Users/rsouza/Documents/1-Projects/DataPrepBase/data/raw-data/",
    "Texas_State_Boundary.gpkg",
    "gpd.read_file"
)
