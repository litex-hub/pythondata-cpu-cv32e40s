import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post219"
version_tuple = (0, 4, 0, 219)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post219")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post77"
data_version_tuple = (0, 4, 0, 77)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post77")
except ImportError:
    pass
data_git_hash = "59d63257587ca2a19224c081da450c614075c423"
data_git_describe = "0.4.0-77-g59d63257"
data_git_msg = """\
commit 59d63257587ca2a19224c081da450c614075c423
Merge: 81f51ffa 67dfb3c0
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Jun 27 09:16:30 2022 +0200

    Merge pull request #240 from Silabs-ArjanB/ArjanV_secsd
    
    Fix of secureseed*_n for RVFI

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
