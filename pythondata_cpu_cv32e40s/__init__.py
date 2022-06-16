import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post185"
version_tuple = (0, 4, 0, 185)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post185")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post43"
data_version_tuple = (0, 4, 0, 43)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post43")
except ImportError:
    pass
data_git_hash = "31047a80e4ec5ebee1cf7a41fdbf9cfdf46a77fe"
data_git_describe = "0.4.0-43-g31047a80"
data_git_msg = """\
commit 31047a80e4ec5ebee1cf7a41fdbf9cfdf46a77fe
Merge: d2bcb55a 27cfbede
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Jun 16 07:32:18 2022 +0200

    Merge pull request #234 from Silabs-ArjanB/ArjanB_pmp0
    
    Tied off PMP related signals when PMP not fully configured

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
