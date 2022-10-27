import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post164"
version_tuple = (0, 6, 0, 164)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post164")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post22"
data_version_tuple = (0, 6, 0, 22)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post22")
except ImportError:
    pass
data_git_hash = "6ef4354dac60807511e83ec95a8c5ea6e1e5150d"
data_git_describe = "0.6.0-22-g6ef4354d"
data_git_msg = """\
commit 6ef4354dac60807511e83ec95a8c5ea6e1e5150d
Merge: 2878f7cb 55e5c909
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Oct 27 09:57:07 2022 +0200

    Merge pull request #331 from silabs-oysteink/minhv_fix-1
    
    Updates to mret/xinhv handling.

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
