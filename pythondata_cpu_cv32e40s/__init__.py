import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.3.0.post392"
version_tuple = (0, 3, 0, 392)
try:
    from packaging.version import Version as V
    pversion = V("0.3.0.post392")
except ImportError:
    pass

# Data version info
data_version_str = "0.3.0.post250"
data_version_tuple = (0, 3, 0, 250)
try:
    from packaging.version import Version as V
    pdata_version = V("0.3.0.post250")
except ImportError:
    pass
data_git_hash = "9757b4230ba7f1d8e3bc2a47210878090b48974e"
data_git_describe = "0.3.0-250-g9757b423"
data_git_msg = """\
commit 9757b4230ba7f1d8e3bc2a47210878090b48974e
Merge: 16ddbc77 88db3e77
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Jun 2 11:57:44 2022 +0200

    Merge pull request #213 from silabs-oysteink/silabs-oysteink_mcounteren-doc
    
    Fixed description of mcounteren as that did not get properly merged in…

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
