import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post150"
version_tuple = (0, 4, 0, 150)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post150")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post8"
data_version_tuple = (0, 4, 0, 8)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post8")
except ImportError:
    pass
data_git_hash = "17e60d8ec04629eed9309e3903304fc4ecd8dc9e"
data_git_describe = "0.4.0-8-g17e60d8e"
data_git_msg = """\
commit 17e60d8ec04629eed9309e3903304fc4ecd8dc9e
Merge: 6c41ac94 6cf7861a
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Jun 8 12:48:34 2022 +0200

    Merge pull request #225 from silabs-oysteink/silabs-oysteink_merge-w23-2
    
    Merge from CV32E40X

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
