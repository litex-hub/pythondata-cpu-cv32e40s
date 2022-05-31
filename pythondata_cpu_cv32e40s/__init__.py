import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.3.0.post368"
version_tuple = (0, 3, 0, 368)
try:
    from packaging.version import Version as V
    pversion = V("0.3.0.post368")
except ImportError:
    pass

# Data version info
data_version_str = "0.3.0.post226"
data_version_tuple = (0, 3, 0, 226)
try:
    from packaging.version import Version as V
    pdata_version = V("0.3.0.post226")
except ImportError:
    pass
data_git_hash = "44dc900af60d123ec47305697a940604d011291c"
data_git_describe = "0.3.0-226-g44dc900a"
data_git_msg = """\
commit 44dc900af60d123ec47305697a940604d011291c
Merge: f85e7129 c7ae092c
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue May 31 16:14:55 2022 +0200

    Merge pull request #207 from silabs-oysteink/silabs-oysteink_merge-csr-refactor
    
    Silabs oysteink merge csr refactor

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
