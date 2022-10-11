import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post279"
version_tuple = (0, 5, 0, 279)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post279")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post137"
data_version_tuple = (0, 5, 0, 137)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post137")
except ImportError:
    pass
data_git_hash = "83962afe4fee3d36be396c88e192aa89510f6a81"
data_git_describe = "0.5.0-137-g83962afe"
data_git_msg = """\
commit 83962afe4fee3d36be396c88e192aa89510f6a81
Merge: e4c027ec 8b75a1df
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 11 10:32:10 2022 +0200

    Merge pull request #322 from silabs-oysteink/dummy-instr-fixes
    
    Dummy instruction fixes

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
