import urllib
import urllib.request
import json

user = '220161223085'

getTokenUrl = 'http://seat.ujn.edu.cn/rest/auth?username=%s&password=%s'%(user,user)

Response = urllib.request.urlopen(getTokenUrl)
Token_Raw = Response.read().decode('utf-8')
Token = json.loads(Token_Raw)['data']['token']
print(Token)

