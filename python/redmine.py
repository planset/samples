import requests
import json

API_KEY = '9c14656d3e47fbbc78cd3ecb73e052abe3acc4e9'



headers = {'X-Redmine-API-Key': API_KEY}
r = requests.get('https://dkpyn.com/redmine/issues.json', headers={'X-Redmine-API-Key': API_KEY})

data = json.loads(r.content)

print data['total_count']
print data['limit']

for issue in data['issues']:
    print """{status}
    {priority}
    {description}
    {parent}
    {author}
    {start_date}
    {project}
    {created_on}
    {tracker}
    {fixed_version}
    {assigned_to}
    {updated_on}
    {id}
    {done_ratio}
    {subject}
    """.format(**issue)

"""

{u'total_count': 6, u'limit': 25, u'issues': [{u'status': {u'id': 1, u'name': u'New'}, u'priority': {
u'id': 4, u'name': u'Normal'}, u'description': u'', u'parent': {u'id': 3}, u'author': {u'id': 3, u'na
me': u'Daisuke Igarashi'}, u'start_date': u'2012-08-27', u'project': {u'id': 2, u'name': u'test2'}, u
'created_on': u'2012-08-28T09:49:00Z', u'tracker': {u'id': 4, u'name': u'Task'}, u'fixed_version': {u
'id': 1, u'name': u'sprint1'}, u'assigned_to': {u'id': 3, u'name': u'Daisuke Igarashi'}, u'updated_on
': u'2012-08-28T09:49:00Z', u'id': 6, u'done_ratio': 0, u'subject': u'Task 2'}

"""

