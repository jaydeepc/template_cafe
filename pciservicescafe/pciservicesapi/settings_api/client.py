from cafe.engine.http.client import AutoMarshallingHTTPClient

from pciservicescafe.pciservicesapi.settings_api.models.settings_api import SettingsResponse


class PCIServicesAPIClient(AutoMarshallingHTTPClient):

    def __init__(self, url, auth_token, serialize_format, deserialize_format=None):
        super(PCIServicesAPIClient, self).__init__(serialize_format,
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

    def settings_data_status_get(self, requestslib_kwargs=None):

        url = '{0}/settings/data/status'.format(self.url)
        return self.request('GET', url,
                            response_entity_type=SettingsResponse,
                            requestslib_kwargs=requestslib_kwargs)