import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post142"
version_tuple = (0, 4, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post0"
data_version_tuple = (0, 4, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post0")
except ImportError:
    pass
data_git_hash = "55f20360d57beb8bfd5495b0c5982b33763c923e"
data_git_describe = "0.4.0-0-g55f20360"
data_git_msg = """\
commit 55f20360d57beb8bfd5495b0c5982b33763c923e
Merge: 39b6ffbc 48426dc5
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Jun 2 13:21:43 2022 +0200

    Merge pull request #215 from silabs-oysteink/silabs-oysteink-merge-w22-2
    
    Silabs oysteink merge w22 2

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
