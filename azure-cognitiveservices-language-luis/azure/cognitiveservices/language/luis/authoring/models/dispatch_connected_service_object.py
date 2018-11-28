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


class DispatchConnectedServiceObject(Model):
    """A disptch connected service.

    :param intent_name: The name of the intent connected to the dispatch
    :type intent_name: str
    :param type: The type of the connected service [luis/qna]
    :type type: str
    :param name: The name of the connected LUIS app (only if type is luis)
    :type name: str
    :param app_id: The ID of the connected LUIS app (only if type is luis)
    :type app_id: str
    :param version: The version ID of the connected LUIS app (only if type is
     luis)
    :type version: str
    :param region: The region of the connected LUIS app (only if type is luis)
    :type region: str
    :param kb_id: The ID of the connected QnA app (only if type is qna)
    :type kb_id: str
    """

    _attribute_map = {
        'intent_name': {'key': 'intentName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'app_id': {'key': 'appId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'kb_id': {'key': 'kbId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DispatchConnectedServiceObject, self).__init__(**kwargs)
        self.intent_name = kwargs.get('intent_name', None)
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)
        self.app_id = kwargs.get('app_id', None)
        self.version = kwargs.get('version', None)
        self.region = kwargs.get('region', None)
        self.kb_id = kwargs.get('kb_id', None)
