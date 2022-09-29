import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post218"
version_tuple = (0, 5, 0, 218)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post218")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post76"
data_version_tuple = (0, 5, 0, 76)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post76")
except ImportError:
    pass
data_git_hash = "6c0bfb77384238f6e5166747c6c068776655caa7"
data_git_describe = "0.5.0-76-g6c0bfb77"
data_git_msg = """\
commit 6c0bfb77384238f6e5166747c6c068776655caa7
Merge: 2178573a 01a501c6
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Thu Sep 29 12:41:38 2022 +0200

    Merge pull request #309 from Silabs-ArjanB/ArjanB_ingr0
    
    Redefined integrity check feature. Impact on major alert changed. Dep…

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
