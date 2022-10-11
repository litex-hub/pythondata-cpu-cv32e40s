import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post276"
version_tuple = (0, 5, 0, 276)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post276")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post134"
data_version_tuple = (0, 5, 0, 134)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post134")
except ImportError:
    pass
data_git_hash = "e4c027ec95a1bdc4cc6226acce27373d7eee7815"
data_git_describe = "0.5.0-134-ge4c027ec"
data_git_msg = """\
commit e4c027ec95a1bdc4cc6226acce27373d7eee7815
Merge: d3b861cf 92cceeb5
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Oct 10 13:31:51 2022 +0200

    Merge pull request #321 from silabs-oivind/master
    
    Add missing LIB parameter for CSR

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
