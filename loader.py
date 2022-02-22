# Example Code
# There is no guarantee or otherwise support for the following code.
# It is here for demonstration purposes, and to spark ideas.
# Running this without understanding what each part does is dangerous.

# You are on your own.


import os

# This example code utilized Terminus plugins pancackes and rsync

org = "Your Org ID"
ups = "Upstream ID"
crt  = "site:create"

# Originally in Demo
# Site Lable | Site Name | Region | Tag
# sites = [["Site 1 Label", "site1", "au", "Autoload"],
#          ["Site 1 Label EU", "site1-eu", "eu", "Autoload"],
#          ["Site 2 Label EU", "site2-au", "eu", "Autoload"]]

# Updated
# Site Lable | Site Name | Region | Tag | OLD URL | Asset Path
sites = [["Site 1 Label", "site1", "au", "Autoload", "<OLDSITE>", "/wp-content/uploads/assets1au.zip"],
         ["Site 1 Label EU", "site1-eu", "eu", "Autoload", "<OLDSITE>", "/wp-content/uploads/assets1eu.zip"],
         ["Site 2 Label EU", "site2-au", "eu", "Autoload", "<OLDSITE>", "/wp-content/uploads/assets2eu.zip"]]

for site in sites:

    lbl = site[0]
    nam = site[1]
    rgn = site[2]
    tag = site[3]
    old = site[4]
    ast = site[5]


    
    trmns_create = "terminus " + crt + " --org=" + org + " --region=" + rgn + "  " + nam + "  \"" + lbl + "\"  " + ups

    trmns_db = "terminus pc " + nam + ".dev --app=mysql < " + nam + ".sql"
    trmns_db_clean = "terminus wp " + nam + ".dev search-replace " + old + " '/'"

    trmns_content = "terminus rsync ./" + nam + "/content/. " + nam + ".dev:code/wp-content"

    # this is an error: The url should not be hard coded.
    trmns_files = "terminus import:files " + nam + ".dev " + old + ast + " --yes"

    trmns_tag = "terminus tag:add " + nam + " " + org + " " + tag

    trmns_git = "terminus connection:set " + nam + ".dev git --yes"
    trmns_cc = "terminus env:clear-cache " + nam + ".dev"

    os.system(trmns_create)
    os.system(trmns_db)
    os.system(trmns_db_clean)
    os.system(trmns_content)
    os.system(trmns_files)
    os.system(trmns_tag)
    os.system(trmns_git)
    os.system(trmns_cc)


