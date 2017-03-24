# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceConfiguration(Model):
    """ResourceConfiguration.

    :param create_if_not_found:
    :type create_if_not_found: bool
    :param properties:
    :type properties: list of :class:`Property <azuretfs.models.Property>`
    :param resource_name:
    :type resource_name: str
    """

    _attribute_map = {
        'create_if_not_found': {'key': 'createIfNotFound', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': '[Property]'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
    }

    def __init__(self, create_if_not_found=None, properties=None, resource_name=None):
        self.create_if_not_found = create_if_not_found
        self.properties = properties
        self.resource_name = resource_name
