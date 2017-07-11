#/usr/bin/python

import jira.client
from jira.client import JIRA

#from credential import *
# Import credential for login to Jira (global_user and global_pwd) : Generate your own

options = {'server':'https://jira.example.com'}
#print 'Step 1'
jira = JIRA(options,basic_auth=(global_user,global_pwd))
#print 'Step 2'
projects = jira.projects()
#print 'Step 3'

#for project in projects:
#issues = jira.search_issues('project=DEV')
#issues = jira.search_issues('project=DEV', startAt = total)
#issues = jira.search_issues('project=DEV', maxResults = False)
#issues = jira.search_issues('project=DEV', maxResults = 500000)
issues = jira.search_issues('filter=24783')
#	print (project,' : ',issues)

counter=0
for issue in issues:
	#counter+=1
	#if str(issue.fields.status) == 'DONE' or str(issue.fields.status) == 'Closed':
	#print 'The Count is : ',counter
	if str(issue.fields.status) == 'IN PROGRESS' or  str(issue.fields.status) == 'SELECTED' or  str(issue.fields.status) == 'INFO REQUIRED' or  str(issue.fields.status) == 'PENDING VERIFICATION':
		counter+=1
		print 'The Count is : ',counter
		print 'Issue ID is : ',issue
		print 'The Issue Type is : ',issue.fields.issuetype
		print 'The Summary is : ',issue.fields.summary
		if str(issue) == 'ISSUE-1350':
			print 'It is 1350'
		elif str(issue) == 'ISSUE-2636':
			print 'It is 2636'
		else:
			print 'Not Related'

		print ''
		print ''

print 'End of this'
