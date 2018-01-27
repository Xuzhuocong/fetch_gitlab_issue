#!/usr/bin/env python3
# coding:utf-8

import requests
import sys
import json
print(len(sys.argv))
print(sys.argv)
if len(sys.argv) < 3:
    errorLog = """
    请输入正确的参数，例如：\n
    fetchGitlabIssue.py http://host_to_gitlab "private token"
    """
    print(errorLog)
    sys.exit(0)

host = sys.argv[1]
privateToken = sys.argv[2]

fetchGroupsUrl = "%s/api/v3/groups?private_token=%s" % (host, privateToken)
response = requests.get(fetchGroupsUrl)
groups = json.loads(response.text)
print(json.dumps(groups, indent=2, sort_keys=True)
      + '\n请选择一个Group Id用于拉取Issue列表:\n\n')

print("\tGroupId\t\tGroupName")
for group in groups:
    print("\t%d\t\t%s" % (group['id'], group['full_name']))
groupId = input("请输入：\n")

fetchProjectsUrl = "%s/api/v3/groups/%s/projects?private_token=%s" % (host, groupId, privateToken)
response = requests.get(fetchProjectsUrl)
projects = json.loads(response.text)
print(json.dumps(projects, indent=2, sort_keys=True)
      + '\n请选择一个Project Id用于拉取Issue列表:\n\n')

print("\tProjectId\t\tProjectName")
for project in projects:
    print("\t%d\t\t%s" % (project['id'], project['name']))
projectId = input("请输入：\n")

fetchIssuesUrl = "%s/api/v3/projects/%s/issues?scope=all&private_token=%s" % (host, projectId, privateToken)
issues = json.loads(requests.get(fetchIssuesUrl).text)
print(json.dumps(issues, indent=2, sort_keys=True))

with open('issues.json', 'w') as issuesFile:
    json.dump(issues, issuesFile)

print("Issues 已经被写入issues.json")
