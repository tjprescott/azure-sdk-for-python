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


class RunCommandInput(Model):
    """Capture Virtual Machine parameters.

    All required parameters must be populated in order to send to Azure.

    :param command_id: Required. The run command id.
    :type command_id: str
    :param script: Optional. The script to be executed.  When this value is
     given, the given script will override the default script of the command.
    :type script: list[str]
    :param parameters: The run command parameters.
    :type parameters:
     list[~azure.mgmt.compute.v2018_04_01.models.RunCommandInputParameter]
    """

    _validation = {
        'command_id': {'required': True},
    }

    _attribute_map = {
        'command_id': {'key': 'commandId', 'type': 'str'},
        'script': {'key': 'script', 'type': '[str]'},
        'parameters': {'key': 'parameters', 'type': '[RunCommandInputParameter]'},
    }

    def __init__(self, **kwargs):
        super(RunCommandInput, self).__init__(**kwargs)
        self.command_id = kwargs.get('command_id', None)
        self.script = kwargs.get('script', None)
        self.parameters = kwargs.get('parameters', None)
