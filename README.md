# Script for Creating Intersection Points from Street Segments

This script identifies and creates intersection points from any street segment layer. It uses ArcPy to perform a spatial intersection and outputs the intersection points to a specified temporary file geodatabase.

## Features

- **Input:** A street segment feature class.
- **Output:** A feature class containing intersection points.
- **Temporary Storage:** Uses a temporary file geodatabase to store the output.

## Script Details

- **Input Street Feature Class:** The `streets_fc` variable should be updated with the path to your street layer.
- **Temporary File Geodatabase:** A file geodatabase is created at `C:/Temp/TempGDB.gdb` if it doesn't already exist.
- **Intersection Identification:** The `Intersect` tool is used to identify intersection points and save them to the specified feature class.

## Usage Instructions

1. **Update the Input Path:** Modify the `streets_fc` variable to point to your input street layer.
2. **Run the Script:** Execute the script in an ArcGIS Pro environment.
3. **Check Output:** The intersections will be saved in the `Intersections` feature class within the temporary file geodatabase.

## Libraries Used

1. `arcpy` - ArcPy is a site package that provides a port and an extension to the ArcGIS Spatial Analyst extension.
2. `os` - This module provides a portable way of using operating system-dependent functionality.

## Example Code

```python
import arcpy
import os

# Define the input street feature class
streets_fc = "CTN_AFP"  # Update with your street layer

# Create a temporary file geodatabase
temp_gdb = "C:/Temp/TempGDB.gdb"
if not arcpy.Exists(temp_gdb):
    arcpy.management.CreateFileGDB(os.path.dirname(temp_gdb), os.path.basename(temp_gdb))
print("Temporary file geodatabase created.")

# Define the output feature class for intersections
intersections_fc = os.path.join(temp_gdb, "Intersections")

try:
    # Identify intersection points
    arcpy.analysis.Intersect([streets_fc], intersections_fc, 
                             join_attributes="ALL", 
                             output_type="POINT")
    print("Intersections identified and created successfully.")

except arcpy.ExecuteError as e:
    print(f"Error: {e}")
    arcpy.AddError(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    arcpy.AddError(e)

