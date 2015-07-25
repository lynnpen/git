from suds.client import Client

sms_url = 'http://sms.ecust.edu.cn/sms/services/SmsSendService?wsdl'
sysld = 'eyou'
password = 'eyou_2014'

client = Client(sms_url)
print client


token = client.service.getToken(sysld, password)

print token
