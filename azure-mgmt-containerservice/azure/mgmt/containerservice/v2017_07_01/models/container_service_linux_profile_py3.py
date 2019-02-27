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


class ContainerServiceLinuxProfile(Model):
    """Profile for Linux VMs in the container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param admin_username: Required. The administrator username to use for
     Linux VMs.
    :type admin_username: str
    :param ssh: Required. SSH configuration for Linux-based VMs running on
     Azure.
    :type ssh:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceSshConfiguration
    """

    _validation = {
        'admin_username': {'required': True, 'pattern': r'^[A-Za-z][-A-Za-z0-9_]*$'},
        'ssh': {'required': True},
    }

    _attribute_map = {
        'admin_username': {'key': 'adminUsername', 'type': 'str'},
        'ssh': {'key': 'ssh', 'type': 'ContainerServiceSshConfiguration'},
    }

    def __init__(self, *, admin_username: str, ssh, **kwargs) -> None:
        super(ContainerServiceLinuxProfile, self).__init__(**kwargs)
        self.admin_username = admin_username
        self.ssh = ssh
