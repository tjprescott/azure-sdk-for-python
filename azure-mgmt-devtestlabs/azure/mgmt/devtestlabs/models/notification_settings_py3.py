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


class NotificationSettings(Model):
    """Notification settings for a schedule.

    :param status: If notifications are enabled for this schedule (i.e.
     Enabled, Disabled). Possible values include: 'Enabled', 'Disabled'
    :type status: str or ~azure.mgmt.devtestlabs.models.EnableStatus
    :param time_in_minutes: Time in minutes before event at which notification
     will be sent.
    :type time_in_minutes: int
    :param webhook_url: The webhook URL to which the notification will be
     sent.
    :type webhook_url: str
    :param email_recipient: The email recipient to send notifications to (can
     be a list of semi-colon separated email addresses).
    :type email_recipient: str
    :param notification_locale: The locale to use when sending a notification
     (fallback for unsupported languages is EN).
    :type notification_locale: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'time_in_minutes': {'key': 'timeInMinutes', 'type': 'int'},
        'webhook_url': {'key': 'webhookUrl', 'type': 'str'},
        'email_recipient': {'key': 'emailRecipient', 'type': 'str'},
        'notification_locale': {'key': 'notificationLocale', 'type': 'str'},
    }

    def __init__(self, *, status=None, time_in_minutes: int=None, webhook_url: str=None, email_recipient: str=None, notification_locale: str=None, **kwargs) -> None:
        super(NotificationSettings, self).__init__(**kwargs)
        self.status = status
        self.time_in_minutes = time_in_minutes
        self.webhook_url = webhook_url
        self.email_recipient = email_recipient
        self.notification_locale = notification_locale
