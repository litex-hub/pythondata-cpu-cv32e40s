import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post171"
version_tuple = (0, 4, 0, 171)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post171")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post29"
data_version_tuple = (0, 4, 0, 29)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post29")
except ImportError:
    pass
data_git_hash = "ea3dfac41f469ed9d7fd8a9d3c3f7a22bb8b5170"
data_git_describe = "0.4.0-29-gea3dfac4"
data_git_msg = """\
commit ea3dfac41f469ed9d7fd8a9d3c3f7a22bb8b5170
Merge: 87c19b47 40205ff1
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jun 7 12:25:40 2022 +0200

    Merge pull request #224 from silabs-oysteink/silabs-oysteink_merge-w23-1
    
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
