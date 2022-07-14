import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post257"
version_tuple = (0, 4, 0, 257)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post257")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post115"
data_version_tuple = (0, 4, 0, 115)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post115")
except ImportError:
    pass
data_git_hash = "c52be100fd0768a9713fa37a5528fa81bc4258e8"
data_git_describe = "0.4.0-115-gc52be100"
data_git_msg = """\
commit c52be100fd0768a9713fa37a5528fa81bc4258e8
Merge: 6ea0aec5 1a490f9c
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Jul 14 10:14:32 2022 +0200

    Merge pull request #252 from silabs-hfegran/dev_hf_clic_manifest_update
    
    Added missing clic interrupt controller to manifest

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
