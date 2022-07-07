import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post245"
version_tuple = (0, 4, 0, 245)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post245")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post103"
data_version_tuple = (0, 4, 0, 103)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post103")
except ImportError:
    pass
data_git_hash = "6d7b0de6f92d6a4d7ee22f5b85ffa0d49919d848"
data_git_describe = "0.4.0-103-g6d7b0de6"
data_git_msg = """\
commit 6d7b0de6f92d6a4d7ee22f5b85ffa0d49919d848
Merge: 1da7c409 27b31d3c
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Jul 7 15:06:49 2022 +0200

    Merge pull request #245 from silabs-oysteink/silabs-oysteink_merge-w27-2
    
    Merge from CV32E40X + PC hardening updates

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
