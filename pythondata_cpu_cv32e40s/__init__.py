import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.3.0.post363"
version_tuple = (0, 3, 0, 363)
try:
    from packaging.version import Version as V
    pversion = V("0.3.0.post363")
except ImportError:
    pass

# Data version info
data_version_str = "0.3.0.post221"
data_version_tuple = (0, 3, 0, 221)
try:
    from packaging.version import Version as V
    pdata_version = V("0.3.0.post221")
except ImportError:
    pass
data_git_hash = "f85e7129b586302333d85316e5421a731d396940"
data_git_describe = "0.3.0-221-gf85e7129"
data_git_msg = """\
commit f85e7129b586302333d85316e5421a731d396940
Merge: f9e957cc 65bf5e79
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri May 27 15:26:18 2022 +0200

    Merge pull request #205 from silabs-oysteink/silabs-oysteink_tbljmp-hardening
    
    Added PC hardening for table jumps. Both the pointer fetch and the ju…

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
