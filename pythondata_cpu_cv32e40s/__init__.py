import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post215"
version_tuple = (0, 5, 0, 215)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post215")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post73"
data_version_tuple = (0, 5, 0, 73)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post73")
except ImportError:
    pass
data_git_hash = "2178573acbaefa2330d24cdfe39657ec3b1dd3e3"
data_git_describe = "0.5.0-73-g2178573a"
data_git_msg = """\
commit 2178573acbaefa2330d24cdfe39657ec3b1dd3e3
Merge: 58265566 eb9f0fd9
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Sep 28 12:25:53 2022 +0200

    Merge pull request #308 from Silabs-ArjanB/ArjanB_rnddummyfreq
    
    Fixed cpuctrl.rnddummyfreq description

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
