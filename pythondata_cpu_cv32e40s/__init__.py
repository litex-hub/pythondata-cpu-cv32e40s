import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post250"
version_tuple = (0, 5, 0, 250)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post250")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post108"
data_version_tuple = (0, 5, 0, 108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post108")
except ImportError:
    pass
data_git_hash = "7e310bd8ea7cf4852afe698190b4a28ce0fd9400"
data_git_describe = "0.5.0-108-g7e310bd8"
data_git_msg = """\
commit 7e310bd8ea7cf4852afe698190b4a28ce0fd9400
Merge: ca96f595 08ba4107
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Sep 30 15:52:16 2022 +0200

    Merge pull request #313 from silabs-oysteink/silabs-oysteink_obi-data-counter
    
    Added separate OBI data interface counter for outstanding transaction.

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
