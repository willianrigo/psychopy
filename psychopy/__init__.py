# Part of the PsychoPy library
# Copyright (C) 2010 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

#version info for PsychoPy
#This file is automatically generated during build (do not edit directly).
__version__='1.63.04'
__license__='GNU GPLv3 (or more recent equivalent)'
__author__='Jonathan Peirce'
__author_email__='jon@peirce.org.uk'
__maintainer_email__='psychopy-dev@googlegroups.com'
__url__='http://www.psychopy.org'
__downloadUrl__='http://code.google.com/p/psychopy/downloads'
__build_platform__='n/a'
__git_sha__='n/a'
if __git_sha__=='n/a':
    import subprocess
    #see if we're in a git repo and fetch from there
    repo_commit=False
    proc = subprocess.Popen('git rev-parse --short HEAD',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            cwd='.', shell=True)
    repo_commit, _ = proc.communicate()
    del proc#to get rid of the background process
    if repo_commit:
        __git_sha__=repo_commit.strip()#remove final linefeed

__all__ = ["gui", "misc", "visual", "core", "event", "data", "filters"]
