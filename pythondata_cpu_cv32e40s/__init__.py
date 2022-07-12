import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post255"
version_tuple = (0, 4, 0, 255)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post255")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post113"
data_version_tuple = (0, 4, 0, 113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post113")
except ImportError:
    pass
data_git_hash = "6ea0aec538c3c3e2e00ebfb471c6b01e9de8a5b8"
data_git_describe = "0.4.0-113-g6ea0aec5"
data_git_msg = """\
commit 6ea0aec538c3c3e2e00ebfb471c6b01e9de8a5b8
Merge: 463bd7d1 305913be
Author: Henrik Fegran <henrik.fegran@silabs.com>
Date:   Tue Jul 12 09:33:40 2022 +0200

    Merge pull request #250 from silabs-hfegran/dev_hf_itrace_param
    
    Added parameter to disable itrace

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
