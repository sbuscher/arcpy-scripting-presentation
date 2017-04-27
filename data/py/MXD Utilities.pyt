import mxd_replace
reload(mxd_replace)
from mxd_replace import ReplaceDataSourceTool


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "MXD Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [ReplaceDataSourceTool]
