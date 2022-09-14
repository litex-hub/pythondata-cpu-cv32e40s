import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.5.0.post190"
version_tuple = (0, 5, 0, 190)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post190")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post48"
data_version_tuple = (0, 5, 0, 48)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post48")
except ImportError:
    pass
data_git_hash = "1144108c27a1bf0852c60959ea5004208af07628"
data_git_describe = "0.5.0-48-g1144108c"
data_git_msg = """\
commit 1144108c27a1bf0852c60959ea5004208af07628
Merge: 24521318 afbc5016
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Sep 14 15:05:50 2022 +0200

    Merge pull request #301 from silabs-oivind/fix_255_pmpaddr_n_rvfi
    
    Update for issue #255. Implement pmp_addr_n_r for RVFI.

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
