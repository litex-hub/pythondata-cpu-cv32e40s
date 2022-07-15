import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.4.0.post262"
version_tuple = (0, 4, 0, 262)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post262")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post120"
data_version_tuple = (0, 4, 0, 120)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post120")
except ImportError:
    pass
data_git_hash = "d11f4a036f2e8ed322188b3460ea27f2f228b585"
data_git_describe = "0.4.0-120-gd11f4a03"
data_git_msg = """\
commit d11f4a036f2e8ed322188b3460ea27f2f228b585
Merge: 26b419dc adc412cf
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Jul 15 12:18:13 2022 +0200

    Merge pull request #254 from Silabs-ArjanB/ArjanB_244
    
    Fix for PMPADDR

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
