import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post142"
version_tuple = (0, 6, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post0"
data_version_tuple = (0, 6, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post0")
except ImportError:
    pass
data_git_hash = "3462ed208034635ac81cfffe6dd616c3fc4c196a"
data_git_describe = "0.6.0-0-g3462ed20"
data_git_msg = """\
commit 3462ed208034635ac81cfffe6dd616c3fc4c196a
Merge: 0ac403b7 5a41c42b
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 12 09:52:11 2022 +0200

    Merge pull request #324 from silabs-oysteink/silabs-oysteink_merge-w41
    
    Merge from CV32E40X

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
