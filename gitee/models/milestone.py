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

class Milestone(object):
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
        'url': 'str',
        'html_url': 'str',
        'number': 'int',
        'repository_id': 'int',
        'state': 'str',
        'title': 'str',
        'description': 'str',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'open_issues': 'int',
        'closed_issues': 'int',
        'due_on': 'str'
    }

    attribute_map = {
        'url': 'url',
        'html_url': 'html_url',
        'number': 'number',
        'repository_id': 'repository_id',
        'state': 'state',
        'title': 'title',
        'description': 'description',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'open_issues': 'open_issues',
        'closed_issues': 'closed_issues',
        'due_on': 'due_on'
    }

    def __init__(self, url=None, html_url=None, number=None, repository_id=None, state=None, title=None, description=None, updated_at=None, created_at=None, open_issues=None, closed_issues=None, due_on=None):  # noqa: E501
        """Milestone - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._html_url = None
        self._number = None
        self._repository_id = None
        self._state = None
        self._title = None
        self._description = None
        self._updated_at = None
        self._created_at = None
        self._open_issues = None
        self._closed_issues = None
        self._due_on = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if html_url is not None:
            self.html_url = html_url
        if number is not None:
            self.number = number
        if repository_id is not None:
            self.repository_id = repository_id
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at
        if open_issues is not None:
            self.open_issues = open_issues
        if closed_issues is not None:
            self.closed_issues = closed_issues
        if due_on is not None:
            self.due_on = due_on

    @property
    def url(self):
        """Gets the url of this Milestone.  # noqa: E501


        :return: The url of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Milestone.


        :param url: The url of this Milestone.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def html_url(self):
        """Gets the html_url of this Milestone.  # noqa: E501


        :return: The html_url of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Milestone.


        :param html_url: The html_url of this Milestone.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def number(self):
        """Gets the number of this Milestone.  # noqa: E501


        :return: The number of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Milestone.


        :param number: The number of this Milestone.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def repository_id(self):
        """Gets the repository_id of this Milestone.  # noqa: E501


        :return: The repository_id of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Milestone.


        :param repository_id: The repository_id of this Milestone.  # noqa: E501
        :type: int
        """

        self._repository_id = repository_id

    @property
    def state(self):
        """Gets the state of this Milestone.  # noqa: E501


        :return: The state of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Milestone.


        :param state: The state of this Milestone.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this Milestone.  # noqa: E501


        :return: The title of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Milestone.


        :param title: The title of this Milestone.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Milestone.  # noqa: E501


        :return: The description of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Milestone.


        :param description: The description of this Milestone.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def updated_at(self):
        """Gets the updated_at of this Milestone.  # noqa: E501


        :return: The updated_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Milestone.


        :param updated_at: The updated_at of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this Milestone.  # noqa: E501


        :return: The created_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Milestone.


        :param created_at: The created_at of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def open_issues(self):
        """Gets the open_issues of this Milestone.  # noqa: E501


        :return: The open_issues of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._open_issues

    @open_issues.setter
    def open_issues(self, open_issues):
        """Sets the open_issues of this Milestone.


        :param open_issues: The open_issues of this Milestone.  # noqa: E501
        :type: int
        """

        self._open_issues = open_issues

    @property
    def closed_issues(self):
        """Gets the closed_issues of this Milestone.  # noqa: E501


        :return: The closed_issues of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._closed_issues

    @closed_issues.setter
    def closed_issues(self, closed_issues):
        """Sets the closed_issues of this Milestone.


        :param closed_issues: The closed_issues of this Milestone.  # noqa: E501
        :type: int
        """

        self._closed_issues = closed_issues

    @property
    def due_on(self):
        """Gets the due_on of this Milestone.  # noqa: E501


        :return: The due_on of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this Milestone.


        :param due_on: The due_on of this Milestone.  # noqa: E501
        :type: str
        """

        self._due_on = due_on

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
        if issubclass(Milestone, dict):
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
        if not isinstance(other, Milestone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
