import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post230"
version_tuple = (0, 4, 0, 230)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post230")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post88"
data_version_tuple = (0, 4, 0, 88)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post88")
except ImportError:
    pass
data_git_hash = "1da7c4097158094915073c7a89be5fb48549f907"
data_git_describe = "0.4.0-88-g1da7c409"
data_git_msg = """\
commit 1da7c4097158094915073c7a89be5fb48549f907
Merge: 59d63257 b8de6df5
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Mon Jul 4 08:02:29 2022 +0200

    Merge pull request #241 from silabs-oysteink/silabs-oysteink_merge-w27
    
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
