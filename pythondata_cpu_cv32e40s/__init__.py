import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post157"
version_tuple = (0, 4, 0, 157)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post157")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post15"
data_version_tuple = (0, 4, 0, 15)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post15")
except ImportError:
    pass
data_git_hash = "74a830e1625ce0f64e563d935a929aa241bec3d7"
data_git_describe = "0.4.0-15-g74a830e1"
data_git_msg = """\
commit 74a830e1625ce0f64e563d935a929aa241bec3d7
Merge: b52070b8 01061f72
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jun 3 15:12:57 2022 +0200

    Merge pull request #219 from silabs-oysteink/silabs-oysteink_merge-w22-3
    
    Merge from cv32e40x

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
