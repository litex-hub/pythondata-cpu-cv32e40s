import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post144"
version_tuple = (0, 4, 0, 144)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post144")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post2"
data_version_tuple = (0, 4, 0, 2)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post2")
except ImportError:
    pass
data_git_hash = "ecde3080f19bf519b280c19485b6c4398812c4fe"
data_git_describe = "0.4.0-2-gecde3080"
data_git_msg = """\
commit ecde3080f19bf519b280c19485b6c4398812c4fe
Merge: 55f20360 73111f11
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Jun 3 11:24:16 2022 +0200

    Merge pull request #216 from Silabs-ArjanB/ArjanB_clicu1
    
    Unifying interrupt controllers; aligning cs registers syntax with cor…

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
