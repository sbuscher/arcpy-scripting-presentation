import os
import arcpy


def replace(from_fc, to_fc_path, to_fc_name):
    fc = os.path.join(to_fc_path, to_fc_name)

    if arcpy.Exists(fc):
        arcpy.Delete_management(fc)

    arcpy.FeatureClassToFeatureClass_conversion(from_fc, to_fc_path, to_fc_name)


if __name__ == "__main__":
    in_fc = arcpy.GetParameterAsText(0)
    out_fc_path = arcpy.GetParameterAsText(1)
    out_fc_name = arcpy.GetParameterAsText(2)

    replace(in_fc, out_fc_path, out_fc_name)
