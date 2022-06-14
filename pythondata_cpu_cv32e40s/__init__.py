import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post156"
version_tuple = (0, 4, 0, 156)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post156")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post14"
data_version_tuple = (0, 4, 0, 14)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post14")
except ImportError:
    pass
data_git_hash = "d12bfca79a20d6b64138fd43344fe9c3797ec02f"
data_git_describe = "0.4.0-14-gd12bfca7"
data_git_msg = """\
commit d12bfca79a20d6b64138fd43344fe9c3797ec02f
Merge: 150e9241 ae2bceae
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Jun 14 10:49:33 2022 +0200

    Merge pull request #228 from silabs-oysteink/silabs-oysteink_merge-w24-1
    
    Cherry picked commit for addition of Smstateen CSRs from CV32E40X.

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
