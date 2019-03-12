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


class RouteCompilationError(Model):
    """Compilation error when evaluating route.

    :param message: Route error message
    :type message: str
    :param severity: Severity of the route error. Possible values include:
     'error', 'warning'
    :type severity: str or ~azure.mgmt.iothub.models.RouteErrorSeverity
    :param location: Location where the route error happened
    :type location: ~azure.mgmt.iothub.models.RouteErrorRange
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
        'location': {'key': 'location', 'type': 'RouteErrorRange'},
    }

    def __init__(self, *, message: str=None, severity=None, location=None, **kwargs) -> None:
        super(RouteCompilationError, self).__init__(**kwargs)
        self.message = message
        self.severity = severity
        self.location = location
