from cafe.engine.models.data_interfaces import ConfigSectionInterface


class MarshallingConfig(ConfigSectionInterface):
    SECTION_NAME = 'marshalling'

    @property
    def serializer(self):
        return self.get("serialize_format")

    @property
    def deserializer(self):
        return self.get("deserialize_format")


class PCIServicesAPIConfig(ConfigSectionInterface):

    SECTION_NAME = 'pciservices_api'

    @property
    def url(self):
        return self.get('url')


class PCIAuthConfig(ConfigSectionInterface):

    SECTION_NAME = 'token_api'

    @property
    def version(self):
        return self.get('version')

    @property
    def username(self):
        return self.get('username')

    @property
    def password(self):
        return self.get('password')

    @property
    def authentication_endpoint(self):
        return self.get('authentication_endpoint')