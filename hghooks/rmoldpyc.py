#!/usr/bin/env python

"""Mercurial hooks to clean-up the code in the repository.
"""

import os
import os.path


def rmoldpyc():
    """ Searches subdirectories of the current directory looking for
        .pyc files which do not have matching .py files, and deletes
        them.

        This is useful as a hook for version control when Python files
        are moved.  It is dangerous for projects that deliberately
        include Python binaries without source.

        This code was written by Oddthinking and made public on
        StackOverflow:

        http://stackoverflow.com/questions/2528283/automatically-deleting-pyc-files-when-corresponding-py-is-moved-mercurial
    """
    print 'Running rmoldpyc hook.'
    for root, dirs, files in os.walk("."):
        pyc_files = filter(lambda filename: filename.endswith(".pyc"), files)
        py_files = set(filter(lambda filename: filename.endswith(".py"), files))
        excess_pyc_files = filter(lambda pyc_filename: pyc_filename[:-1] not in py_files, pyc_files)
        for excess_pyc_file in excess_pyc_files:
            full_path = os.path.join(root, excess_pyc_file)
            print "Removing old .pyc file:", full_path
            os.remove(full_path)
    return False # Tell Mercurial to carry on, if this is a controlling hook.

if __name__ == '__main__':
    rmoldpyc()
