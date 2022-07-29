import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post284"
version_tuple = (0, 4, 0, 284)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post284")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post142"
data_version_tuple = (0, 4, 0, 142)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post142")
except ImportError:
    pass
data_git_hash = "bbebeb502897b715bc5b84835dfeb4199ba79993"
data_git_describe = "0.4.0-142-gbbebeb50"
data_git_msg = """\
commit bbebeb502897b715bc5b84835dfeb4199ba79993
Merge: ed92096c a7d4b796
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jul 29 12:18:17 2022 +0200

    Merge pull request #271 from Silabs-ArjanB/ArjanB_intgr1
    
    Added integrity and pcharden bits in cpuctrl CSR. Redefined integrity…

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
