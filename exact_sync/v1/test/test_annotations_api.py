# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
import uuid

from exact_sync.v1.api_client import ApiClient as client

from exact_sync.v1.api.annotations_api import AnnotationsApi  # noqa: E501

from exact_sync.v1.api.images_api import ImagesApi  # noqa: E501
from exact_sync.v1.api.teams_api import TeamsApi
from exact_sync.v1.api.image_sets_api import ImageSetsApi
from exact_sync.v1.api.products_api import ProductsApi
from exact_sync.v1.api.annotation_types_api import AnnotationTypesApi  # noqa: E501

from exact_sync.v1.rest import ApiException
from exact_sync.v1.models import ImageSet, Team, Product, AnnotationType, Image, Annotation


class TestAnnotationsApi(unittest.TestCase):
    """AnnotationsApi unit test stubs"""

    def setUp(self):
        self.api = AnnotationsApi()  # noqa: E501
        self.team_api = TeamsApi()
        self.image_sets_api = ImageSetsApi()
        self.product_api = ProductsApi()
        self.anno_type_api = AnnotationTypesApi()
        self.image_api = ImagesApi()

        # create dummy team, image_sets, product, image and anno_type
        teams = self.team_api.list_teams(name="test_annotation")
        if teams.count == 0:
            team = Team(name="test_annotation")
            team = self.team_api.create_team(body=team) 
        else:
            team = teams.results[0]

        image_sets = self.image_sets_api.list_image_sets(name="test_annotation")
        if image_sets.count == 0:
            image_set = ImageSet(name="test_annotation", team=team.id)
            image_set = self.image_sets_api.create_image_set(body=image_set)
        else:
            image_set = image_sets.results[0]

        products = self.product_api.list_products(name="test_annotation")
        if products.count == 0:
            product = Product(name="test_annotation", imagesets=[image_set.id], team=team.id)
            product = self.product_api.create_product(body=product)
        else:
            product = products.results[0]

        annotation_types = self.anno_type_api.list_annotation_types(name="test_annotation")
        if annotation_types.count == 0:
            annotation_type = AnnotationType(name="test_annotation", vector_type=int(AnnotationType.VECTOR_TYPE.BOUNDING_BOX), product=product.id)
            annotation_type = self.anno_type_api.create_annotation_type(body=annotation_type)
        else:
            annotation_type = annotation_types.results[0]

        images = self.image_api.list_images(name="Eosinophile.png")
        if images.count == 0:
            file_path = "exact_sync/v1/test/images/Eosinophile.png"
            image_type = 0
            
            images = self.image_api.create_image(file_path=file_path, image_type=image_type, image_set=image_set.id)
            image = images.results[0]
        else:
            image = images.results[0]

        self.team = team
        self.image_set = image_set 
        self.product = product 
        self.annotation_type = annotation_type
        self.image = image

    def tearDown(self):

        self.image_api.destroy_image(id=self.image.id)
        self.anno_type_api.destroy_annotation_type(id=self.annotation_type.id)
        self.product_api.destroy_product(id=self.product.id)
        self.image_sets_api.destroy_image_set(id=self.image_set.id)
        self.team_api.destroy_team(id=self.team.id)

        pass

    def test_create_annotation(self):
        """Test case for create_annotation

        """
        vector = {"x1":10, "x2":20, "y1":10, "y2":20}
        unique_identifier = str(uuid.uuid4())
        time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        annotation = Annotation(annotation_type=self.annotation_type.id, time=time, vector=vector, image=self.image.id, unique_identifier=unique_identifier)
        created_annotation = self.api.create_annotation(body=annotation)
        
        assert created_annotation.unique_identifier == unique_identifier
        assert created_annotation.time == time
        self.api.destroy_annotation(id=created_annotation.id)

    def test_destroy_annotation(self):
        """Test case for destroy_annotation

        """
        assert False

    def test_list_annotations(self):
        """Test case for list_annotations

        """
        annotations = self.api.list_annotations(omit="annotation_types")
        pass

    def test_partial_update_annotation(self):
        """Test case for partial_update_annotation

        """
        vector = {"x1":10, "x2":20, "y1":10, "y2":20}
        unique_identifier = str(uuid.uuid4())
        last_edit_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

        annotation = Annotation(annotation_type=self.annotation_type.id, vector=vector, image=self.image.id, unique_identifier=unique_identifier)
        created_annotation = self.api.create_annotation(body=annotation)
        
        new_vector = {"x1":100, "x2":200, "y1":100, "y2":200}
        updated_annotation = self.api.partial_update_annotation(id=created_annotation.id, last_edit_time=last_edit_time, vector=new_vector)
        
        assert new_vector == updated_annotation.vector
        assert last_edit_time == updated_annotation.last_edit_time
        self.api.destroy_annotation(id=created_annotation.id)

    def test_retrieve_annotation(self):
        """Test case for retrieve_annotation

        """
        annotations = self.api.list_annotations(omit="annotation_types")
        anno = annotations.results[0]
        annotation = self.api.retrieve_annotation(id=anno.id)
        pass

    def test_update_annotation(self):
        """Test case for update_annotation

        """
        vector = {"x1":10, "x2":20, "y1":10, "y2":20}
        unique_identifier = str(uuid.uuid4())
        annotation = Annotation(annotation_type=self.annotation_type.id, vector=vector, image=self.image.id, unique_identifier=unique_identifier)
        created_annotation = self.api.create_annotation(body=annotation)
        
        created_annotation.deleted = True
        updated_annotation = self.api.update_annotation(id=created_annotation.id, body=created_annotation)
        
        assert created_annotation.deleted == updated_annotation.deleted
        self.api.destroy_annotation(id=created_annotation.id)


if __name__ == '__main__':
    unittest.main()
