import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post239"
version_tuple = (0, 5, 0, 239)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post239")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post97"
data_version_tuple = (0, 5, 0, 97)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post97")
except ImportError:
    pass
data_git_hash = "7bc96f031a4661f9877619f74e2e1e932d85ede4"
data_git_describe = "0.5.0-97-g7bc96f03"
data_git_msg = """\
commit 7bc96f031a4661f9877619f74e2e1e932d85ede4
Merge: 6c0bfb77 9f04d8ee
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Sep 29 16:20:06 2022 +0200

    Merge pull request #311 from silabs-oysteink/silabs-oysteink_merge_w39-1
    
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
