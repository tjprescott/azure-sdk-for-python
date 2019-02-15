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


class SecretFragment(UpdateResource):
    """A secret.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param value: The value of the secret for secret creation.
    :type value: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'value': {'key': 'properties.value', 'type': 'str'},
    }

    def __init__(self, *, tags=None, value: str=None, **kwargs) -> None:
        super(SecretFragment, self).__init__(tags=tags, **kwargs)
        self.value = value
