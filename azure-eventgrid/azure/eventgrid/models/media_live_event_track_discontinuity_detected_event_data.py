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


class MediaLiveEventTrackDiscontinuityDetectedEventData(Model):
    """Ingest track discontinuity detected event data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar track_type: Gets the type of the track (Audio / Video).
    :vartype track_type: str
    :ivar track_name: Gets the track name.
    :vartype track_name: str
    :ivar bitrate: Gets the bitrate.
    :vartype bitrate: long
    :ivar previous_timestamp: Gets the timestamp of the previous fragment.
    :vartype previous_timestamp: str
    :ivar new_timestamp: Gets the timestamp of the current fragment.
    :vartype new_timestamp: str
    :ivar timescale: Gets the timescale in which both timestamps and
     discontinuity gap are represented.
    :vartype timescale: str
    :ivar discontinuity_gap: Gets the discontinuity gap between
     PreviousTimestamp and NewTimestamp.
    :vartype discontinuity_gap: str
    """

    _validation = {
        'track_type': {'readonly': True},
        'track_name': {'readonly': True},
        'bitrate': {'readonly': True},
        'previous_timestamp': {'readonly': True},
        'new_timestamp': {'readonly': True},
        'timescale': {'readonly': True},
        'discontinuity_gap': {'readonly': True},
    }

    _attribute_map = {
        'track_type': {'key': 'trackType', 'type': 'str'},
        'track_name': {'key': 'trackName', 'type': 'str'},
        'bitrate': {'key': 'bitrate', 'type': 'long'},
        'previous_timestamp': {'key': 'previousTimestamp', 'type': 'str'},
        'new_timestamp': {'key': 'newTimestamp', 'type': 'str'},
        'timescale': {'key': 'timescale', 'type': 'str'},
        'discontinuity_gap': {'key': 'discontinuityGap', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MediaLiveEventTrackDiscontinuityDetectedEventData, self).__init__(**kwargs)
        self.track_type = None
        self.track_name = None
        self.bitrate = None
        self.previous_timestamp = None
        self.new_timestamp = None
        self.timescale = None
        self.discontinuity_gap = None
