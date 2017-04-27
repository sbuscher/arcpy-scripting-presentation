import arcpy


def main(in_mxd, out_mxd, out_connection):
    # Create an in-memory version of the input mxd
    mxd = arcpy.mapping.MapDocument(in_mxd)

    # Perform connection replacements on feature classes and tables
    replace_layer_workspaces(mxd, out_connection)

    # Save a new mxd to the desired path
    mxd.saveACopy(out_mxd)

    arcpy.AddMessage("Replacements completed successfully")

    # The input mxd is never saved so its connections are not altered
    # Free up the in-memory mxd
    del mxd

    return


def replace_layer_workspaces(mxd, source):
    # Fetch the mxd layers
    layers = arcpy.mapping.ListLayers(mxd)

    # Swap the data source
    for layer in layers:
        layer.findAndReplaceWorkspacePath(layer.workspacePath, source)
        arcpy.AddMessage("Replaced {} data source.".format(layer.name))

    return

if __name__ == "__main__":
    # Get parameter values
    input_mxd = arcpy.GetParameterAsText(0)
    output_mxd = arcpy.GetParameterAsText(1)
    data_source = arcpy.GetParameterAsText(2)

    # Execute the script
    main(input_mxd, output_mxd, data_source)

