import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post183"
version_tuple = (0, 4, 0, 183)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post183")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post41"
data_version_tuple = (0, 4, 0, 41)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post41")
except ImportError:
    pass
data_git_hash = "d2bcb55a2ce432e3108d2337c0d55c1ebeae44c6"
data_git_describe = "0.4.0-41-gd2bcb55a"
data_git_msg = """\
commit d2bcb55a2ce432e3108d2337c0d55c1ebeae44c6
Merge: 20f63bd8 00bc245b
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Tue Jun 14 15:55:58 2022 +0200

    Merge pull request #233 from Silabs-ArjanB/ArjanB_dbg0
    
    Added dcsr.EBREAKU related explanations

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
