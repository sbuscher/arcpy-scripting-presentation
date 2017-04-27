import os
import arcpy


class ReplaceDataSourceTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Replace MXD data sources"
        self.description = "Swap out data sources in an MXD."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""

        in_mxd = arcpy.Parameter(
                displayName="Source Map Document",
                name="input_mxd",
                # datatype="DEFile",
                datatype="GPString",
                parameterType="Required",
                direction="Input")

        out_mxd_folder = arcpy.Parameter(
                displayName="Output MXD folder",
                name="output_mxd",
                #datatype="DEFolder",
                datatype="GPString",
                parameterType="Required",
                direction="Input")

        out_mxd_file = arcpy.Parameter(
                displayName="MXD file name (include extension)",
                name="mxd_file",
                datatype="GPString",
                parameterType="Required",
                direction="Input")

        data_source = arcpy.Parameter(
                displayName="New data source",
                name="new_data_source",
                datatype="GPString",
                #datatype="DEWorkspace",
                parameterType="Required",
                direction="Input")

        return [in_mxd, out_mxd_folder, out_mxd_file, data_source]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        new_mxd = os.path.join(parameters[1].valueAsText,
                               parameters[2].valueAsText)

        replace_data_sources(
                parameters[0].valueAsText,
                new_mxd,
                parameters[3].valueAsText)

        return


def replace_data_sources(in_mxd, out_mxd, new_source):
    # Create an in-memory version of the input mxd
    mxd = arcpy.mapping.MapDocument(in_mxd)

    # Fetch list of mxd layers
    layers = arcpy.mapping.ListLayers(mxd)

    # Swap the data source
    for layer in layers:
        layer.findAndReplaceWorkspacePath(layer.workspacePath, new_source)
        arcpy.AddMessage("Replaced {} data source.".format(layer.name))

    # Save a new mxd to the desired path
    arcpy.AddMessage("Creating new MXD.")
    mxd.saveACopy(out_mxd)

    arcpy.AddMessage("Replacements completed successfully")

    # The input mxd is never saved so its connections are not altered
    # Free up the in-memory mxd
    del mxd

if __name__ == "__main__":
    in_mxd = arcpy.GetParameterAsText(0)
    out_mxd = arcpy.GetParameterAsText(1)
    workspace = arcpy.GetParameterAsText(2)

    replace_data_sources(in_mxd, out_mxd, workspace)
