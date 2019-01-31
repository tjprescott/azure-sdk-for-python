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


class BaselineResponse(Model):
    """The response to a baseline query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: the metric baseline Id.
    :vartype id: str
    :ivar type: the resource type of the baseline resource.
    :vartype type: str
    :ivar name: the name and the display name of the metric, i.e. it is
     localizable string.
    :vartype name: ~azure.mgmt.monitor.models.LocalizableString
    :param timespan: The timespan for which the data was retrieved. Its value
     consists of two datetimes concatenated, separated by '/'.  This may be
     adjusted in the future and returned back from what was originally
     requested.
    :type timespan: str
    :param interval: The interval (window size) for which the metric data was
     returned in.  This may be adjusted in the future and returned back from
     what was originally requested.  This is not present if a metadata request
     was made.
    :type interval: timedelta
    :param aggregation: The aggregation type of the metric.
    :type aggregation: str
    :param timestamps: the array of timestamps of the baselines.
    :type timestamps: list[datetime]
    :param baseline: the baseline values for each sensitivity.
    :type baseline: list[~azure.mgmt.monitor.models.Baseline]
    :param metadata: the baseline metadata values.
    :type metadata: list[~azure.mgmt.monitor.models.BaselineMetadataValue]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'timespan': {'key': 'properties.timespan', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'duration'},
        'aggregation': {'key': 'properties.aggregation', 'type': 'str'},
        'timestamps': {'key': 'properties.timestamps', 'type': '[iso-8601]'},
        'baseline': {'key': 'properties.baseline', 'type': '[Baseline]'},
        'metadata': {'key': 'properties.metadata', 'type': '[BaselineMetadataValue]'},
    }

    def __init__(self, **kwargs):
        super(BaselineResponse, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.timespan = kwargs.get('timespan', None)
        self.interval = kwargs.get('interval', None)
        self.aggregation = kwargs.get('aggregation', None)
        self.timestamps = kwargs.get('timestamps', None)
        self.baseline = kwargs.get('baseline', None)
        self.metadata = kwargs.get('metadata', None)
