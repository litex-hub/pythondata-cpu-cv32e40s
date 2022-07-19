import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post276"
version_tuple = (0, 4, 0, 276)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post276")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post134"
data_version_tuple = (0, 4, 0, 134)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post134")
except ImportError:
    pass
data_git_hash = "87e0c256a1b025318758f8d6deb0b51d066f42b5"
data_git_describe = "0.4.0-134-g87e0c256"
data_git_msg = """\
commit 87e0c256a1b025318758f8d6deb0b51d066f42b5
Merge: 972b3616 081c23cb
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jul 19 10:53:51 2022 +0200

    Merge pull request #266 from Silabs-ArjanB/ArjanB_chk1
    
    Added notes on checksum behavior for sub-word transactions

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
