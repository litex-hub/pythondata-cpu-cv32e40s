import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post211"
version_tuple = (0, 4, 0, 211)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post211")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post69"
data_version_tuple = (0, 4, 0, 69)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post69")
except ImportError:
    pass
data_git_hash = "f9932ac7075eab611ac418e357a011af81e999f6"
data_git_describe = "0.4.0-69-gf9932ac7"
data_git_msg = """\
commit f9932ac7075eab611ac418e357a011af81e999f6
Merge: 5c6057bf 4454d721
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jun 24 16:25:44 2022 +0200

    Merge pull request #238 from silabs-oysteink/silabs-oysteink_merge-w25-2
    
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
