import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post274"
version_tuple = (0, 5, 0, 274)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post274")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post132"
data_version_tuple = (0, 5, 0, 132)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post132")
except ImportError:
    pass
data_git_hash = "d3b861cf7763e744c99da74178014db674b7d283"
data_git_describe = "0.5.0-132-gd3b861cf"
data_git_msg = """\
commit d3b861cf7763e744c99da74178014db674b7d283
Merge: 4f08c049 1d115f01
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Oct 6 15:08:21 2022 +0200

    Merge pull request #319 from Silabs-ArjanB/ArjanB_pcs
    
    Simplified meaning of debug_pc_* interface

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40s."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40s".format(f))
    return fn
