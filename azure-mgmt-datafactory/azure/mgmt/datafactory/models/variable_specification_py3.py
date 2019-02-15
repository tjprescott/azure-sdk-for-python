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


class VariableSpecification(Model):
    """Definition of a single variable for a Pipeline.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Variable type. Possible values include: 'String',
     'Bool', 'Array'
    :type type: str or ~azure.mgmt.datafactory.models.VariableType
    :param default_value: Default value of variable.
    :type default_value: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
    }

    def __init__(self, *, type, default_value=None, **kwargs) -> None:
        super(VariableSpecification, self).__init__(**kwargs)
        self.type = type
        self.default_value = default_value
