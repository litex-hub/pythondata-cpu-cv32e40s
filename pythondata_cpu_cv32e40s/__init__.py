import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post264"
version_tuple = (0, 4, 0, 264)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post264")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post122"
data_version_tuple = (0, 4, 0, 122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post122")
except ImportError:
    pass
data_git_hash = "33734528ed27ad2df86ee1055173f3047d9c1649"
data_git_describe = "0.4.0-122-g33734528"
data_git_msg = """\
commit 33734528ed27ad2df86ee1055173f3047d9c1649
Merge: d11f4a03 6cd941bb
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 09:48:21 2022 +0200

    Merge pull request #258 from Silabs-ArjanB/ArjanB_248
    
    RVFI fix for issue 248 (wrong rvfi_dbg)

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
