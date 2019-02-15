# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LoadBalancerConfiguration(Model):
    """A load balancer configuration for an availability group listener.

    :param private_ip_address: Private IP address.
    :type private_ip_address:
     ~azure.mgmt.sqlvirtualmachine.models.PrivateIPAddress
    :param public_ip_address_resource_id: Resource id of the public IP.
    :type public_ip_address_resource_id: str
    :param load_balancer_resource_id: Resource id of the load balancer.
    :type load_balancer_resource_id: str
    :param probe_port: Probe port.
    :type probe_port: int
    :param sql_virtual_machine_instances: List of the SQL virtual machine
     instance resource id's that are enrolled into the availability group
     listener.
    :type sql_virtual_machine_instances: list[str]
    """

    _attribute_map = {
        'private_ip_address': {'key': 'privateIpAddress', 'type': 'PrivateIPAddress'},
        'public_ip_address_resource_id': {'key': 'publicIpAddressResourceId', 'type': 'str'},
        'load_balancer_resource_id': {'key': 'loadBalancerResourceId', 'type': 'str'},
        'probe_port': {'key': 'probePort', 'type': 'int'},
        'sql_virtual_machine_instances': {'key': 'sqlVirtualMachineInstances', 'type': '[str]'},
    }

    def __init__(self, *, private_ip_address=None, public_ip_address_resource_id: str=None, load_balancer_resource_id: str=None, probe_port: int=None, sql_virtual_machine_instances=None, **kwargs) -> None:
        super(LoadBalancerConfiguration, self).__init__(**kwargs)
        self.private_ip_address = private_ip_address
        self.public_ip_address_resource_id = public_ip_address_resource_id
        self.load_balancer_resource_id = load_balancer_resource_id
        self.probe_port = probe_port
        self.sql_virtual_machine_instances = sql_virtual_machine_instances
