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

class MembersUsernameBody(object):
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
        'outsourced': 'bool',
        'role': 'str',
        'active': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'outsourced': 'outsourced',
        'role': 'role',
        'active': 'active',
        'name': 'name'
    }

    def __init__(self, access_token=None, outsourced=None, role='member', active=True, name=None):  # noqa: E501
        """MembersUsernameBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._outsourced = None
        self._role = None
        self._active = None
        self._name = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if outsourced is not None:
            self.outsourced = outsourced
        if role is not None:
            self.role = role
        if active is not None:
            self.active = active
        if name is not None:
            self.name = name

    @property
    def access_token(self):
        """Gets the access_token of this MembersUsernameBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this MembersUsernameBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this MembersUsernameBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this MembersUsernameBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def outsourced(self):
        """Gets the outsourced of this MembersUsernameBody.  # noqa: E501

        是否企业外包成员，默认：否  # noqa: E501

        :return: The outsourced of this MembersUsernameBody.  # noqa: E501
        :rtype: bool
        """
        return self._outsourced

    @outsourced.setter
    def outsourced(self, outsourced):
        """Sets the outsourced of this MembersUsernameBody.

        是否企业外包成员，默认：否  # noqa: E501

        :param outsourced: The outsourced of this MembersUsernameBody.  # noqa: E501
        :type: bool
        """

        self._outsourced = outsourced

    @property
    def role(self):
        """Gets the role of this MembersUsernameBody.  # noqa: E501

        企业角色，默认普通成员  # noqa: E501

        :return: The role of this MembersUsernameBody.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MembersUsernameBody.

        企业角色，默认普通成员  # noqa: E501

        :param role: The role of this MembersUsernameBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "member"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def active(self):
        """Gets the active of this MembersUsernameBody.  # noqa: E501

        是否可访问企业资源，默认:是。（若选否则禁止该用户访问企业资源）  # noqa: E501

        :return: The active of this MembersUsernameBody.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MembersUsernameBody.

        是否可访问企业资源，默认:是。（若选否则禁止该用户访问企业资源）  # noqa: E501

        :param active: The active of this MembersUsernameBody.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """Gets the name of this MembersUsernameBody.  # noqa: E501

        企业成员真实姓名（备注）  # noqa: E501

        :return: The name of this MembersUsernameBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MembersUsernameBody.

        企业成员真实姓名（备注）  # noqa: E501

        :param name: The name of this MembersUsernameBody.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(MembersUsernameBody, dict):
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
        if not isinstance(other, MembersUsernameBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
