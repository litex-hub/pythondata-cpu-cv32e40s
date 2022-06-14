import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post174"
version_tuple = (0, 4, 0, 174)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post174")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post32"
data_version_tuple = (0, 4, 0, 32)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post32")
except ImportError:
    pass
data_git_hash = "bed221ae98e9f0c4371ce2091039877bfb8ec8dd"
data_git_describe = "0.4.0-32-gbed221ae"
data_git_msg = """\
commit bed221ae98e9f0c4371ce2091039877bfb8ec8dd
Merge: 597ae2d9 bb0cc419
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Tue Jun 14 11:32:19 2022 +0200

    Merge pull request #229 from Silabs-ArjanB/ArjanB_stl
    
    PMP, WARL, style updates

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
