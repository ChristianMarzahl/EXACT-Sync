# swagger_client.AnnotationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationsApi.md#create_annotation) | **POST** /api/v1/annotations/annotations/ | 
[**create_annotation_media_file**](AnnotationsApi.md#create_annotation_media_file) | **POST** /api/v1/annotations/annotation_media_files/ | 
[**create_annotation_type**](AnnotationsApi.md#create_annotation_type) | **POST** /api/v1/annotations/annotation_types/ | 
[**create_annotation_version**](AnnotationsApi.md#create_annotation_version) | **POST** /api/v1/annotations/annotation_versions/ | 
[**create_log_image_action**](AnnotationsApi.md#create_log_image_action) | **POST** /api/v1/annotations/log_image_actions/ | 
[**create_verification**](AnnotationsApi.md#create_verification) | **POST** /api/v1/annotations/verifications/ | 
[**destroy_annotation**](AnnotationsApi.md#destroy_annotation) | **DELETE** /api/v1/annotations/annotations/{id}/ | 
[**destroy_annotation_media_file**](AnnotationsApi.md#destroy_annotation_media_file) | **DELETE** /api/v1/annotations/annotation_media_files/{id}/ | 
[**destroy_annotation_type**](AnnotationsApi.md#destroy_annotation_type) | **DELETE** /api/v1/annotations/annotation_types/{id}/ | 
[**destroy_annotation_version**](AnnotationsApi.md#destroy_annotation_version) | **DELETE** /api/v1/annotations/annotation_versions/{id}/ | 
[**destroy_log_image_action**](AnnotationsApi.md#destroy_log_image_action) | **DELETE** /api/v1/annotations/log_image_actions/{id}/ | 
[**destroy_verification**](AnnotationsApi.md#destroy_verification) | **DELETE** /api/v1/annotations/verifications/{id}/ | 
[**list_annotation_media_files**](AnnotationsApi.md#list_annotation_media_files) | **GET** /api/v1/annotations/annotation_media_files/ | 
[**list_annotation_types**](AnnotationsApi.md#list_annotation_types) | **GET** /api/v1/annotations/annotation_types/ | 
[**list_annotation_versions**](AnnotationsApi.md#list_annotation_versions) | **GET** /api/v1/annotations/annotation_versions/ | 
[**list_annotations**](AnnotationsApi.md#list_annotations) | **GET** /api/v1/annotations/annotations/ | 
[**list_log_image_actions**](AnnotationsApi.md#list_log_image_actions) | **GET** /api/v1/annotations/log_image_actions/ | 
[**list_verifications**](AnnotationsApi.md#list_verifications) | **GET** /api/v1/annotations/verifications/ | 
[**partial_update_annotation**](AnnotationsApi.md#partial_update_annotation) | **PATCH** /api/v1/annotations/annotations/{id}/ | 
[**partial_update_annotation_media_file**](AnnotationsApi.md#partial_update_annotation_media_file) | **PATCH** /api/v1/annotations/annotation_media_files/{id}/ | 
[**partial_update_annotation_type**](AnnotationsApi.md#partial_update_annotation_type) | **PATCH** /api/v1/annotations/annotation_types/{id}/ | 
[**partial_update_annotation_version**](AnnotationsApi.md#partial_update_annotation_version) | **PATCH** /api/v1/annotations/annotation_versions/{id}/ | 
[**partial_update_log_image_action**](AnnotationsApi.md#partial_update_log_image_action) | **PATCH** /api/v1/annotations/log_image_actions/{id}/ | 
[**partial_update_verification**](AnnotationsApi.md#partial_update_verification) | **PATCH** /api/v1/annotations/verifications/{id}/ | 
[**retrieve_annotation**](AnnotationsApi.md#retrieve_annotation) | **GET** /api/v1/annotations/annotations/{id}/ | 
[**retrieve_annotation_media_file**](AnnotationsApi.md#retrieve_annotation_media_file) | **GET** /api/v1/annotations/annotation_media_files/{id}/ | 
[**retrieve_annotation_type**](AnnotationsApi.md#retrieve_annotation_type) | **GET** /api/v1/annotations/annotation_types/{id}/ | 
[**retrieve_annotation_version**](AnnotationsApi.md#retrieve_annotation_version) | **GET** /api/v1/annotations/annotation_versions/{id}/ | 
[**retrieve_log_image_action**](AnnotationsApi.md#retrieve_log_image_action) | **GET** /api/v1/annotations/log_image_actions/{id}/ | 
[**retrieve_verification**](AnnotationsApi.md#retrieve_verification) | **GET** /api/v1/annotations/verifications/{id}/ | 
[**update_annotation**](AnnotationsApi.md#update_annotation) | **PUT** /api/v1/annotations/annotations/{id}/ | 
[**update_annotation_media_file**](AnnotationsApi.md#update_annotation_media_file) | **PUT** /api/v1/annotations/annotation_media_files/{id}/ | 
[**update_annotation_type**](AnnotationsApi.md#update_annotation_type) | **PUT** /api/v1/annotations/annotation_types/{id}/ | 
[**update_annotation_version**](AnnotationsApi.md#update_annotation_version) | **PUT** /api/v1/annotations/annotation_versions/{id}/ | 
[**update_log_image_action**](AnnotationsApi.md#update_log_image_action) | **PUT** /api/v1/annotations/log_image_actions/{id}/ | 
[**update_verification**](AnnotationsApi.md#update_verification) | **PUT** /api/v1/annotations/verifications/{id}/ | 

# **create_annotation**
> Annotation create_annotation(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.Annotation() # Annotation |  (optional)

try:
    api_response = api_instance.create_annotation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Annotation**](Annotation.md)|  | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation_media_file**
> AnnotationMediaFile create_annotation_media_file(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.AnnotationMediaFile() # AnnotationMediaFile |  (optional)

try:
    api_response = api_instance.create_annotation_media_file(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation_media_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationMediaFile**](AnnotationMediaFile.md)|  | [optional] 

### Return type

[**AnnotationMediaFile**](AnnotationMediaFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation_type**
> AnnotationType create_annotation_type(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.AnnotationType() # AnnotationType |  (optional)

try:
    api_response = api_instance.create_annotation_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationType**](AnnotationType.md)|  | [optional] 

### Return type

[**AnnotationType**](AnnotationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation_version**
> AnnotationVersion create_annotation_version(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.AnnotationVersion() # AnnotationVersion |  (optional)

try:
    api_response = api_instance.create_annotation_version(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationVersion**](AnnotationVersion.md)|  | [optional] 

### Return type

[**AnnotationVersion**](AnnotationVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_log_image_action**
> LogImageAction create_log_image_action(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.LogImageAction() # LogImageAction |  (optional)

try:
    api_response = api_instance.create_log_image_action(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_log_image_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogImageAction**](LogImageAction.md)|  | [optional] 

### Return type

[**LogImageAction**](LogImageAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_verification**
> Verification create_verification(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
body = swagger_client.Verification() # Verification |  (optional)

try:
    api_response = api_instance.create_verification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Verification**](Verification.md)|  | [optional] 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_annotation**
> destroy_annotation(id, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
last_edit_time = 'last_edit_time_example' # str | last_edit_time (optional)
last_edit_time__lte = 'last_edit_time__lte_example' # str | last_edit_time__lte (optional)
last_edit_time__gte = 'last_edit_time__gte_example' # str | last_edit_time__gte (optional)
last_edit_time__range = 'last_edit_time__range_example' # str | last_edit_time__range (optional)
unique_identifier = 'unique_identifier_example' # str | unique_identifier (optional)
unique_identifier__contains = 'unique_identifier__contains_example' # str | unique_identifier__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
deleted = 'deleted_example' # str | deleted (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
verified_by = 'verified_by_example' # str | verified_by (optional)
verified_by__range = 'verified_by__range_example' # str | verified_by__range (optional)
annotationversion = 'annotationversion_example' # str | annotationversion (optional)
vector_x = 'vector_x_example' # str | Vector-X-Range (optional)
vector_y = 'vector_y_example' # str | Vector-Y-Range (optional)
meta_data__isnull = 'meta_data__isnull_example' # str | meta_data__isnull (optional)
vector__isnull = 'vector__isnull_example' # str | vector__isnull (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)

try:
    api_instance.destroy_annotation(id, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **last_edit_time** | **str**| last_edit_time | [optional] 
 **last_edit_time__lte** | **str**| last_edit_time__lte | [optional] 
 **last_edit_time__gte** | **str**| last_edit_time__gte | [optional] 
 **last_edit_time__range** | **str**| last_edit_time__range | [optional] 
 **unique_identifier** | **str**| unique_identifier | [optional] 
 **unique_identifier__contains** | **str**| unique_identifier__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **verified_by** | **str**| verified_by | [optional] 
 **verified_by__range** | **str**| verified_by__range | [optional] 
 **annotationversion** | **str**| annotationversion | [optional] 
 **vector_x** | **str**| Vector-X-Range | [optional] 
 **vector_y** | **str**| Vector-Y-Range | [optional] 
 **meta_data__isnull** | **str**| meta_data__isnull | [optional] 
 **vector__isnull** | **str**| vector__isnull | [optional] 
 **vector_type** | **str**| vector_type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_annotation_media_file**
> destroy_annotation_media_file(id, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
annotation = 'annotation_example' # str | annotation (optional)
media_file_type = 'media_file_type_example' # str | media_file_type (optional)

try:
    api_instance.destroy_annotation_media_file(id, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_annotation_media_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **media_file_type** | **str**| media_file_type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_annotation_type**
> destroy_annotation_type(id, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)
vector_type__lte = 'vector_type__lte_example' # str | vector_type__lte (optional)
vector_type__gte = 'vector_type__gte_example' # str | vector_type__gte (optional)
vector_type__range = 'vector_type__range_example' # str | vector_type__range (optional)
active = 'active_example' # str | active (optional)
product = 'product_example' # str | product (optional)

try:
    api_instance.destroy_annotation_type(id, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_annotation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **vector_type** | **str**| vector_type | [optional] 
 **vector_type__lte** | **str**| vector_type__lte | [optional] 
 **vector_type__gte** | **str**| vector_type__gte | [optional] 
 **vector_type__range** | **str**| vector_type__range | [optional] 
 **active** | **str**| active | [optional] 
 **product** | **str**| product | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_annotation_version**
> destroy_annotation_version(id, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
version = 'version_example' # str | version (optional)
annotation = 'annotation_example' # str | annotation (optional)
image = 'image_example' # str | image (optional)
deleted = 'deleted_example' # str | deleted (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
has_changes = 'has_changes_example' # str | Has Changes (optional)

try:
    api_instance.destroy_annotation_version(id, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_annotation_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **version** | **str**| version | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **image** | **str**| image | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **has_changes** | **str**| Has Changes | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_log_image_action**
> destroy_log_image_action(id, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
ip = 'ip_example' # str | ip (optional)
ip__contains = 'ip__contains_example' # str | ip__contains (optional)
action = 'action_example' # str | action (optional)

try:
    api_instance.destroy_log_image_action(id, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_log_image_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **ip** | **str**| ip | [optional] 
 **ip__contains** | **str**| ip__contains | [optional] 
 **action** | **str**| action | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_verification**
> destroy_verification(id, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
annotation = 'annotation_example' # str | annotation (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_instance.destroy_verification(id, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)
except ApiException as e:
    print("Exception when calling AnnotationsApi->destroy_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_annotation_media_files**
> InlineResponse20012 list_annotation_media_files(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
annotation = 'annotation_example' # str | annotation (optional)
media_file_type = 'media_file_type_example' # str | media_file_type (optional)

try:
    api_response = api_instance.list_annotation_media_files(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_annotation_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **media_file_type** | **str**| media_file_type | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_annotation_types**
> InlineResponse20011 list_annotation_types(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)
vector_type__lte = 'vector_type__lte_example' # str | vector_type__lte (optional)
vector_type__gte = 'vector_type__gte_example' # str | vector_type__gte (optional)
vector_type__range = 'vector_type__range_example' # str | vector_type__range (optional)
active = 'active_example' # str | active (optional)
product = 'product_example' # str | product (optional)

try:
    api_response = api_instance.list_annotation_types(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_annotation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **vector_type** | **str**| vector_type | [optional] 
 **vector_type__lte** | **str**| vector_type__lte | [optional] 
 **vector_type__gte** | **str**| vector_type__gte | [optional] 
 **vector_type__range** | **str**| vector_type__range | [optional] 
 **active** | **str**| active | [optional] 
 **product** | **str**| product | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_annotation_versions**
> InlineResponse20010 list_annotation_versions(limit=limit, offset=offset, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
version = 'version_example' # str | version (optional)
annotation = 'annotation_example' # str | annotation (optional)
image = 'image_example' # str | image (optional)
deleted = 'deleted_example' # str | deleted (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
has_changes = 'has_changes_example' # str | Has Changes (optional)

try:
    api_response = api_instance.list_annotation_versions(limit=limit, offset=offset, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_annotation_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **version** | **str**| version | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **image** | **str**| image | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **has_changes** | **str**| Has Changes | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_annotations**
> InlineResponse2009 list_annotations(limit=limit, offset=offset, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
last_edit_time = 'last_edit_time_example' # str | last_edit_time (optional)
last_edit_time__lte = 'last_edit_time__lte_example' # str | last_edit_time__lte (optional)
last_edit_time__gte = 'last_edit_time__gte_example' # str | last_edit_time__gte (optional)
last_edit_time__range = 'last_edit_time__range_example' # str | last_edit_time__range (optional)
unique_identifier = 'unique_identifier_example' # str | unique_identifier (optional)
unique_identifier__contains = 'unique_identifier__contains_example' # str | unique_identifier__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
deleted = 'deleted_example' # str | deleted (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
verified_by = 'verified_by_example' # str | verified_by (optional)
verified_by__range = 'verified_by__range_example' # str | verified_by__range (optional)
annotationversion = 'annotationversion_example' # str | annotationversion (optional)
vector_x = 'vector_x_example' # str | Vector-X-Range (optional)
vector_y = 'vector_y_example' # str | Vector-Y-Range (optional)
meta_data__isnull = 'meta_data__isnull_example' # str | meta_data__isnull (optional)
vector__isnull = 'vector__isnull_example' # str | vector__isnull (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)

try:
    api_response = api_instance.list_annotations(limit=limit, offset=offset, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **last_edit_time** | **str**| last_edit_time | [optional] 
 **last_edit_time__lte** | **str**| last_edit_time__lte | [optional] 
 **last_edit_time__gte** | **str**| last_edit_time__gte | [optional] 
 **last_edit_time__range** | **str**| last_edit_time__range | [optional] 
 **unique_identifier** | **str**| unique_identifier | [optional] 
 **unique_identifier__contains** | **str**| unique_identifier__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **verified_by** | **str**| verified_by | [optional] 
 **verified_by__range** | **str**| verified_by__range | [optional] 
 **annotationversion** | **str**| annotationversion | [optional] 
 **vector_x** | **str**| Vector-X-Range | [optional] 
 **vector_y** | **str**| Vector-Y-Range | [optional] 
 **meta_data__isnull** | **str**| meta_data__isnull | [optional] 
 **vector__isnull** | **str**| vector__isnull | [optional] 
 **vector_type** | **str**| vector_type | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_log_image_actions**
> InlineResponse20014 list_log_image_actions(limit=limit, offset=offset, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
ip = 'ip_example' # str | ip (optional)
ip__contains = 'ip__contains_example' # str | ip__contains (optional)
action = 'action_example' # str | action (optional)

try:
    api_response = api_instance.list_log_image_actions(limit=limit, offset=offset, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_log_image_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **ip** | **str**| ip | [optional] 
 **ip__contains** | **str**| ip__contains | [optional] 
 **action** | **str**| action | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_verifications**
> InlineResponse20013 list_verifications(limit=limit, offset=offset, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
annotation = 'annotation_example' # str | annotation (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.list_verifications(limit=limit, offset=offset, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->list_verifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_annotation**
> Annotation partial_update_annotation(id, body=body, id2=id2, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.Annotation() # Annotation |  (optional)
id2 = 'id_example' # str | id (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
last_edit_time = 'last_edit_time_example' # str | last_edit_time (optional)
last_edit_time__lte = 'last_edit_time__lte_example' # str | last_edit_time__lte (optional)
last_edit_time__gte = 'last_edit_time__gte_example' # str | last_edit_time__gte (optional)
last_edit_time__range = 'last_edit_time__range_example' # str | last_edit_time__range (optional)
unique_identifier = 'unique_identifier_example' # str | unique_identifier (optional)
unique_identifier__contains = 'unique_identifier__contains_example' # str | unique_identifier__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
deleted = 'deleted_example' # str | deleted (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
verified_by = 'verified_by_example' # str | verified_by (optional)
verified_by__range = 'verified_by__range_example' # str | verified_by__range (optional)
annotationversion = 'annotationversion_example' # str | annotationversion (optional)
vector_x = 'vector_x_example' # str | Vector-X-Range (optional)
vector_y = 'vector_y_example' # str | Vector-Y-Range (optional)
meta_data__isnull = 'meta_data__isnull_example' # str | meta_data__isnull (optional)
vector__isnull = 'vector__isnull_example' # str | vector__isnull (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)

try:
    api_response = api_instance.partial_update_annotation(id, body=body, id2=id2, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Annotation**](Annotation.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **last_edit_time** | **str**| last_edit_time | [optional] 
 **last_edit_time__lte** | **str**| last_edit_time__lte | [optional] 
 **last_edit_time__gte** | **str**| last_edit_time__gte | [optional] 
 **last_edit_time__range** | **str**| last_edit_time__range | [optional] 
 **unique_identifier** | **str**| unique_identifier | [optional] 
 **unique_identifier__contains** | **str**| unique_identifier__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **verified_by** | **str**| verified_by | [optional] 
 **verified_by__range** | **str**| verified_by__range | [optional] 
 **annotationversion** | **str**| annotationversion | [optional] 
 **vector_x** | **str**| Vector-X-Range | [optional] 
 **vector_y** | **str**| Vector-Y-Range | [optional] 
 **meta_data__isnull** | **str**| meta_data__isnull | [optional] 
 **vector__isnull** | **str**| vector__isnull | [optional] 
 **vector_type** | **str**| vector_type | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_annotation_media_file**
> AnnotationMediaFile partial_update_annotation_media_file(id, body=body, id2=id2, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationMediaFile() # AnnotationMediaFile |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
annotation = 'annotation_example' # str | annotation (optional)
media_file_type = 'media_file_type_example' # str | media_file_type (optional)

try:
    api_response = api_instance.partial_update_annotation_media_file(id, body=body, id2=id2, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_annotation_media_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationMediaFile**](AnnotationMediaFile.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **media_file_type** | **str**| media_file_type | [optional] 

### Return type

[**AnnotationMediaFile**](AnnotationMediaFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_annotation_type**
> AnnotationType partial_update_annotation_type(id, body=body, id2=id2, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationType() # AnnotationType |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)
vector_type__lte = 'vector_type__lte_example' # str | vector_type__lte (optional)
vector_type__gte = 'vector_type__gte_example' # str | vector_type__gte (optional)
vector_type__range = 'vector_type__range_example' # str | vector_type__range (optional)
active = 'active_example' # str | active (optional)
product = 'product_example' # str | product (optional)

try:
    api_response = api_instance.partial_update_annotation_type(id, body=body, id2=id2, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_annotation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationType**](AnnotationType.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **vector_type** | **str**| vector_type | [optional] 
 **vector_type__lte** | **str**| vector_type__lte | [optional] 
 **vector_type__gte** | **str**| vector_type__gte | [optional] 
 **vector_type__range** | **str**| vector_type__range | [optional] 
 **active** | **str**| active | [optional] 
 **product** | **str**| product | [optional] 

### Return type

[**AnnotationType**](AnnotationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_annotation_version**
> AnnotationVersion partial_update_annotation_version(id, body=body, id2=id2, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationVersion() # AnnotationVersion |  (optional)
id2 = 'id_example' # str | id (optional)
version = 'version_example' # str | version (optional)
annotation = 'annotation_example' # str | annotation (optional)
image = 'image_example' # str | image (optional)
deleted = 'deleted_example' # str | deleted (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
has_changes = 'has_changes_example' # str | Has Changes (optional)

try:
    api_response = api_instance.partial_update_annotation_version(id, body=body, id2=id2, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_annotation_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationVersion**](AnnotationVersion.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **version** | **str**| version | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **image** | **str**| image | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **has_changes** | **str**| Has Changes | [optional] 

### Return type

[**AnnotationVersion**](AnnotationVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_log_image_action**
> LogImageAction partial_update_log_image_action(id, body=body, id2=id2, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.LogImageAction() # LogImageAction |  (optional)
id2 = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
ip = 'ip_example' # str | ip (optional)
ip__contains = 'ip__contains_example' # str | ip__contains (optional)
action = 'action_example' # str | action (optional)

try:
    api_response = api_instance.partial_update_log_image_action(id, body=body, id2=id2, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_log_image_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**LogImageAction**](LogImageAction.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **ip** | **str**| ip | [optional] 
 **ip__contains** | **str**| ip__contains | [optional] 
 **action** | **str**| action | [optional] 

### Return type

[**LogImageAction**](LogImageAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_verification**
> Verification partial_update_verification(id, body=body, id2=id2, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.Verification() # Verification |  (optional)
id2 = 'id_example' # str | id (optional)
annotation = 'annotation_example' # str | annotation (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.partial_update_verification(id, body=body, id2=id2, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->partial_update_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Verification**](Verification.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_annotation**
> Annotation retrieve_annotation(id, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
last_edit_time = 'last_edit_time_example' # str | last_edit_time (optional)
last_edit_time__lte = 'last_edit_time__lte_example' # str | last_edit_time__lte (optional)
last_edit_time__gte = 'last_edit_time__gte_example' # str | last_edit_time__gte (optional)
last_edit_time__range = 'last_edit_time__range_example' # str | last_edit_time__range (optional)
unique_identifier = 'unique_identifier_example' # str | unique_identifier (optional)
unique_identifier__contains = 'unique_identifier__contains_example' # str | unique_identifier__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
deleted = 'deleted_example' # str | deleted (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
verified_by = 'verified_by_example' # str | verified_by (optional)
verified_by__range = 'verified_by__range_example' # str | verified_by__range (optional)
annotationversion = 'annotationversion_example' # str | annotationversion (optional)
vector_x = 'vector_x_example' # str | Vector-X-Range (optional)
vector_y = 'vector_y_example' # str | Vector-Y-Range (optional)
meta_data__isnull = 'meta_data__isnull_example' # str | meta_data__isnull (optional)
vector__isnull = 'vector__isnull_example' # str | vector__isnull (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)

try:
    api_response = api_instance.retrieve_annotation(id, id=id, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **last_edit_time** | **str**| last_edit_time | [optional] 
 **last_edit_time__lte** | **str**| last_edit_time__lte | [optional] 
 **last_edit_time__gte** | **str**| last_edit_time__gte | [optional] 
 **last_edit_time__range** | **str**| last_edit_time__range | [optional] 
 **unique_identifier** | **str**| unique_identifier | [optional] 
 **unique_identifier__contains** | **str**| unique_identifier__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **verified_by** | **str**| verified_by | [optional] 
 **verified_by__range** | **str**| verified_by__range | [optional] 
 **annotationversion** | **str**| annotationversion | [optional] 
 **vector_x** | **str**| Vector-X-Range | [optional] 
 **vector_y** | **str**| Vector-Y-Range | [optional] 
 **meta_data__isnull** | **str**| meta_data__isnull | [optional] 
 **vector__isnull** | **str**| vector__isnull | [optional] 
 **vector_type** | **str**| vector_type | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_annotation_media_file**
> AnnotationMediaFile retrieve_annotation_media_file(id, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
annotation = 'annotation_example' # str | annotation (optional)
media_file_type = 'media_file_type_example' # str | media_file_type (optional)

try:
    api_response = api_instance.retrieve_annotation_media_file(id, id=id, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_annotation_media_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **media_file_type** | **str**| media_file_type | [optional] 

### Return type

[**AnnotationMediaFile**](AnnotationMediaFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_annotation_type**
> AnnotationType retrieve_annotation_type(id, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)
vector_type__lte = 'vector_type__lte_example' # str | vector_type__lte (optional)
vector_type__gte = 'vector_type__gte_example' # str | vector_type__gte (optional)
vector_type__range = 'vector_type__range_example' # str | vector_type__range (optional)
active = 'active_example' # str | active (optional)
product = 'product_example' # str | product (optional)

try:
    api_response = api_instance.retrieve_annotation_type(id, id=id, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_annotation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **vector_type** | **str**| vector_type | [optional] 
 **vector_type__lte** | **str**| vector_type__lte | [optional] 
 **vector_type__gte** | **str**| vector_type__gte | [optional] 
 **vector_type__range** | **str**| vector_type__range | [optional] 
 **active** | **str**| active | [optional] 
 **product** | **str**| product | [optional] 

### Return type

[**AnnotationType**](AnnotationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_annotation_version**
> AnnotationVersion retrieve_annotation_version(id, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
version = 'version_example' # str | version (optional)
annotation = 'annotation_example' # str | annotation (optional)
image = 'image_example' # str | image (optional)
deleted = 'deleted_example' # str | deleted (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
has_changes = 'has_changes_example' # str | Has Changes (optional)

try:
    api_response = api_instance.retrieve_annotation_version(id, id=id, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_annotation_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **version** | **str**| version | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **image** | **str**| image | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **has_changes** | **str**| Has Changes | [optional] 

### Return type

[**AnnotationVersion**](AnnotationVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_log_image_action**
> LogImageAction retrieve_log_image_action(id, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
ip = 'ip_example' # str | ip (optional)
ip__contains = 'ip__contains_example' # str | ip__contains (optional)
action = 'action_example' # str | action (optional)

try:
    api_response = api_instance.retrieve_log_image_action(id, id=id, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_log_image_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **ip** | **str**| ip | [optional] 
 **ip__contains** | **str**| ip__contains | [optional] 
 **action** | **str**| action | [optional] 

### Return type

[**LogImageAction**](LogImageAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_verification**
> Verification retrieve_verification(id, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
annotation = 'annotation_example' # str | annotation (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.retrieve_verification(id, id=id, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->retrieve_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> Annotation update_annotation(id, body=body, id2=id2, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.Annotation() # Annotation |  (optional)
id2 = 'id_example' # str | id (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
last_edit_time = 'last_edit_time_example' # str | last_edit_time (optional)
last_edit_time__lte = 'last_edit_time__lte_example' # str | last_edit_time__lte (optional)
last_edit_time__gte = 'last_edit_time__gte_example' # str | last_edit_time__gte (optional)
last_edit_time__range = 'last_edit_time__range_example' # str | last_edit_time__range (optional)
unique_identifier = 'unique_identifier_example' # str | unique_identifier (optional)
unique_identifier__contains = 'unique_identifier__contains_example' # str | unique_identifier__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
deleted = 'deleted_example' # str | deleted (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
verified_by = 'verified_by_example' # str | verified_by (optional)
verified_by__range = 'verified_by__range_example' # str | verified_by__range (optional)
annotationversion = 'annotationversion_example' # str | annotationversion (optional)
vector_x = 'vector_x_example' # str | Vector-X-Range (optional)
vector_y = 'vector_y_example' # str | Vector-Y-Range (optional)
meta_data__isnull = 'meta_data__isnull_example' # str | meta_data__isnull (optional)
vector__isnull = 'vector__isnull_example' # str | vector__isnull (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)

try:
    api_response = api_instance.update_annotation(id, body=body, id2=id2, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, last_edit_time=last_edit_time, last_edit_time__lte=last_edit_time__lte, last_edit_time__gte=last_edit_time__gte, last_edit_time__range=last_edit_time__range, unique_identifier=unique_identifier, unique_identifier__contains=unique_identifier__contains, description=description, description__contains=description__contains, deleted=deleted, image=image, user=user, annotation_type=annotation_type, verified_by=verified_by, verified_by__range=verified_by__range, annotationversion=annotationversion, vector_x=vector_x, vector_y=vector_y, meta_data__isnull=meta_data__isnull, vector__isnull=vector__isnull, vector_type=vector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Annotation**](Annotation.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **last_edit_time** | **str**| last_edit_time | [optional] 
 **last_edit_time__lte** | **str**| last_edit_time__lte | [optional] 
 **last_edit_time__gte** | **str**| last_edit_time__gte | [optional] 
 **last_edit_time__range** | **str**| last_edit_time__range | [optional] 
 **unique_identifier** | **str**| unique_identifier | [optional] 
 **unique_identifier__contains** | **str**| unique_identifier__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **verified_by** | **str**| verified_by | [optional] 
 **verified_by__range** | **str**| verified_by__range | [optional] 
 **annotationversion** | **str**| annotationversion | [optional] 
 **vector_x** | **str**| Vector-X-Range | [optional] 
 **vector_y** | **str**| Vector-Y-Range | [optional] 
 **meta_data__isnull** | **str**| meta_data__isnull | [optional] 
 **vector__isnull** | **str**| vector__isnull | [optional] 
 **vector_type** | **str**| vector_type | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation_media_file**
> AnnotationMediaFile update_annotation_media_file(id, body=body, id2=id2, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationMediaFile() # AnnotationMediaFile |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
annotation = 'annotation_example' # str | annotation (optional)
media_file_type = 'media_file_type_example' # str | media_file_type (optional)

try:
    api_response = api_instance.update_annotation_media_file(id, body=body, id2=id2, name=name, name__contains=name__contains, annotation=annotation, media_file_type=media_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation_media_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationMediaFile**](AnnotationMediaFile.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **media_file_type** | **str**| media_file_type | [optional] 

### Return type

[**AnnotationMediaFile**](AnnotationMediaFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation_type**
> AnnotationType update_annotation_type(id, body=body, id2=id2, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationType() # AnnotationType |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
vector_type = 'vector_type_example' # str | vector_type (optional)
vector_type__lte = 'vector_type__lte_example' # str | vector_type__lte (optional)
vector_type__gte = 'vector_type__gte_example' # str | vector_type__gte (optional)
vector_type__range = 'vector_type__range_example' # str | vector_type__range (optional)
active = 'active_example' # str | active (optional)
product = 'product_example' # str | product (optional)

try:
    api_response = api_instance.update_annotation_type(id, body=body, id2=id2, name=name, name__contains=name__contains, vector_type=vector_type, vector_type__lte=vector_type__lte, vector_type__gte=vector_type__gte, vector_type__range=vector_type__range, active=active, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationType**](AnnotationType.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **vector_type** | **str**| vector_type | [optional] 
 **vector_type__lte** | **str**| vector_type__lte | [optional] 
 **vector_type__gte** | **str**| vector_type__gte | [optional] 
 **vector_type__range** | **str**| vector_type__range | [optional] 
 **active** | **str**| active | [optional] 
 **product** | **str**| product | [optional] 

### Return type

[**AnnotationType**](AnnotationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation_version**
> AnnotationVersion update_annotation_version(id, body=body, id2=id2, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.AnnotationVersion() # AnnotationVersion |  (optional)
id2 = 'id_example' # str | id (optional)
version = 'version_example' # str | version (optional)
annotation = 'annotation_example' # str | annotation (optional)
image = 'image_example' # str | image (optional)
deleted = 'deleted_example' # str | deleted (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
has_changes = 'has_changes_example' # str | Has Changes (optional)

try:
    api_response = api_instance.update_annotation_version(id, body=body, id2=id2, version=version, annotation=annotation, image=image, deleted=deleted, annotation_type=annotation_type, has_changes=has_changes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AnnotationVersion**](AnnotationVersion.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **version** | **str**| version | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **image** | **str**| image | [optional] 
 **deleted** | **str**| deleted | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **has_changes** | **str**| Has Changes | [optional] 

### Return type

[**AnnotationVersion**](AnnotationVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_image_action**
> LogImageAction update_log_image_action(id, body=body, id2=id2, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.LogImageAction() # LogImageAction |  (optional)
id2 = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
ip = 'ip_example' # str | ip (optional)
ip__contains = 'ip__contains_example' # str | ip__contains (optional)
action = 'action_example' # str | action (optional)

try:
    api_response = api_instance.update_log_image_action(id, body=body, id2=id2, image=image, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, ip=ip, ip__contains=ip__contains, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_log_image_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**LogImageAction**](LogImageAction.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **ip** | **str**| ip | [optional] 
 **ip__contains** | **str**| ip__contains | [optional] 
 **action** | **str**| action | [optional] 

### Return type

[**LogImageAction**](LogImageAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_verification**
> Verification update_verification(id, body=body, id2=id2, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnnotationsApi()
id = 'id_example' # str | 
body = swagger_client.Verification() # Verification |  (optional)
id2 = 'id_example' # str | id (optional)
annotation = 'annotation_example' # str | annotation (optional)
user = 'user_example' # str | user (optional)
time = 'time_example' # str | time (optional)
time__lte = 'time__lte_example' # str | time__lte (optional)
time__gte = 'time__gte_example' # str | time__gte (optional)
time__range = 'time__range_example' # str | time__range (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.update_verification(id, body=body, id2=id2, annotation=annotation, user=user, time=time, time__lte=time__lte, time__gte=time__gte, time__range=time__range, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Verification**](Verification.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **annotation** | **str**| annotation | [optional] 
 **user** | **str**| user | [optional] 
 **time** | **str**| time | [optional] 
 **time__lte** | **str**| time__lte | [optional] 
 **time__gte** | **str**| time__gte | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

