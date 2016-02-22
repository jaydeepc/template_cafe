from cafe.engine.http.client import AutoMarshallingHTTPClient

from pciservicescafe.pciservicesapi.notification_api.models.notification_api import NotificationsResponse


class NotificationServicsClient(AutoMarshallingHTTPClient):

    def __init__(self, url, auth_token, serialize_format, deserialize_format=None):
        super(NotificationServicsClient, self).__init__(serialize_format,
                                              deserialize_format)
        self.url = url
        self.auth_token = auth_token
        self.default_headers['X-Auth-Token'] = auth_token
        ct = '{content_type}/{content_subtype}'.format(
            content_type='application',
            content_subtype=self.serialize_format)
        accept = '{content_type}/{content_subtype}'.format(
            content_type='application',
            content_subtype=self.deserialize_format)
        self.default_headers['Content-Type'] = ct
        self.default_headers['Accept'] = accept

    def get_all_notifications(self, requestslib_kwargs=None):

        url = '{0}/notifications'.format(self.url)
        return self.request('GET', url,
                            response_entity_type=NotificationsResponse,
                            requestslib_kwargs=requestslib_kwargs)

    def mark_read_all_notifications(self, requestslib_kwargs=None):

        url = '{0}/notifications'.format(self.url)
        return self.request('PUT', url, requestslib_kwargs=requestslib_kwargs)

    def mark_read_notification_by_id(self, notification_id, requestslib_kwargs=None):

        url = '{0}/notifications/{1}'.format(self.url, notification_id)
        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)