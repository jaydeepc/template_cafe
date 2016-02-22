from cafe.engine.http.client import AutoMarshallingHTTPClient

from pciservicescafe.pciservicesapi.auth_api.models.auth_api import AuthResponse, AuthRequest


class PCIAuthClient(AutoMarshallingHTTPClient):

    def __init__(self, url, serialize_format, deserialize_format=None):
        super(PCIAuthClient, self).__init__(serialize_format,
                                              deserialize_format)
        self.url = url
        self.default_headers['User-Agent'] = "python-requests/2.9.1"
        ct = '{content_type}/{content_subtype}'.format(
            content_type='application',
            content_subtype=self.serialize_format)
        accept = '{content_type}/{content_subtype}'.format(
            content_type='application',
            content_subtype=self.deserialize_format)
        self.default_headers['Content-Type'] = ct
        self.default_headers['Accept'] = accept

    def get_token(self, username, password, requestslib_kwargs=None):

        url = '{0}/session'.format(self.url)
        request = AuthRequest(username=username, password=password)
        return self.request('POST', url,
                            response_entity_type=AuthResponse,
                            request_entity=request,
                            requestslib_kwargs=requestslib_kwargs)