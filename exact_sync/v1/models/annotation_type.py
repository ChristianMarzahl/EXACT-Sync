# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AnnotationType(object):
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
        'name': 'str',
        'vector_type': 'int',
        'node_count': 'int',
        'enable_concealed': 'bool',
        'enable_blurred': 'bool',
        'color_code': 'str',
        'default_width': 'int',
        'default_height': 'int',
        'sort_order': 'int',
        'closed': 'bool',
        'area_hit_test': 'bool',
        'product': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vector_type': 'vector_type',
        'node_count': 'node_count',
        'enable_concealed': 'enable_concealed',
        'enable_blurred': 'enable_blurred',
        'color_code': 'color_code',
        'default_width': 'default_width',
        'default_height': 'default_height',
        'sort_order': 'sort_order',
        'closed': 'closed',
        'area_hit_test': 'area_hit_test',
        'product': 'product'
    }

    class VECTOR_TYPE():
        BOUNDING_BOX = 1
        POINT = 2
        LINE = 3
        MULTI_LINE = 4
        POLYGON = 5
        FIXED_SIZE_BOUNDING_BOX = 6
        GLOBAL = 7 #Annotations without a shape that are valid for the whole image

    def __init__(self, id=None, name=None, vector_type:int=1, node_count=1, enable_concealed=1, enable_blurred=None, color_code="#FF0000", default_width=50, default_height=50, sort_order=0, closed=1, area_hit_test=1, product=None):  # noqa: E501
        """AnnotationType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._vector_type = None
        self._node_count = None
        self._enable_concealed = None
        self._enable_blurred = None
        self._color_code = None
        self._default_width = None
        self._default_height = None
        self._sort_order = None
        self._closed = None
        self._area_hit_test = None
        self._product = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if vector_type is not None:
            self.vector_type = vector_type
        if node_count is not None:
            self.node_count = node_count
        if enable_concealed is not None:
            self.enable_concealed = enable_concealed
        if enable_blurred is not None:
            self.enable_blurred = enable_blurred
        if color_code is not None:
            self.color_code = color_code
        if default_width is not None:
            self.default_width = default_width
        if default_height is not None:
            self.default_height = default_height
        if sort_order is not None:
            self.sort_order = sort_order
        if closed is not None:
            self.closed = closed
        if area_hit_test is not None:
            self.area_hit_test = area_hit_test
        self.product = product

    @property
    def id(self):
        """Gets the id of this AnnotationType.  # noqa: E501


        :return: The id of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnnotationType.


        :param id: The id of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AnnotationType.  # noqa: E501


        :return: The name of this AnnotationType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotationType.


        :param name: The name of this AnnotationType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vector_type(self):
        """Gets the vector_type of this AnnotationType.  # noqa: E501


        :return: The vector_type of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._vector_type

    @vector_type.setter
    def vector_type(self, vector_type):
        """Sets the vector_type of this AnnotationType.


        :param vector_type: The vector_type of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._vector_type = vector_type

    @property
    def node_count(self):
        """Gets the node_count of this AnnotationType.  # noqa: E501


        :return: The node_count of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this AnnotationType.


        :param node_count: The node_count of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._node_count = node_count

    @property
    def enable_concealed(self):
        """Gets the enable_concealed of this AnnotationType.  # noqa: E501


        :return: The enable_concealed of this AnnotationType.  # noqa: E501
        :rtype: bool
        """
        return self._enable_concealed

    @enable_concealed.setter
    def enable_concealed(self, enable_concealed):
        """Sets the enable_concealed of this AnnotationType.


        :param enable_concealed: The enable_concealed of this AnnotationType.  # noqa: E501
        :type: bool
        """

        self._enable_concealed = enable_concealed

    @property
    def enable_blurred(self):
        """Gets the enable_blurred of this AnnotationType.  # noqa: E501


        :return: The enable_blurred of this AnnotationType.  # noqa: E501
        :rtype: bool
        """
        return self._enable_blurred

    @enable_blurred.setter
    def enable_blurred(self, enable_blurred):
        """Sets the enable_blurred of this AnnotationType.


        :param enable_blurred: The enable_blurred of this AnnotationType.  # noqa: E501
        :type: bool
        """

        self._enable_blurred = enable_blurred

    @property
    def color_code(self):
        """Gets the color_code of this AnnotationType.  # noqa: E501


        :return: The color_code of this AnnotationType.  # noqa: E501
        :rtype: str
        """
        return self._color_code

    @color_code.setter
    def color_code(self, color_code):
        """Sets the color_code of this AnnotationType.


        :param color_code: The color_code of this AnnotationType.  # noqa: E501
        :type: str
        """

        self._color_code = color_code

    @property
    def default_width(self):
        """Gets the default_width of this AnnotationType.  # noqa: E501


        :return: The default_width of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._default_width

    @default_width.setter
    def default_width(self, default_width):
        """Sets the default_width of this AnnotationType.


        :param default_width: The default_width of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._default_width = default_width

    @property
    def default_height(self):
        """Gets the default_height of this AnnotationType.  # noqa: E501


        :return: The default_height of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._default_height

    @default_height.setter
    def default_height(self, default_height):
        """Sets the default_height of this AnnotationType.


        :param default_height: The default_height of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._default_height = default_height

    @property
    def sort_order(self):
        """Gets the sort_order of this AnnotationType.  # noqa: E501


        :return: The sort_order of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AnnotationType.


        :param sort_order: The sort_order of this AnnotationType.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def closed(self):
        """Gets the closed of this AnnotationType.  # noqa: E501


        :return: The closed of this AnnotationType.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this AnnotationType.


        :param closed: The closed of this AnnotationType.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def area_hit_test(self):
        """Gets the area_hit_test of this AnnotationType.  # noqa: E501


        :return: The area_hit_test of this AnnotationType.  # noqa: E501
        :rtype: bool
        """
        return self._area_hit_test

    @area_hit_test.setter
    def area_hit_test(self, area_hit_test):
        """Sets the area_hit_test of this AnnotationType.


        :param area_hit_test: The area_hit_test of this AnnotationType.  # noqa: E501
        :type: bool
        """

        self._area_hit_test = area_hit_test

    @property
    def product(self):
        """Gets the product of this AnnotationType.  # noqa: E501


        :return: The product of this AnnotationType.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AnnotationType.


        :param product: The product of this AnnotationType.  # noqa: E501
        :type: int
        """
        #if product is None:
        #    raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

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
        if issubclass(AnnotationType, dict):
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
        if not isinstance(other, AnnotationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
