import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post152"
version_tuple = (0, 4, 0, 152)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post152")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post10"
data_version_tuple = (0, 4, 0, 10)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post10")
except ImportError:
    pass
data_git_hash = "b39deb561e8ed5506eaeec6db3d0ad4148c56908"
data_git_describe = "0.4.0-10-gb39deb56"
data_git_msg = """\
commit b39deb561e8ed5506eaeec6db3d0ad4148c56908
Merge: 17e60d8e 5516ac3e
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Jun 8 16:29:25 2022 +0200

    Merge pull request #226 from Silabs-ArjanB/ArjanB_misax
    
    Fix for issue #70

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
