import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.3.0.post372"
version_tuple = (0, 3, 0, 372)
try:
    from packaging.version import Version as V
    pversion = V("0.3.0.post372")
except ImportError:
    pass

# Data version info
data_version_str = "0.3.0.post230"
data_version_tuple = (0, 3, 0, 230)
try:
    from packaging.version import Version as V
    pdata_version = V("0.3.0.post230")
except ImportError:
    pass
data_git_hash = "9a80ba87ce22ed8d4039d7dde7e01378830a8895"
data_git_describe = "0.3.0-230-g9a80ba87"
data_git_msg = """\
commit 9a80ba87ce22ed8d4039d7dde7e01378830a8895
Merge: 53bad812 cf4c866d
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Jun 1 12:55:28 2022 +0200

    Merge pull request #210 from Silabs-ArjanB/ArjanB_uretx
    
    Removed reference to uret

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
