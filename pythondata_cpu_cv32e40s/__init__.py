import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post272"
version_tuple = (0, 4, 0, 272)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post272")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post130"
data_version_tuple = (0, 4, 0, 130)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post130")
except ImportError:
    pass
data_git_hash = "fcca1616576762304d5e323c49b505c0c284558a"
data_git_describe = "0.4.0-130-gfcca1616"
data_git_msg = """\
commit fcca1616576762304d5e323c49b505c0c284558a
Merge: 70793cc8 c3cb5b93
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 18 13:51:26 2022 +0200

    Merge pull request #263 from Silabs-ArjanB/ArjanB_mrv
    
    Added reset value for rvfi_mode

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
