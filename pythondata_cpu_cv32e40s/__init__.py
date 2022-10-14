import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post144"
version_tuple = (0, 6, 0, 144)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post144")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post2"
data_version_tuple = (0, 6, 0, 2)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post2")
except ImportError:
    pass
data_git_hash = "297083642dead29d855fdd53e03ada1875ff17cb"
data_git_describe = "0.6.0-2-g29708364"
data_git_msg = """\
commit 297083642dead29d855fdd53e03ada1875ff17cb
Merge: 3462ed20 f8715717
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Oct 14 15:28:55 2022 +0200

    Merge pull request #325 from silabs-oivind/doc_pmp_warl
    
    Add notes about PMPCFG and PMPADDR in user manual

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
