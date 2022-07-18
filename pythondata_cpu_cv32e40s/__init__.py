import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post270"
version_tuple = (0, 4, 0, 270)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post270")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post128"
data_version_tuple = (0, 4, 0, 128)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post128")
except ImportError:
    pass
data_git_hash = "70793cc8e187fcc2c49a752402af82efd1df958d"
data_git_describe = "0.4.0-128-g70793cc8"
data_git_msg = """\
commit 70793cc8e187fcc2c49a752402af82efd1df958d
Merge: c70bf4e1 70ceb3aa
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 12:56:45 2022 +0200

    Merge pull request #261 from Silabs-ArjanB/ArjanB_249b
    
    PMP fix (additional fix for issue 249)

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
