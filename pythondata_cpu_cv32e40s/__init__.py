import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post252"
version_tuple = (0, 5, 0, 252)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post252")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post110"
data_version_tuple = (0, 5, 0, 110)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post110")
except ImportError:
    pass
data_git_hash = "8816f407b153f4a68b696dda7bfb8cf9811d275b"
data_git_describe = "0.5.0-110-g8816f407"
data_git_msg = """\
commit 8816f407b153f4a68b696dda7bfb8cf9811d275b
Merge: 7e310bd8 9ddf5733
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 07:46:41 2022 +0200

    Merge pull request #315 from silabs-oivind/fix_issue_294
    
    Update PMPnCFG WARL behaviour. Fix for issue #294

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
