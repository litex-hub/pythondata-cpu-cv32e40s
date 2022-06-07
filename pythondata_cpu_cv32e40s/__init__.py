import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post163"
version_tuple = (0, 4, 0, 163)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post163")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post21"
data_version_tuple = (0, 4, 0, 21)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post21")
except ImportError:
    pass
data_git_hash = "87c19b479de5dccd5173407589b75ebc04642c17"
data_git_describe = "0.4.0-21-g87c19b47"
data_git_msg = """\
commit 87c19b479de5dccd5173407589b75ebc04642c17
Merge: b4695ee6 012736c8
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Tue Jun 7 09:26:15 2022 +0200

    Merge pull request #221 from Silabs-ArjanB/ArjanB_profi
    
    Reduced profiling infrastructure. Removed support for Zihpm and Zicntr

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
