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

from .update_resource_py3 import UpdateResource


class ServiceFabricFragment(UpdateResource):
    """A Service Fabric.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param external_service_fabric_id: The backing service fabric resource's
     id
    :type external_service_fabric_id: str
    :param environment_id: The resource id of the environment under which the
     service fabric resource is present
    :type environment_id: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'external_service_fabric_id': {'key': 'properties.externalServiceFabricId', 'type': 'str'},
        'environment_id': {'key': 'properties.environmentId', 'type': 'str'},
    }

    def __init__(self, *, tags=None, external_service_fabric_id: str=None, environment_id: str=None, **kwargs) -> None:
        super(ServiceFabricFragment, self).__init__(tags=tags, **kwargs)
        self.external_service_fabric_id = external_service_fabric_id
        self.environment_id = environment_id
