import os

org = "fce29c48-522f-4984-8c7c-f9473733c67b"
ups = "e8fe8550-1ab9-4964-8838-2b9abdccf4bf"
crt  = "site:create"

sites = [["Site 1 AU", "site1-au", "au", "Autoload"],
         ["Site 1 EU", "site1-eu", "eu", "Autoload"],
         ["Site 2 AU", "site2-au", "eu", "Autoload"]]

for site in sites:

    lbl = site[0]
    nam = site[1]
    rgn = site[2]
    tag = site[3]

    trmns_create = "terminus " + crt + " --org=" + org + " --region=" + rgn + "  " + nam + "  \"" + lbl + "\"  " + ups

    trmns_db = "terminus pc " + nam + ".dev --app=mysql < " + nam + ".sql"
    trmns_db_clean = "terminus wp " + nam + ".dev search-replace 'http://wpcu.lndo.site/' '/'"

    trmns_content = "terminus rsync ./" + nam + "/content/. " + nam + ".dev:code/wp-content"
    trmns_files = "terminus import:files " + nam + ".dev https://dev-wp-template-1.pantheonsite.io/wp-content/uploads/assets.zip --yes"

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


