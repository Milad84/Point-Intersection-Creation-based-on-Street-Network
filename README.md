
![Figure_1](https://github.com/Milad84/Point-Intersection-Creation-based-on-Street-Network/assets/38597478/e666d9be-4045-4d0d-94b8-b503a90cdd82)

# Creating Intersection Points from Street Segments

This repository contains scripts to identify and create intersection points from a given layer of street segments. Two approaches are provided: one using ArcPy and the other using open-source GIS libraries.

## Features

- **Input:** A street segment feature class or GeoDataFrame.
- **Output:** A feature class or shapefile containing intersection points.
- **Temporary Storage:** Uses a temporary file geodatabase for ArcPy and a user-specified directory for open-source GIS.

## ArcPy Approach

This script uses ArcPy to perform a spatial intersection and create intersection points from a street network.

### Features

- **Input:** A street segment feature class.
- **Output:** A feature class containing intersection points.
- **Temporary Storage:** Uses a temporary file geodatabase to store the output.

### Script Details

- **Input Street Feature Class:** The `streets_fc` variable should be updated with the path to your street layer.
- **Temporary File Geodatabase:** A file geodatabase is created at `C:/Temp/TempGDB.gdb` if it doesn't already exist.
- **Intersection Identification:** The `Intersect` tool is used to identify intersection points and save them to the specified feature class.

### Usage Instructions

1. **Update the Input Path:** Modify the `streets_fc` variable to point to your input street layer.
2. **Run the Script:** Execute the script in an ArcGIS Pro environment.
3. **Check Output:** The intersections will be saved in the `Intersections` feature class within the temporary file geodatabase.

## Open-source GIS Approach

This script uses Shapely and GeoPandas to create intersection points from a street network.

### Features

- **Input:** A street segment GeoDataFrame.
- **Output:** A shapefile containing intersection points.
- **Temporary Storage:** Uses a user-specified directory to store the output shapefile.

### Script Details

- **Input Street Feature Class:** Creates a realistic sample of a street network.
- **Intersection Identification:** The `intersects` method from Shapely is used to identify intersection points.
- **Output:** Prompts the user for a directory to save the output shapefile.

### Usage Instructions

1. **Run the Script:** Execute the script in a Python environment.
2. **Enter the Output Directory:** When prompted, enter the directory path where you want to save the intersection points shapefile.
3. **Check Output:** The intersections will be saved as `Intersection_Points.shp` in the specified directory.

## Libraries Used

### ArcPy Approach

1. `arcpy`: ArcPy is a Python site package for performing geographic data analysis, data conversion, data management, and map automation with ArcGIS.

### Open-source GIS Approach

1. `geopandas`: GeoPandas is an open-source project to make working with geospatial data in Python easier. It extends pandas to allow spatial operations on geometric types.
2. `shapely`: Shapely is a Python package for manipulation and analysis of planar geometric objects.
3. `matplotlib`: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

### Installation

Install the necessary libraries using pip:

```sh
pip install geopandas shapely matplotlib
