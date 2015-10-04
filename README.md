# CopyDir
A small toolset to copy a folder from a synched (dropbox type) folder to one linked to a git repo.

in Settings.py, set gitPath to the root path of where you keep your git-synched folders, syncPath to the shared folder, activeProjects is an array of folders that you want to keep in sync.

After that, run CopyToGit or CopyFromGit depending.  The copy algorithm tests for things like date and signature before copying, so as to prevent accidental erasure.  Might still have bugs, so use at own risks.  Refer to CopyDir.git and check the code to see all the checks made.

This is useful if you collaborate with someone who cannot use Git.  You can sync things with them that way.

chris@exequor.com
