import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post268"
version_tuple = (0, 5, 0, 268)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post268")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post126"
data_version_tuple = (0, 5, 0, 126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post126")
except ImportError:
    pass
data_git_hash = "4a9ff950f56136863eaff7a11baa83b73fcafab9"
data_git_describe = "0.5.0-126-g4a9ff950"
data_git_msg = """\
commit 4a9ff950f56136863eaff7a11baa83b73fcafab9
Merge: 736e1e42 a91905d2
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 15:25:03 2022 +0200

    Merge pull request #314 from silabs-oysteink/protocol_harden
    
    OBI protocol hardening

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
