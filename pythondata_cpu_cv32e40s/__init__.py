import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post264"
version_tuple = (0, 5, 0, 264)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post264")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post122"
data_version_tuple = (0, 5, 0, 122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post122")
except ImportError:
    pass
data_git_hash = "736e1e4253b50ed550bf6adeebc6fd71cf19dca4"
data_git_describe = "0.5.0-122-g736e1e42"
data_git_msg = """\
commit 736e1e4253b50ed550bf6adeebc6fd71cf19dca4
Merge: 8816f407 ebec85ec
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 10:13:19 2022 +0200

    Merge pull request #316 from silabs-oysteink/silabs-oysteink_merge-w40-1
    
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
