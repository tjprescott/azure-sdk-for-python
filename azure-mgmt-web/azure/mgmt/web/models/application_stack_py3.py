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


class ApplicationStack(Model):
    """Application stack.

    :param name: Application stack name.
    :type name: str
    :param display: Application stack display name.
    :type display: str
    :param dependency: Application stack dependency.
    :type dependency: str
    :param major_versions: List of major versions available.
    :type major_versions: list[~azure.mgmt.web.models.StackMajorVersion]
    :param frameworks: List of frameworks associated with application stack.
    :type frameworks: list[~azure.mgmt.web.models.ApplicationStack]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'str'},
        'dependency': {'key': 'dependency', 'type': 'str'},
        'major_versions': {'key': 'majorVersions', 'type': '[StackMajorVersion]'},
        'frameworks': {'key': 'frameworks', 'type': '[ApplicationStack]'},
    }

    def __init__(self, *, name: str=None, display: str=None, dependency: str=None, major_versions=None, frameworks=None, **kwargs) -> None:
        super(ApplicationStack, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.dependency = dependency
        self.major_versions = major_versions
        self.frameworks = frameworks
