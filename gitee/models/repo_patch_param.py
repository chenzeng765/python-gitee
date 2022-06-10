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

class RepoPatchParam(object):
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
        'name': 'str',
        'description': 'str',
        'homepage': 'str',
        'has_issues': 'str',
        'has_wiki': 'str',
        'can_comment': 'str',
        'private': 'str',
        'path': 'str',
        'default_branch': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'name': 'name',
        'description': 'description',
        'homepage': 'homepage',
        'has_issues': 'has_issues',
        'has_wiki': 'has_wiki',
        'can_comment': 'can_comment',
        'private': 'private',
        'path': 'path',
        'default_branch': 'default_branch'
    }

    def __init__(self, access_token=None, name=None, description=None, homepage=None, has_issues='true', has_wiki='true', can_comment=None, private=None, path=None, default_branch=None):  # noqa: E501
        """RepoPatchParam - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._name = None
        self._description = None
        self._homepage = None
        self._has_issues = None
        self._has_wiki = None
        self._can_comment = None
        self._private = None
        self._path = None
        self._default_branch = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if homepage is not None:
            self.homepage = homepage
        if has_issues is not None:
            self.has_issues = has_issues
        if has_wiki is not None:
            self.has_wiki = has_wiki
        if can_comment is not None:
            self.can_comment = can_comment
        if private is not None:
            self.private = private
        if path is not None:
            self.path = path
        if default_branch is not None:
            self.default_branch = default_branch

    @property
    def access_token(self):
        """Gets the access_token of this RepoPatchParam.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RepoPatchParam.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def name(self):
        """Gets the name of this RepoPatchParam.  # noqa: E501

        仓库名称  # noqa: E501

        :return: The name of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepoPatchParam.

        仓库名称  # noqa: E501

        :param name: The name of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RepoPatchParam.  # noqa: E501

        仓库描述  # noqa: E501

        :return: The description of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepoPatchParam.

        仓库描述  # noqa: E501

        :param description: The description of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def homepage(self):
        """Gets the homepage of this RepoPatchParam.  # noqa: E501

        主页(eg: https://gitee.com)  # noqa: E501

        :return: The homepage of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this RepoPatchParam.

        主页(eg: https://gitee.com)  # noqa: E501

        :param homepage: The homepage of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def has_issues(self):
        """Gets the has_issues of this RepoPatchParam.  # noqa: E501

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :return: The has_issues of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this RepoPatchParam.

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :param has_issues: The has_issues of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._has_issues = has_issues

    @property
    def has_wiki(self):
        """Gets the has_wiki of this RepoPatchParam.  # noqa: E501

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :return: The has_wiki of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this RepoPatchParam.

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :param has_wiki: The has_wiki of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._has_wiki = has_wiki

    @property
    def can_comment(self):
        """Gets the can_comment of this RepoPatchParam.  # noqa: E501

        允许用户对仓库进行评论  # noqa: E501

        :return: The can_comment of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._can_comment

    @can_comment.setter
    def can_comment(self, can_comment):
        """Sets the can_comment of this RepoPatchParam.

        允许用户对仓库进行评论  # noqa: E501

        :param can_comment: The can_comment of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._can_comment = can_comment

    @property
    def private(self):
        """Gets the private of this RepoPatchParam.  # noqa: E501

        仓库公开或私有。  # noqa: E501

        :return: The private of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this RepoPatchParam.

        仓库公开或私有。  # noqa: E501

        :param private: The private of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._private = private

    @property
    def path(self):
        """Gets the path of this RepoPatchParam.  # noqa: E501

        更新仓库路径  # noqa: E501

        :return: The path of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RepoPatchParam.

        更新仓库路径  # noqa: E501

        :param path: The path of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def default_branch(self):
        """Gets the default_branch of this RepoPatchParam.  # noqa: E501

        更新默认分支  # noqa: E501

        :return: The default_branch of this RepoPatchParam.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this RepoPatchParam.

        更新默认分支  # noqa: E501

        :param default_branch: The default_branch of this RepoPatchParam.  # noqa: E501
        :type: str
        """

        self._default_branch = default_branch

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
        if issubclass(RepoPatchParam, dict):
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
        if not isinstance(other, RepoPatchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
