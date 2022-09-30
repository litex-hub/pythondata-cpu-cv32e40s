import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post246"
version_tuple = (0, 5, 0, 246)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post246")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post104"
data_version_tuple = (0, 5, 0, 104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post104")
except ImportError:
    pass
data_git_hash = "ca96f5954096ffde5fcec4264f810da70364f74b"
data_git_describe = "0.5.0-104-gca96f595"
data_git_msg = """\
commit ca96f5954096ffde5fcec4264f810da70364f74b
Merge: 505a8b41 6033f829
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Sep 30 12:15:37 2022 +0200

    Merge pull request #312 from Silabs-ArjanB/ArjanB_RMZC
    
    Removed reference to unsupported Zcmb extension

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
