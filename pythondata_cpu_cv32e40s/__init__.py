import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post283"
version_tuple = (0, 5, 0, 283)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post283")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post141"
data_version_tuple = (0, 5, 0, 141)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post141")
except ImportError:
    pass
data_git_hash = "0ac403b719ebb5096a34a82425caae7d0ac71303"
data_git_describe = "0.5.0-141-g0ac403b7"
data_git_msg = """\
commit 0ac403b719ebb5096a34a82425caae7d0ac71303
Merge: 83962afe fbe3a8f7
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 12 08:51:52 2022 +0200

    Merge pull request #323 from silabs-oysteink/random-hint
    
    Implemented random hint instructions

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
