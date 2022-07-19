import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post274"
version_tuple = (0, 4, 0, 274)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post274")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post132"
data_version_tuple = (0, 4, 0, 132)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post132")
except ImportError:
    pass
data_git_hash = "972b3616141140bb99f7bc9072450174c03f027a"
data_git_describe = "0.4.0-132-g972b3616"
data_git_msg = """\
commit 972b3616141140bb99f7bc9072450174c03f027a
Merge: fcca1616 1c566f81
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jul 19 08:45:54 2022 +0200

    Merge pull request #264 from Silabs-ArjanB/ArjanB_chk0
    
    Changed parity from odd to even for some of the achk and rchk signals

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
