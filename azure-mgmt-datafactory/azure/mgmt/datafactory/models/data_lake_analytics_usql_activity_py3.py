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

from .execution_activity_py3 import ExecutionActivity


class DataLakeAnalyticsUSQLActivity(ExecutionActivity):
    """Data Lake Analytics U-SQL activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param script_path: Required. Case-sensitive path to folder that contains
     the U-SQL script. Type: string (or Expression with resultType string).
    :type script_path: object
    :param script_linked_service: Required. Script linked service reference.
    :type script_linked_service:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param degree_of_parallelism: The maximum number of nodes simultaneously
     used to run the job. Default value is 1. Type: integer (or Expression with
     resultType integer), minimum: 1.
    :type degree_of_parallelism: object
    :param priority: Determines which jobs out of all that are queued should
     be selected to run first. The lower the number, the higher the priority.
     Default value is 1000. Type: integer (or Expression with resultType
     integer), minimum: 1.
    :type priority: object
    :param parameters: Parameters for U-SQL job request.
    :type parameters: dict[str, object]
    :param runtime_version: Runtime version of the U-SQL engine to use. Type:
     string (or Expression with resultType string).
    :type runtime_version: object
    :param compilation_mode: Compilation mode of U-SQL. Must be one of these
     values : Semantic, Full and SingleBox. Type: string (or Expression with
     resultType string).
    :type compilation_mode: object
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'script_path': {'required': True},
        'script_linked_service': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'script_path': {'key': 'typeProperties.scriptPath', 'type': 'object'},
        'script_linked_service': {'key': 'typeProperties.scriptLinkedService', 'type': 'LinkedServiceReference'},
        'degree_of_parallelism': {'key': 'typeProperties.degreeOfParallelism', 'type': 'object'},
        'priority': {'key': 'typeProperties.priority', 'type': 'object'},
        'parameters': {'key': 'typeProperties.parameters', 'type': '{object}'},
        'runtime_version': {'key': 'typeProperties.runtimeVersion', 'type': 'object'},
        'compilation_mode': {'key': 'typeProperties.compilationMode', 'type': 'object'},
    }

    def __init__(self, *, name: str, script_path, script_linked_service, additional_properties=None, description: str=None, depends_on=None, user_properties=None, linked_service_name=None, policy=None, degree_of_parallelism=None, priority=None, parameters=None, runtime_version=None, compilation_mode=None, **kwargs) -> None:
        super(DataLakeAnalyticsUSQLActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.script_path = script_path
        self.script_linked_service = script_linked_service
        self.degree_of_parallelism = degree_of_parallelism
        self.priority = priority
        self.parameters = parameters
        self.runtime_version = runtime_version
        self.compilation_mode = compilation_mode
        self.type = 'DataLakeAnalyticsU-SQL'
