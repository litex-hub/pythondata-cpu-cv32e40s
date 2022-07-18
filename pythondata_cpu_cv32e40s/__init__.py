import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post266"
version_tuple = (0, 4, 0, 266)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post266")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post124"
data_version_tuple = (0, 4, 0, 124)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post124")
except ImportError:
    pass
data_git_hash = "c86152d136ff86d3d674a6291fff2a25e734aa08"
data_git_describe = "0.4.0-124-gc86152d1"
data_git_msg = """\
commit c86152d136ff86d3d674a6291fff2a25e734aa08
Merge: 33734528 38ed6a0b
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 11:06:52 2022 +0200

    Merge pull request #259 from Silabs-ArjanB/ArjanB_249
    
    PMP fix (issue 249)

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
