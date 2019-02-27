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

from .proxy_only_resource_py3 import ProxyOnlyResource


class CertificateEmail(ProxyOnlyResource):
    """SSL certificate email.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param email_id: Email id.
    :type email_id: str
    :param time_stamp: Time stamp.
    :type time_stamp: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'email_id': {'key': 'properties.emailId', 'type': 'str'},
        'time_stamp': {'key': 'properties.timeStamp', 'type': 'iso-8601'},
    }

    def __init__(self, *, kind: str=None, email_id: str=None, time_stamp=None, **kwargs) -> None:
        super(CertificateEmail, self).__init__(kind=kind, **kwargs)
        self.email_id = email_id
        self.time_stamp = time_stamp
