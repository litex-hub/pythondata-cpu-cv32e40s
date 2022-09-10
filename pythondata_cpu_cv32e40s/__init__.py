import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post187"
version_tuple = (0, 5, 0, 187)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post187")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post45"
data_version_tuple = (0, 5, 0, 45)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post45")
except ImportError:
    pass
data_git_hash = "245213180e683e63ab1047e735f6574c35c888af"
data_git_describe = "0.5.0-45-g24521318"
data_git_msg = """\
commit 245213180e683e63ab1047e735f6574c35c888af
Merge: ee43ee91 6d56c9ed
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Sep 8 19:23:23 2022 +0200

    Merge pull request #298 from silabs-oivind/merge_e40x
    
    Merge e40x

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
