import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post148"
version_tuple = (0, 4, 0, 148)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post148")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post6"
data_version_tuple = (0, 4, 0, 6)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post6")
except ImportError:
    pass
data_git_hash = "b52070b8427b52f3c177b581d4f34c6f3cc6ebc3"
data_git_describe = "0.4.0-6-gb52070b8"
data_git_msg = """\
commit b52070b8427b52f3c177b581d4f34c6f3cc6ebc3
Merge: 44597e3c f20917b1
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Jun 3 13:44:49 2022 +0200

    Merge pull request #218 from Silabs-ArjanB/ArjanB_csrh
    
    Fixed CSR hardening

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
