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
