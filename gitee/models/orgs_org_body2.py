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

class OrgsOrgBody2(object):
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
        'access_token': 'str',
        'email': 'str',
        'location': 'str',
        'name': 'str',
        'description': 'str',
        'html_url': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'email': 'email',
        'location': 'location',
        'name': 'name',
        'description': 'description',
        'html_url': 'html_url'
    }

    def __init__(self, access_token=None, email=None, location=None, name=None, description=None, html_url=None):  # noqa: E501
        """OrgsOrgBody2 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._email = None
        self._location = None
        self._name = None
        self._description = None
        self._html_url = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if email is not None:
            self.email = email
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if html_url is not None:
            self.html_url = html_url

    @property
    def access_token(self):
        """Gets the access_token of this OrgsOrgBody2.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OrgsOrgBody2.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def email(self):
        """Gets the email of this OrgsOrgBody2.  # noqa: E501

        组织公开的邮箱地址  # noqa: E501

        :return: The email of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrgsOrgBody2.

        组织公开的邮箱地址  # noqa: E501

        :param email: The email of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def location(self):
        """Gets the location of this OrgsOrgBody2.  # noqa: E501

        组织所在地  # noqa: E501

        :return: The location of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this OrgsOrgBody2.

        组织所在地  # noqa: E501

        :param location: The location of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this OrgsOrgBody2.  # noqa: E501

        组织名称  # noqa: E501

        :return: The name of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgsOrgBody2.

        组织名称  # noqa: E501

        :param name: The name of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this OrgsOrgBody2.  # noqa: E501

        组织简介  # noqa: E501

        :return: The description of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrgsOrgBody2.

        组织简介  # noqa: E501

        :param description: The description of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def html_url(self):
        """Gets the html_url of this OrgsOrgBody2.  # noqa: E501

        组织站点  # noqa: E501

        :return: The html_url of this OrgsOrgBody2.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this OrgsOrgBody2.

        组织站点  # noqa: E501

        :param html_url: The html_url of this OrgsOrgBody2.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

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
        if issubclass(OrgsOrgBody2, dict):
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
        if not isinstance(other, OrgsOrgBody2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
