import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post217"
version_tuple = (0, 4, 0, 217)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post217")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post75"
data_version_tuple = (0, 4, 0, 75)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post75")
except ImportError:
    pass
data_git_hash = "81f51ffab8253a9ae8977d67693db468153cc6cd"
data_git_describe = "0.4.0-75-g81f51ffa"
data_git_msg = """\
commit 81f51ffab8253a9ae8977d67693db468153cc6cd
Merge: f9932ac7 10865870
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jun 27 08:49:30 2022 +0200

    Merge pull request #239 from silabs-oysteink/silabs-oysteink_merge-w26-1
    
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
