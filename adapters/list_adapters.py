# v1.0 Rich Martin, Joksan Flores
# uses GitLab API to list the currently available public Itential Adapters and output an json array to stdout
# - only parses one subgroup deep! if this changes, may want to re-write it to recurse
# - doesn't filter out items that may not be adapters, because criteria isn't clear...

import requests, json

output = "["
# commented out 05/30/24 - no longer required due to reordering of adapters
#get any projects that are in the root adapter group
#response = requests.get("https://gitlab.com/api/v4/groups/4836968/projects")
#for project in response.json():
#    output += "{\"name\":\""+project['path']+"\",\"category\":\""+project['namespace'].get('path')+"\"},"

# get a list of the subgroups under the adapter group
response = requests.get("https://gitlab.com/api/v4/groups/4836968/subgroups")
for subgroup in response.json():
    # get a list of the projects that are in this group
    response2 = requests.get("https://gitlab.com/api/v4/groups/"+str(subgroup['id'])+"/projects")
    for project in response2.json():
        output += "{\"name\":\""+project['path']+"\",\"category\":\""+project['namespace'].get('path')+"\"},"

output = output[0:-1] + "]"
# send the built json array object to stdout
adapterListObj = {}
adapterListObj["adapterList"] = json.loads(output)
adapterListObj["adapterCount"] = len(json.loads(output))
print(json.dumps(adapterListObj, indent=3))
