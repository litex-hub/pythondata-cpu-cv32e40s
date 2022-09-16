import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post194"
version_tuple = (0, 5, 0, 194)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post194")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post52"
data_version_tuple = (0, 5, 0, 52)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post52")
except ImportError:
    pass
data_git_hash = "d115a782563527abe9cfd983bba4cfc65eae1893"
data_git_describe = "0.5.0-52-gd115a782"
data_git_msg = """\
commit d115a782563527abe9cfd983bba4cfc65eae1893
Merge: 1144108c cb8181e0
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Sep 16 10:32:55 2022 +0200

    Merge pull request #303 from silabs-oivind/impl_pma_integrity_2
    
    Implement PMA integrity

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
