import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post208"
version_tuple = (0, 5, 0, 208)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post208")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post66"
data_version_tuple = (0, 5, 0, 66)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post66")
except ImportError:
    pass
data_git_hash = "7568910d50da36509677aad69e8c109aeb45ce73"
data_git_describe = "0.5.0-66-g7568910d"
data_git_msg = """\
commit 7568910d50da36509677aad69e8c109aeb45ce73
Merge: 2e710384 7e370cc9
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Sep 26 10:27:59 2022 +0200

    Merge pull request #306 from Silabs-ArjanB/ArjanB_cpuctrl1
    
    Turned some security features to default on, changing the reset value…

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
