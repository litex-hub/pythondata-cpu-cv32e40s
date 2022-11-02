import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post175"
version_tuple = (0, 6, 0, 175)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post175")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post33"
data_version_tuple = (0, 6, 0, 33)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post33")
except ImportError:
    pass
data_git_hash = "68a94befb5771e8b29ce445cfcf2de6de5877cb4"
data_git_describe = "0.6.0-33-g68a94bef"
data_git_msg = """\
commit 68a94befb5771e8b29ce445cfcf2de6de5877cb4
Merge: 6ef4354d b6d632d8
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Nov 2 09:28:37 2022 +0100

    Merge pull request #332 from silabs-oysteink/silabs-oysteink_merge-w44-1
    
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
