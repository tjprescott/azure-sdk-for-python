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


class TriggerRunsQueryResponse(Model):
    """A list of trigger runs.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of trigger runs.
    :type value: list[~azure.mgmt.datafactory.models.TriggerRun]
    :param continuation_token: The continuation token for getting the next
     page of results, if any remaining results exist, null otherwise.
    :type continuation_token: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TriggerRun]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TriggerRunsQueryResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.continuation_token = kwargs.get('continuation_token', None)
