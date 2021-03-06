# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from enum import Enum, IntEnum
import six


class Image(object):
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

    class ImageSourceTypes(IntEnum):
        DEFAULT = 0
        SERVER_GENERATED = 1
        FILE_LINK = 2

    swagger_types = {
        'id': 'int',
        'name': 'str',
        'filename': 'str',
        'time': 'datetime',
        'height': 'int',
        'width': 'int',
        'mpp': 'float',
        'objective_power': 'float',
        'image_type': 'int',
        'image_set': 'int',
        'annotations': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'filename': 'filename',
        'time': 'time',
        'height': 'height',
        'width': 'width',
        'mpp': 'mpp',
        'objective_power': 'objectivePower',
        'image_type': 'image_type',
        'image_set': 'image_set',
        'annotations': 'annotations'
    }

    def __init__(self, id=None, name=None, filename=None, time=None, height=None, width=None, mpp=None, objective_power=None, image_type=None, image_set=None, annotations=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._filename = None
        self._time = None
        self._height = None
        self._width = None
        self._mpp = None
        self._objective_power = None
        self._image_type = None
        self._image_set = None
        self._annotations = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.filename = filename
        if time is not None:
            self.time = time
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if mpp is not None:
            self.mpp = mpp
        if objective_power is not None:
            self.objective_power = objective_power
        if image_type is not None:
            self.image_type = image_type
        self.image_set = image_set
        self.annotations = annotations

    @property
    def id(self):
        """Gets the id of this Image.  # noqa: E501


        :return: The id of this Image.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.


        :param id: The id of this Image.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Image.  # noqa: E501


        :return: The name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Image.


        :param name: The name of this Image.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def filename(self):
        """Gets the filename of this Image.  # noqa: E501


        :return: The filename of this Image.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Image.


        :param filename: The filename of this Image.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def time(self):
        """Gets the time of this Image.  # noqa: E501


        :return: The time of this Image.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Image.


        :param time: The time of this Image.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def height(self):
        """Gets the height of this Image.  # noqa: E501


        :return: The height of this Image.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Image.


        :param height: The height of this Image.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this Image.  # noqa: E501


        :return: The width of this Image.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Image.


        :param width: The width of this Image.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def mpp(self):
        """Gets the mpp of this Image.  # noqa: E501


        :return: The mpp of this Image.  # noqa: E501
        :rtype: float
        """
        return self._mpp

    @mpp.setter
    def mpp(self, mpp):
        """Sets the mpp of this Image.


        :param mpp: The mpp of this Image.  # noqa: E501
        :type: float
        """

        self._mpp = mpp

    @property
    def objective_power(self):
        """Gets the objective_power of this Image.  # noqa: E501


        :return: The objective_power of this Image.  # noqa: E501
        :rtype: float
        """
        return self._objective_power

    @objective_power.setter
    def objective_power(self, objective_power):
        """Sets the objective_power of this Image.


        :param objective_power: The objective_power of this Image.  # noqa: E501
        :type: float
        """

        self._objective_power = objective_power

    @property
    def image_type(self):
        """Gets the image_type of this Image.  # noqa: E501


        :return: The image_type of this Image.  # noqa: E501
        :rtype: float
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this Image.


        :param image_type: The image_type of this Image.  # noqa: E501
        :type: float
        """

        self._image_type = image_type

    @property
    def image_set(self):
        """Gets the image_set of this Image.  # noqa: E501


        :return: The image_set of this Image.  # noqa: E501
        :rtype: int
        """
        return self._image_set

    @image_set.setter
    def image_set(self, image_set):
        """Sets the image_set of this Image.


        :param image_set: The image_set of this Image.  # noqa: E501
        :type: int
        """
        if image_set is None:
            image_set = "image_set not load please remove omit=image_set"
        #if image_set is None:
        #    raise ValueError("Invalid value for `image_set`, must not be `None`")  # noqa: E501

        self._image_set = image_set

    @property
    def annotations(self):
        """Gets the annotations of this Image.  # noqa: E501


        :return: The annotations of this Image.  # noqa: E501
        :rtype: list[int]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Image.


        :param annotations: The annotations of this Image.  # noqa: E501
        :type: list[int]
        """
        if annotations is None:
            annotations = "Annotations not load please remove omit=annotations"
        #    raise ValueError("Invalid value for `annotations`, must not be `None`")  # noqa: E501

        self._annotations = annotations

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
