import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post154"
version_tuple = (0, 4, 0, 154)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post154")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post12"
data_version_tuple = (0, 4, 0, 12)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post12")
except ImportError:
    pass
data_git_hash = "150e924186a63b3db2f6080870ccf8f867144208"
data_git_describe = "0.4.0-12-g150e9241"
data_git_msg = """\
commit 150e924186a63b3db2f6080870ccf8f867144208
Merge: b39deb56 3c6b1c26
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Jun 10 09:34:04 2022 +0200

    Merge pull request #227 from silabs-oysteink/silabs-oysteink_csr-rd-error-fix
    
    Tied off CLIC CSR rd_error signals when SMCLIC=0.

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
