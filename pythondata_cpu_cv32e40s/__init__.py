import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40s"

# Module version
version_str = "0.3.0.post370"
version_tuple = (0, 3, 0, 370)
try:
    from packaging.version import Version as V
    pversion = V("0.3.0.post370")
except ImportError:
    pass

# Data version info
data_version_str = "0.3.0.post228"
data_version_tuple = (0, 3, 0, 228)
try:
    from packaging.version import Version as V
    pdata_version = V("0.3.0.post228")
except ImportError:
    pass
data_git_hash = "53bad81280c42516298b9cb5434f35cca6ef3bf0"
data_git_describe = "0.3.0-228-g53bad812"
data_git_msg = """\
commit 53bad81280c42516298b9cb5434f35cca6ef3bf0
Merge: 44dc900a 0afef109
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue May 31 18:55:56 2022 +0200

    Merge pull request #208 from silabs-oysteink/silabs-oysteink_tbljmp-fix1
    
    Dummy instructions could be marked as table jumps in the fetch stage…

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
