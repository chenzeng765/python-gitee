# coding: utf-8

"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Group(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'login': 'str',
        'url': 'str',
        'avatar_url': 'str',
        'repos_url': 'str',
        'events_url': 'str',
        'members_url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'url': 'url',
        'avatar_url': 'avatar_url',
        'repos_url': 'repos_url',
        'events_url': 'events_url',
        'members_url': 'members_url',
        'description': 'description'
    }

    def __init__(self, id=None, login=None, url=None, avatar_url=None, repos_url=None, events_url=None, members_url=None, description=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._login = None
        self._url = None
        self._avatar_url = None
        self._repos_url = None
        self._events_url = None
        self._members_url = None
        self._description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if url is not None:
            self.url = url
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if repos_url is not None:
            self.repos_url = repos_url
        if events_url is not None:
            self.events_url = events_url
        if members_url is not None:
            self.members_url = members_url
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this Group.  # noqa: E501


        :return: The login of this Group.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this Group.


        :param login: The login of this Group.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def url(self):
        """Gets the url of this Group.  # noqa: E501


        :return: The url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Group.


        :param url: The url of this Group.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Group.  # noqa: E501


        :return: The avatar_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Group.


        :param avatar_url: The avatar_url of this Group.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def repos_url(self):
        """Gets the repos_url of this Group.  # noqa: E501


        :return: The repos_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._repos_url

    @repos_url.setter
    def repos_url(self, repos_url):
        """Sets the repos_url of this Group.


        :param repos_url: The repos_url of this Group.  # noqa: E501
        :type: str
        """

        self._repos_url = repos_url

    @property
    def events_url(self):
        """Gets the events_url of this Group.  # noqa: E501


        :return: The events_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._events_url

    @events_url.setter
    def events_url(self, events_url):
        """Sets the events_url of this Group.


        :param events_url: The events_url of this Group.  # noqa: E501
        :type: str
        """

        self._events_url = events_url

    @property
    def members_url(self):
        """Gets the members_url of this Group.  # noqa: E501


        :return: The members_url of this Group.  # noqa: E501
        :rtype: str
        """
        return self._members_url

    @members_url.setter
    def members_url(self, members_url):
        """Sets the members_url of this Group.


        :param members_url: The members_url of this Group.  # noqa: E501
        :type: str
        """

        self._members_url = members_url

    @property
    def description(self):
        """Gets the description of this Group.  # noqa: E501


        :return: The description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Group.


        :param description: The description of this Group.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Group, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
