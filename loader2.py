# Example Code
# There is no guarantee or otherwise support for the following code.
# It is here for demonstration purposes, and to spark ideas.
# Running this without understanding what each part does is dangerous.

# You are on your own.

import os

# This example code utilized Terminus plugins pancakes and rsync

org = "<ORG_UUID>"
up_stream = "<UPSTREAM_UUID>"

# Site Label | Site Name | Region | Tags | OLD URL | Asset Path | Absolute Path
sites = [["Site 1 AU", "site1-au", "au", ["Autoload", "Australia"], "<OLD_URL>", "<ASSETS_FILE>", "'<ABSOLUTE_PATTERN>'"],
         ["Site 1 EU", "site1-eu", "eu", ["Autoload", "Europe"], "<OLD_URL>", "<ASSETS_FILE>", "'<ABSOLUTE_PATTERN>'"],
         ["Site 2 EU", "site2-au", "eu", ["Autoload", "Europe"], "<OLD_URL>", "<ASSETS_FILE>", "'<ABSOLUTE_PATTERN>'"]]

for site in sites:
    # switch print() for os.system()
    print("terminus site:create --org=" + org + " --region=" + site[2] + "  " + site[1] + "  \"" + site[0] + "\"  " + up_stream)
    print("terminus pc " + site[1] + ".dev --app=mysql < " + site[1] + ".sql")
    print("terminus wp " + site[1] + ".dev search-replace " + site[6] + " '/'")
    print("terminus rsync ./" + site[1] + "/<CONTENT>/. " + site[1] + ".dev:code/wp-content")
    print("terminus import:files " + site[1] + ".dev " + site[4] + " /wp-content/uploads/" + site[5] + " --yes")
    for tag in site[3]:
        print("terminus tag:add " + site[1] + " " + org + " " + tag)
    print("terminus connection:set " + site[1] + ".dev git --yes")
    print("terminus env:clear-cache " + site[1] + ".dev")

    break