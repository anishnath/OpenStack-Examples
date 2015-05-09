__author__ = 'Anish'
import swiftclient
import ConfigParser
'''
Sample Openstack Swift Example for Creating Container
Addign Object to the Container
watch the demo @ https://goo.gl/tUNwBc

'''
class SwiftClientExample:
        def __init__(self,tenantName):
            config = ConfigParser.RawConfigParser()
            config.read('auth.properties')
            #Step-1 Swift Configuration
            self.conn = swiftclient.Connection(
                config.get(tenantName,'AUTH_URL'),
                config.get(tenantName,'USERNAME'),
                config.get(tenantName,'PASSWORD'),
                auth_version=2,
                tenant_name=config.get(tenantName,'PROJECT_ID'))

            #Step-2 Create Swift Container
            self.conn.put_container('MyFirstContainer')
            #Step-3 Create Swift Object
            self.conn.put_object(
                "MyFirstContainer", "Firstfile", "Hello World With Swift")
            #Step-4 Test the fiel get from the container
            print self.conn.get_container('MyFirstContainer')

x=SwiftClientExample('Project_Name')
