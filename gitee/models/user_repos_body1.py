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

class UserReposBody1(object):
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
        'has_issues': 'bool',
        'has_wiki': 'bool',
        'can_comment': 'bool',
        'auto_init': 'bool',
        'gitignore_template': 'str',
        'license_template': 'str',
        'private': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'name': 'name',
        'description': 'description',
        'homepage': 'homepage',
        'has_issues': 'has_issues',
        'has_wiki': 'has_wiki',
        'can_comment': 'can_comment',
        'auto_init': 'auto_init',
        'gitignore_template': 'gitignore_template',
        'license_template': 'license_template',
        'private': 'private'
    }

    def __init__(self, access_token=None, name=None, description=None, homepage=None, has_issues=True, has_wiki=True, can_comment=True, auto_init=None, gitignore_template=None, license_template=None, private=None):  # noqa: E501
        """UserReposBody1 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._name = None
        self._description = None
        self._homepage = None
        self._has_issues = None
        self._has_wiki = None
        self._can_comment = None
        self._auto_init = None
        self._gitignore_template = None
        self._license_template = None
        self._private = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
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
        if auto_init is not None:
            self.auto_init = auto_init
        if gitignore_template is not None:
            self.gitignore_template = gitignore_template
        if license_template is not None:
            self.license_template = license_template
        if private is not None:
            self.private = private

    @property
    def access_token(self):
        """Gets the access_token of this UserReposBody1.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this UserReposBody1.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this UserReposBody1.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def name(self):
        """Gets the name of this UserReposBody1.  # noqa: E501

        仓库名称  # noqa: E501

        :return: The name of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserReposBody1.

        仓库名称  # noqa: E501

        :param name: The name of this UserReposBody1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UserReposBody1.  # noqa: E501

        仓库描述  # noqa: E501

        :return: The description of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserReposBody1.

        仓库描述  # noqa: E501

        :param description: The description of this UserReposBody1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def homepage(self):
        """Gets the homepage of this UserReposBody1.  # noqa: E501

        主页(eg: https://gitee.com)  # noqa: E501

        :return: The homepage of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this UserReposBody1.

        主页(eg: https://gitee.com)  # noqa: E501

        :param homepage: The homepage of this UserReposBody1.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def has_issues(self):
        """Gets the has_issues of this UserReposBody1.  # noqa: E501

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :return: The has_issues of this UserReposBody1.  # noqa: E501
        :rtype: bool
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this UserReposBody1.

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :param has_issues: The has_issues of this UserReposBody1.  # noqa: E501
        :type: bool
        """

        self._has_issues = has_issues

    @property
    def has_wiki(self):
        """Gets the has_wiki of this UserReposBody1.  # noqa: E501

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :return: The has_wiki of this UserReposBody1.  # noqa: E501
        :rtype: bool
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this UserReposBody1.

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :param has_wiki: The has_wiki of this UserReposBody1.  # noqa: E501
        :type: bool
        """

        self._has_wiki = has_wiki

    @property
    def can_comment(self):
        """Gets the can_comment of this UserReposBody1.  # noqa: E501

        允许用户对仓库进行评论。默认: 允许(true)  # noqa: E501

        :return: The can_comment of this UserReposBody1.  # noqa: E501
        :rtype: bool
        """
        return self._can_comment

    @can_comment.setter
    def can_comment(self, can_comment):
        """Sets the can_comment of this UserReposBody1.

        允许用户对仓库进行评论。默认: 允许(true)  # noqa: E501

        :param can_comment: The can_comment of this UserReposBody1.  # noqa: E501
        :type: bool
        """

        self._can_comment = can_comment

    @property
    def auto_init(self):
        """Gets the auto_init of this UserReposBody1.  # noqa: E501

        值为true时则会用README初始化仓库。默认: 不初始化(false)  # noqa: E501

        :return: The auto_init of this UserReposBody1.  # noqa: E501
        :rtype: bool
        """
        return self._auto_init

    @auto_init.setter
    def auto_init(self, auto_init):
        """Sets the auto_init of this UserReposBody1.

        值为true时则会用README初始化仓库。默认: 不初始化(false)  # noqa: E501

        :param auto_init: The auto_init of this UserReposBody1.  # noqa: E501
        :type: bool
        """

        self._auto_init = auto_init

    @property
    def gitignore_template(self):
        """Gets the gitignore_template of this UserReposBody1.  # noqa: E501

        Git Ingore模版  # noqa: E501

        :return: The gitignore_template of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._gitignore_template

    @gitignore_template.setter
    def gitignore_template(self, gitignore_template):
        """Sets the gitignore_template of this UserReposBody1.

        Git Ingore模版  # noqa: E501

        :param gitignore_template: The gitignore_template of this UserReposBody1.  # noqa: E501
        :type: str
        """
        allowed_values = ["Actionscript", "Ada", "Agda", "Android", "AppEngine", "AppceleratorTitanium", "ArchLinuxPackages", "Autotools", "C", "C++", "CFWheels", "CMake", "CUDA", "CakePHP", "ChefCookbook", "Clojure", "CodeIgniter", "CommonLisp", "Composer", "Concrete5", "Coq", "CraftCMS", "D", "DM", "Dart", "Delphi", "Drupal", "EPiServer", "Eagle", "Elisp", "Elixir", "Elm", "Erlang", "ExpressionEngine", "ExtJs", "Fancy", "Finale", "Flutter", "ForceDotCom", "Fortran", "FuelPHP", "GWT", "Gcov", "GitBook", "Global/Anjuta", "Global/Ansible", "Global/Archives", "Global/Backup", "Global/Bazaar", "Global/BricxCC", "Global/CVS", "Global/Calabash", "Global/Cloud9", "Global/CodeKit", "Global/DartEditor", "Global/Diff", "Global/Dreamweaver", "Global/Dropbox", "Global/Eclipse", "Global/EiffelStudio", "Global/Emacs", "Global/Ensime", "Global/Espresso", "Global/FlexBuilder", "Global/GPG", "Global/Images", "Global/JDeveloper", "Global/JEnv", "Global/JetBrains", "Global/KDevelop4", "Global/Kate", "Global/Lazarus", "Global/LibreOffice", "Global/Linux", "Global/LyX", "Global/MATLAB", "Global/Mercurial", "Global/MicrosoftOffice", "Global/ModelSim", "Global/Momentics", "Global/MonoDevelop", "Global/NetBeans", "Global/Ninja", "Global/NotepadPP", "Global/Octave", "Global/Otto", "Global/PSoCCreator", "Global/Patch", "Global/PuTTY", "Global/Redcar", "Global/Redis", "Global/SBT", "Global/SVN", "Global/SlickEdit", "Global/Stata", "Global/SublimeText", "Global/SynopsysVCS", "Global/Tags", "Global/TextMate", "Global/TortoiseGit", "Global/Vagrant", "Global/Vim", "Global/VirtualEnv", "Global/Virtuoso", "Global/VisualStudioCode", "Global/WebMethods", "Global/Windows", "Global/Xcode", "Global/XilinxISE", "Global/macOS", "Go", "Godot", "Gradle", "Grails", "Haskell", "IGORPro", "Idris", "JBoss", "Java", "Jekyll", "Joomla", "Julia", "KiCad", "Kohana", "Kotlin", "LabVIEW", "Laravel", "Leiningen", "LemonStand", "Lilypond", "Lithium", "Lua", "Magento", "Maven", "Mercury", "MetaProgrammingSystem", "MiniProgram", "Nanoc", "Nim", "Node", "OCaml", "Objective-C", "Opa", "OpenCart", "OracleForms", "Packer", "Perl", "Perl6", "Phalcon", "PlayFramework", "Plone", "Prestashop", "Processing", "PureScript", "Python", "Qooxdoo", "Qt", "R", "ROS", "Rails", "RhodesRhomobile", "Ruby", "Rust", "SCons", "Sass", "Scala", "Scheme", "Scrivener", "Sdcc", "SeamGen", "SketchUp", "Smalltalk", "Stella", "SugarCRM", "Swift", "Symfony", "SymphonyCMS", "TeX", "Terraform", "Textpattern", "TurboGears2", "Typo3", "Umbraco", "Unity", "UnrealEngine", "VVVV", "VisualStudio", "Waf", "WordPress", "Xojo", "Yeoman", "Yii", "ZendFramework", "Zephir"]  # noqa: E501
        if gitignore_template not in allowed_values:
            raise ValueError(
                "Invalid value for `gitignore_template` ({0}), must be one of {1}"  # noqa: E501
                .format(gitignore_template, allowed_values)
            )

        self._gitignore_template = gitignore_template

    @property
    def license_template(self):
        """Gets the license_template of this UserReposBody1.  # noqa: E501

        License模版  # noqa: E501

        :return: The license_template of this UserReposBody1.  # noqa: E501
        :rtype: str
        """
        return self._license_template

    @license_template.setter
    def license_template(self, license_template):
        """Sets the license_template of this UserReposBody1.

        License模版  # noqa: E501

        :param license_template: The license_template of this UserReposBody1.  # noqa: E501
        :type: str
        """
        allowed_values = ["MulanPSL-1.0", "AFL-3.0", "AGPL-3.0", "Apache-2.0", "Artistic-2.0", "BSD-2-Clause", "BSD-3-Clause", "BSD-3-Clause-Clear", "BSL-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "CC0-1.0", "ECL-2.0", "EPL-1.0", "EUPL-1.1", "GPL-2.0", "GPL-3.0", "ISC", "LGPL-2.1", "LGPL-3.0", "LPPL-1.3c", "MIT", "MPL-2.0", "MS-PL", "MS-RL", "NCSA", "OFL-1.1", "OSL-3.0", "PostgreSQL", "Unlicense", "WTFPL", "Zlib"]  # noqa: E501
        if license_template not in allowed_values:
            raise ValueError(
                "Invalid value for `license_template` ({0}), must be one of {1}"  # noqa: E501
                .format(license_template, allowed_values)
            )

        self._license_template = license_template

    @property
    def private(self):
        """Gets the private of this UserReposBody1.  # noqa: E501

        仓库公开或私有。默认: 公开(false)  # noqa: E501

        :return: The private of this UserReposBody1.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this UserReposBody1.

        仓库公开或私有。默认: 公开(false)  # noqa: E501

        :param private: The private of this UserReposBody1.  # noqa: E501
        :type: bool
        """

        self._private = private

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
        if issubclass(UserReposBody1, dict):
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
        if not isinstance(other, UserReposBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
