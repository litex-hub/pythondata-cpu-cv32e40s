import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post251"
version_tuple = (0, 4, 0, 251)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post251")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post109"
data_version_tuple = (0, 4, 0, 109)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post109")
except ImportError:
    pass
data_git_hash = "022ea425ad558588bfcf0b2c2c183f824f6972aa"
data_git_describe = "0.4.0-109-g022ea425"
data_git_msg = """\
commit 022ea425ad558588bfcf0b2c2c183f824f6972aa
Merge: 6d7b0de6 b4e4513f
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Jul 8 10:28:48 2022 +0200

    Merge pull request #246 from silabs-oysteink/silabs-oysteink_merge-w27-rvfi
    
    Self merging due to vacation season, should be reviewed later.

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
