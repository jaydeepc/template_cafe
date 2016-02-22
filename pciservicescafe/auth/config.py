from cafe.engine.models.data_interfaces import ConfigSectionInterface


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