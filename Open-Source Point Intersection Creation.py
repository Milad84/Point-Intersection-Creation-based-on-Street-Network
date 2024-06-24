import geopandas as gpd
from shapely.geometry import LineString, Point
import matplotlib.pyplot as plt
import os

# Create a realistic sample of a street network
lines = [
    LineString([(0, 0), (10, 0)]),
    LineString([(0, 1), (10, 1)]),
    LineString([(0, 2), (10, 2)]),
    LineString([(1, -1), (1, 3)]),
    LineString([(2, -1), (2, 3)]),
    LineString([(3, -1), (3, 3)]),
]

# Create a GeoDataFrame for the street network
gdf_lines = gpd.GeoDataFrame(geometry=lines)
gdf_lines.crs = "EPSG:4326"  # Set the coordinate reference system

# Function to find intersections
def find_intersections(gdf):
    intersections = []
    for i, line1 in enumerate(gdf.geometry):
        for j, line2 in enumerate(gdf.geometry):
            if i < j:  # Avoid comparing the same lines and repeating comparisons
                if line1.intersects(line2):
                    intersection = line1.intersection(line2)
                    if isinstance(intersection, Point):
                        intersections.append(intersection)
                    elif isinstance(intersection, LineString):
                        # If the intersection is a LineString (overlapping lines), add the endpoints
                        intersections.extend([Point(intersection.coords[0]), Point(intersection.coords[-1])])
    return intersections

# Find intersections
intersections = find_intersections(gdf_lines)

# Create a GeoDataFrame for the intersections
gdf_intersections = gpd.GeoDataFrame(geometry=intersections)
gdf_intersections.crs = "EPSG:4326"  # Set the coordinate reference system

# Ask user for the output directory path
output_dir = input("Enter the directory where you want to save the intersection points shapefile: ")

# Ensure the directory exists and is writable
if not os.path.exists(output_dir):
    print(f"Error: The directory {output_dir} does not exist.")
elif not os.access(output_dir, os.W_OK):
    print(f"Error: The directory {output_dir} is not writable.")
else:
    # Define the output shapefile path
    output_shapefile = os.path.join(output_dir, "Intersection_Points.shp")

    # Save the intersections to a shapefile
    gdf_intersections.to_file(output_shapefile)
    print(f"Intersection points saved to {output_shapefile}")

    # Verify the file was saved
    if os.path.exists(output_shapefile):
        print(f"The file {output_shapefile} was created successfully.")
    else:
        print(f"Error: The file {output_shapefile} was not created.")

# Plot the street network and intersections
fig, ax = plt.subplots()
gdf_lines.plot(ax=ax, color='blue', linewidth=2)
gdf_intersections.plot(ax=ax, color='red', marker='o', markersize=50)
plt.show()

# Print the intersection points
print(gdf_intersections)
