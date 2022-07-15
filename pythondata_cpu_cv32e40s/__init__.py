import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post259"
version_tuple = (0, 4, 0, 259)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post259")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post117"
data_version_tuple = (0, 4, 0, 117)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post117")
except ImportError:
    pass
data_git_hash = "26b419dc079ddaa509dcd16062eeda0d70744847"
data_git_describe = "0.4.0-117-g26b419dc"
data_git_msg = """\
commit 26b419dc079ddaa509dcd16062eeda0d70744847
Merge: c52be100 fe941ae5
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jul 15 08:12:56 2022 +0200

    Merge pull request #253 from Silabs-ArjanB/ArjanB_todofl
    
    Added todos related to recent PRs

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
