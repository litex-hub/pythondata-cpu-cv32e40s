import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post244"
version_tuple = (0, 5, 0, 244)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post244")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post102"
data_version_tuple = (0, 5, 0, 102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post102")
except ImportError:
    pass
data_git_hash = "505a8b41389fbddf30c9c8c38ab215fb72537bf0"
data_git_describe = "0.5.0-102-g505a8b41"
data_git_msg = """\
commit 505a8b41389fbddf30c9c8c38ab215fb72537bf0
Merge: 7bc96f03 1932aeb9
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Sep 29 17:27:23 2022 +0200

    Merge pull request #310 from silabs-oysteink/silabs-oysteink_instr_lsu-fix
    
    Fixes for issue #307

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
