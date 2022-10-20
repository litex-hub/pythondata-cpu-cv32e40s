import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post161"
version_tuple = (0, 6, 0, 161)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post161")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post19"
data_version_tuple = (0, 6, 0, 19)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post19")
except ImportError:
    pass
data_git_hash = "2878f7cba028fb201f4a84bc1feea5059813d503"
data_git_describe = "0.6.0-19-g2878f7cb"
data_git_msg = """\
commit 2878f7cba028fb201f4a84bc1feea5059813d503
Merge: d6f68a6a 3fd58d5b
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Oct 20 09:59:11 2022 +0200

    Merge pull request #330 from silabs-oivind/merge_cv32e40x
    
    Merge cv32e40x

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
