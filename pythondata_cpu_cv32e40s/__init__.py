import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post181"
version_tuple = (0, 4, 0, 181)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post181")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post39"
data_version_tuple = (0, 4, 0, 39)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post39")
except ImportError:
    pass
data_git_hash = "20f63bd87c6fe7d50d61abcef1a2867bd7d4ebb5"
data_git_describe = "0.4.0-39-g20f63bd8"
data_git_msg = """\
commit 20f63bd87c6fe7d50d61abcef1a2867bd7d4ebb5
Merge: 84eeb991 86ec0da5
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jun 14 12:51:50 2022 +0200

    Merge pull request #232 from silabs-oysteink/silabs-oysteink_merge-w24-3
    
    Silabs oysteink merge w24 3

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
