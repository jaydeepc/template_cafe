import json

from cafe.engine.models.base import AutoMarshallingModel


class AuthResponse(AutoMarshallingModel):

    def __init__(self, ID, companyID=None, companyLabel=None, companyType=None, createdOn=None, email=None, expiresOn=None, fullName=None, principal=None,
                 scope=None, scopeAttributes=None, subscription=None, updatedOn=None):
        super(AuthResponse, self).__init__()
        self.ID = ID
        self.companyID = companyID
        self.companyLabel = companyLabel
        self.companyType = companyType
        self.createdOn = createdOn
        self.email = email
        self.expiresOn = expiresOn
        self.fullName = fullName
        self.principal = principal
        self.scope = scope
        self.scopeAttributes = scopeAttributes
        self.subscription = subscription
        self.updatedOn = updatedOn

    @classmethod
    def _json_to_obj(cls, serialized_str):
        serialized_str = json.loads(serialized_str)
        entity = AuthResponse(ID=serialized_str.get("ID"))
        return entity



class AuthRequest(AutoMarshallingModel):

    def __init__(self, username, password):
        super(AuthRequest, self).__init__()
        self.username = username
        self.password = password

    def _obj_to_json(self):
        body = {
            'username': self.username,
            'password': self.password
        }
        return json.dumps(body)