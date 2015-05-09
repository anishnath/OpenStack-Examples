__author__ = 'Anish '
from keystoneclient.auth.identity import v2
from novaclient import client
from keystoneclient import session
import ConfigParser
'''
Sample Openstack Swift Example for Creating a Security Group
Adding sampple port Port Range TCP/UDP
Demo @ https://goo.gl/SKUYJ2
'''
class SecurityGroupExample:
        def __init__(self,tenantName):
            config = ConfigParser.RawConfigParser()
            config.read('auth.properties')
            #Step-1 Keystone AUTH Configuration
            auth = v2.Password(auth_url=config.get(tenantName, 'AUTH_URL'),
                           username=config.get(tenantName, 'USERNAME'),
                           password=config.get(tenantName, 'PASSWORD'),
                           tenant_name=config.get(tenantName, 'PROJECT_ID'))
            #Step-2 Create Session
            sess = session.Session(auth=auth)
            #Step-3 Initialize Nova API
            self.nova = client.Client(2, session=sess)
            #Step-4 Create Security gropu using Nova API
            secgroup = self.nova.security_groups.create(
                name="LiveSecurityGroup",
                description="Live Security Group Demo")
            #Step-5  Define Rules add ssh port
            self.nova.security_group_rules.create(secgroup.id,
                                              ip_protocol="tcp",
                                              from_port=22,
                                              to_port=22)
            # Step-6 Test the example
            print self.nova.security_groups.list()

x=SecurityGroupExample('Project_Name')
