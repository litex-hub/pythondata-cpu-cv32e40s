import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post278"
version_tuple = (0, 4, 0, 278)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post278")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post136"
data_version_tuple = (0, 4, 0, 136)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post136")
except ImportError:
    pass
data_git_hash = "cdf2304c714ecbe6b731089b5a84f28d5dba0fdb"
data_git_describe = "0.4.0-136-gcdf2304c"
data_git_msg = """\
commit cdf2304c714ecbe6b731089b5a84f28d5dba0fdb
Merge: 87e0c256 f349ac23
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jul 26 10:37:47 2022 +0200

    Merge pull request #267 from Silabs-ArjanB/ArjanB_wres
    
    Added WARL resolution functions. Minimizing diff with 40X

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
