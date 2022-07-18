import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post268"
version_tuple = (0, 4, 0, 268)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post268")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post126"
data_version_tuple = (0, 4, 0, 126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post126")
except ImportError:
    pass
data_git_hash = "c70bf4e1121589c09edb4d0d51e8f599abaf1c03"
data_git_describe = "0.4.0-126-gc70bf4e1"
data_git_msg = """\
commit c70bf4e1121589c09edb4d0d51e8f599abaf1c03
Merge: c86152d1 580f52b6
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 11:43:50 2022 +0200

    Merge pull request #260 from Silabs-ArjanB/ArjanB_242
    
    Fixed two bus related to the combination of debug mode and user level…

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
