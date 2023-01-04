# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PluginResultAnnotation(object):
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
        'annotation_type': 'int',
        'pluginresultentry': 'int',
        'meta_data': 'object',
        'vector': 'object',
        'unique_identifier': 'str',
        'generated': 'str',
        'image': 'int',
        'time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'annotation_type': 'annotation_type',
        'pluginresultentry': 'pluginresultentry',
        'meta_data': 'meta_data',
        'vector': 'vector',
        'unique_identifier': 'unique_identifier',
        'generated': 'generated',
        'image': 'image',
        'time': 'time'
    }

    def __init__(self, id=None, annotation_type=None, pluginresultentry=None, meta_data=None, vector=None, unique_identifier=None, generated=None, image=None, time=None):  # noqa: E501
        """PluginResultAnnotation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._annotation_type = None
        self._pluginresultentry = None
        self._meta_data = None
        self._vector = None
        self._unique_identifier = None
        self._generated = None
        self._image = None
        self._time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.annotation_type = annotation_type
        self.pluginresultentry = pluginresultentry
        if meta_data is not None:
            self.meta_data = meta_data
        if vector is not None:
            self.vector = vector
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if generated is not None:
            self.generated = generated
        self.image = image
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this PluginResultAnnotation.  # noqa: E501


        :return: The id of this PluginResultAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PluginResultAnnotation.


        :param id: The id of this PluginResultAnnotation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def annotation_type(self):
        """Gets the annotation_type of this PluginResultAnnotation.  # noqa: E501


        :return: The annotation_type of this PluginResultAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._annotation_type

    @annotation_type.setter
    def annotation_type(self, annotation_type):
        """Sets the annotation_type of this PluginResultAnnotation.


        :param annotation_type: The annotation_type of this PluginResultAnnotation.  # noqa: E501
        :type: int
        """
        if annotation_type is None:
            raise ValueError("Invalid value for `annotation_type`, must not be `None`")  # noqa: E501

        self._annotation_type = annotation_type

    @property
    def pluginresultentry(self):
        """Gets the pluginresultentry of this PluginResultAnnotation.  # noqa: E501


        :return: The pluginresultentry of this PluginResultAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._pluginresultentry

    @pluginresultentry.setter
    def pluginresultentry(self, pluginresultentry):
        """Sets the pluginresultentry of this PluginResultAnnotation.


        :param pluginresultentry: The pluginresultentry of this PluginResultAnnotation.  # noqa: E501
        :type: int
        """
        if pluginresultentry is None:
            raise ValueError("Invalid value for `pluginresultentry`, must not be `None`")  # noqa: E501

        self._pluginresultentry = pluginresultentry

    @property
    def meta_data(self):
        """Gets the meta_data of this PluginResultAnnotation.  # noqa: E501


        :return: The meta_data of this PluginResultAnnotation.  # noqa: E501
        :rtype: object
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this PluginResultAnnotation.


        :param meta_data: The meta_data of this PluginResultAnnotation.  # noqa: E501
        :type: object
        """

        self._meta_data = meta_data

    @property
    def vector(self):
        """Gets the vector of this PluginResultAnnotation.  # noqa: E501


        :return: The vector of this PluginResultAnnotation.  # noqa: E501
        :rtype: object
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this PluginResultAnnotation.


        :param vector: The vector of this PluginResultAnnotation.  # noqa: E501
        :type: object
        """

        self._vector = vector

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this PluginResultAnnotation.  # noqa: E501


        :return: The unique_identifier of this PluginResultAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this PluginResultAnnotation.


        :param unique_identifier: The unique_identifier of this PluginResultAnnotation.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def generated(self):
        """Gets the generated of this PluginResultAnnotation.  # noqa: E501


        :return: The generated of this PluginResultAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this PluginResultAnnotation.


        :param generated: The generated of this PluginResultAnnotation.  # noqa: E501
        :type: str
        """

        self._generated = generated

    @property
    def image(self):
        """Gets the image of this PluginResultAnnotation.  # noqa: E501


        :return: The image of this PluginResultAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PluginResultAnnotation.


        :param image: The image of this PluginResultAnnotation.  # noqa: E501
        :type: int
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def time(self):
        """Gets the time of this PluginResultAnnotation.  # noqa: E501


        :return: The time of this PluginResultAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this PluginResultAnnotation.


        :param time: The time of this PluginResultAnnotation.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if issubclass(PluginResultAnnotation, dict):
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
        if not isinstance(other, PluginResultAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
