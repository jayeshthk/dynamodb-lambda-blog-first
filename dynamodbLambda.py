import json
import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name='region_name')
table = dynamodb.Table('table_name')

class CheckAuthenticatedUser():
    def __init__(self,value=None,passwd=None):
        self.value=value
        self.passwd=passwd
    def checkit(self,emailvalue):
        
        response1 = table.get_item(Key={'email': emailvalue})

        if 'Item' in response1  :
            print('True')
        else:
            print('False')
        return response1
        
            
        
        
    


mysubid='demo@gmail.com'
def lambda_handler(event, context):
    obj=CheckAuthenticatedUser()
    
    
    # TODO implement
    
    return obj.checkit('demo@gmail.com')
