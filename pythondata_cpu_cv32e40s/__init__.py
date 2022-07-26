import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post280"
version_tuple = (0, 4, 0, 280)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post280")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post138"
data_version_tuple = (0, 4, 0, 138)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post138")
except ImportError:
    pass
data_git_hash = "2a72ce47742aca2870ab2340dc5d468abadc5829"
data_git_describe = "0.4.0-138-g2a72ce47"
data_git_msg = """\
commit 2a72ce47742aca2870ab2340dc5d468abadc5829
Merge: cdf2304c c35076ca
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jul 26 11:37:34 2022 +0200

    Merge pull request #268 from Silabs-ArjanB/ArjanB_196
    
    Fix for issue 196

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
