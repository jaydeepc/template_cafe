import json
from pprint import pformat

from cafe.engine.models.base import AutoMarshallingModel
from six import iteritems


class NotificationsResponse(AutoMarshallingModel):

    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, notifications, pagination):
        """
        DataStatus - a model defined in Swagger

        """

        self.notifications = notifications
        self.pagination = pagination

    @classmethod
    def _json_to_obj(cls, serialized_str):
        serialized_str = json.loads(serialized_str)
        entity = NotificationsResponse(notifications=cls._list_to_obj(serialized_str.get("notifications")),
                                      pagination=PaginationResponse._dict_to_obj(serialized_str.get("pagination")))
        return entity

    @classmethod
    def _list_to_obj(cls, notification_dict_list):
        notification_list = []
        for notification_dict in notification_dict_list:
            notification_list.append(NotificationResponse._dict_to_obj(notification_dict))
        return notification_list


class NotificationResponse(AutoMarshallingModel):

    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, readOn, isRead, ID, text, createdOn):
        """
        DataStatus - a model defined in Swagger

        """

        self.read_on = readOn
        self.is_read = isRead
        self.id = ID
        self.text = text
        self.created_on = createdOn

    @classmethod
    def _dict_to_obj(cls, notification_dict):
        notification = NotificationResponse(readOn=notification_dict.get("readOn"),
                                            isRead=notification_dict.get("isRead"),
                                            ID=notification_dict.get("ID"),
                                            text=notification_dict.get("text"),
                                            createdOn=notification_dict.get("createdOn"))
        return notification


class PaginationResponse(AutoMarshallingModel):

    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total, perPage, hasNext, page):
        """
        DataStatus - a model defined in Swagger

        """

        self.total = total
        self.per_page = perPage
        self.has_next = hasNext
        self.page = page

    @classmethod
    def _dict_to_obj(cls, pagination_dict):
        pagination = PaginationResponse(total=pagination_dict.get("total"),
                                          perPage=pagination_dict.get("perPage"),
                                          hasNext=pagination_dict.get("hasNext"),
                                          page=pagination_dict.get("page"))
        return pagination