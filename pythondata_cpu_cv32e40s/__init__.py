import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post272"
version_tuple = (0, 5, 0, 272)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post272")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post130"
data_version_tuple = (0, 5, 0, 130)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post130")
except ImportError:
    pass
data_git_hash = "4f08c0490f93da2f32b7f937b23d349a2aa56edf"
data_git_describe = "0.5.0-130-g4f08c049"
data_git_msg = """\
commit 4f08c0490f93da2f32b7f937b23d349a2aa56edf
Merge: 3bf3aa78 ede8ee81
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 5 13:59:48 2022 +0200

    Merge pull request #318 from silabs-oysteink/issue_293
    
    Fix for issue #293.

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
