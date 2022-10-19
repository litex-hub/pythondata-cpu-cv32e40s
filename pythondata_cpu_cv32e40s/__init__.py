import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.6.0.post157"
version_tuple = (0, 6, 0, 157)
try:
    from packaging.version import Version as V
    pversion = V("0.6.0.post157")
except ImportError:
    pass

# Data version info
data_version_str = "0.6.0.post15"
data_version_tuple = (0, 6, 0, 15)
try:
    from packaging.version import Version as V
    pdata_version = V("0.6.0.post15")
except ImportError:
    pass
data_git_hash = "d6f68a6a7e2005a4968d1c9ade5d8b2416eafd7d"
data_git_describe = "0.6.0-15-gd6f68a6a"
data_git_msg = """\
commit d6f68a6a7e2005a4968d1c9ade5d8b2416eafd7d
Merge: 020677aa 836dac1b
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Oct 19 15:46:53 2022 +0200

    Merge pull request #329 from silabs-oivind/issue_227_assertion
    
    Add assertion for issue #277. mstatus.mprv is cleared when entering u…

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
