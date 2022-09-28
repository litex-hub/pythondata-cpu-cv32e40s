import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post213"
version_tuple = (0, 5, 0, 213)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post213")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post71"
data_version_tuple = (0, 5, 0, 71)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post71")
except ImportError:
    pass
data_git_hash = "582655667cfa68b830ba9a8e3e6caf7e35fcc76d"
data_git_describe = "0.5.0-71-g58265566"
data_git_msg = """\
commit 582655667cfa68b830ba9a8e3e6caf7e35fcc76d
Merge: 7568910d 611fa254
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Sep 28 10:30:53 2022 +0200

    Merge pull request #305 from silabs-oysteink/silabs-oysteink_lsu-integrity
    
    Added LSU integrity checking.

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
