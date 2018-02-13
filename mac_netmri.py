#!/usr/local/env python3.6

import json
import requests
import validators
from netmri_auto import object_manager

def addressSearch():

    address = input("> ")
    x = object_manager.netMRIManager()
    x.macQuery(user_input=address)

if __name__ == "__main__":
    addressSearch()

requests.packages.urllib3.disable_warnings()
# suppress irrelevant messages to enduser

# use x.show(self, objtype, objid) to pull information of switch
# after figuring out how to isolate the InfraDeviceID from y output

