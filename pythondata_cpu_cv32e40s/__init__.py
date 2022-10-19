import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post155"
version_tuple = (0, 6, 0, 155)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post155")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post13"
data_version_tuple = (0, 6, 0, 13)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post13")
except ImportError:
    pass
data_git_hash = "020677aaf6dec3fb04e13cee9dbb0679d8e5ab15"
data_git_describe = "0.6.0-13-g020677aa"
data_git_msg = """\
commit 020677aaf6dec3fb04e13cee9dbb0679d8e5ab15
Merge: 51abba01 40f30d2f
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 19 08:41:04 2022 +0200

    Merge pull request #328 from silabs-oysteink/silabs-oysteink_merge-w42-1
    
    Merge from CV32E40X.

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
