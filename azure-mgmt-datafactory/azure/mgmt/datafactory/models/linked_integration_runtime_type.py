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


class LinkedIntegrationRuntimeType(Model):
    """The base definition of a linked integration runtime.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: LinkedIntegrationRuntimeRbacAuthorization,
    LinkedIntegrationRuntimeKeyAuthorization

    All required parameters must be populated in order to send to Azure.

    :param authorization_type: Required. Constant filled by server.
    :type authorization_type: str
    """

    _validation = {
        'authorization_type': {'required': True},
    }

    _attribute_map = {
        'authorization_type': {'key': 'authorizationType', 'type': 'str'},
    }

    _subtype_map = {
        'authorization_type': {'RBAC': 'LinkedIntegrationRuntimeRbacAuthorization', 'Key': 'LinkedIntegrationRuntimeKeyAuthorization'}
    }

    def __init__(self, **kwargs):
        super(LinkedIntegrationRuntimeType, self).__init__(**kwargs)
        self.authorization_type = None
