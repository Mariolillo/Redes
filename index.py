#from pysnmp.hlapi import *
from pysnmp.hlapi import getCMD,SnmpEngine,CommunityData,UdpTransportTarget,ContextData,ObjectType


#Deployment
name='mario'
ips
oid=''


iterator = getCmd(
    SnmpEngine(),    CommunityData('public', mpModel=0),  #nombre de la comunidad viendolo desde el router
    UdpTransportTarget(('192.168.x.x', 161)),#host,puerto
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
) #buscar el oid que me de alusión del modelo y nombre del router

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))

