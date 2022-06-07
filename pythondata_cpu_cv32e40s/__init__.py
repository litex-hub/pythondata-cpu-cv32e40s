import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post179"
version_tuple = (0, 4, 0, 179)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post179")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post37"
data_version_tuple = (0, 4, 0, 37)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post37")
except ImportError:
    pass
data_git_hash = "6c41ac941e61b6325183e6d9338af7778cce5e42"
data_git_describe = "0.4.0-37-g6c41ac94"
data_git_msg = """\
commit 6c41ac941e61b6325183e6d9338af7778cce5e42
Merge: e7586faf b28c2244
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jun 7 13:57:41 2022 +0200

    Merge pull request #222 from silabs-oysteink/silabs-oysteink_smstateen
    
    Implemented Smstateen for table jumps

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
