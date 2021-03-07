# swagger_client.ImagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_set_version**](ImagesApi.md#add_set_version) | **POST** /api/v1/images/set_versions/{id}/add/ | 
[**create_image**](ImagesApi.md#create_image) | **POST** /api/v1/images/images/ | 
[**create_image_registration**](ImagesApi.md#create_image_registration) | **POST** /api/v1/images/registration/ | 
[**create_image_set**](ImagesApi.md#create_image_set) | **POST** /api/v1/images/image_sets/ | 
[**create_screening_mode**](ImagesApi.md#create_screening_mode) | **POST** /api/v1/images/screening_modes/ | 
[**create_set_tag**](ImagesApi.md#create_set_tag) | **POST** /api/v1/images/set_tags/ | 
[**create_set_version**](ImagesApi.md#create_set_version) | **POST** /api/v1/images/set_versions/ | 
[**destroy_image**](ImagesApi.md#destroy_image) | **DELETE** /api/v1/images/images/{id}/ | 
[**destroy_image_registration**](ImagesApi.md#destroy_image_registration) | **DELETE** /api/v1/images/registration/{id}/ | 
[**destroy_image_set**](ImagesApi.md#destroy_image_set) | **DELETE** /api/v1/images/image_sets/{id}/ | 
[**destroy_screening_mode**](ImagesApi.md#destroy_screening_mode) | **DELETE** /api/v1/images/screening_modes/{id}/ | 
[**destroy_set_tag**](ImagesApi.md#destroy_set_tag) | **DELETE** /api/v1/images/set_tags/{id}/ | 
[**destroy_set_version**](ImagesApi.md#destroy_set_version) | **DELETE** /api/v1/images/set_versions/{id}/ | 
[**get_patch_image**](ImagesApi.md#get_patch_image) | **GET** /api/v1/images/images/{id}/get_patch/ | 
[**list_image_registrations**](ImagesApi.md#list_image_registrations) | **GET** /api/v1/images/registration/ | 
[**list_image_sets**](ImagesApi.md#list_image_sets) | **GET** /api/v1/images/image_sets/ | 
[**list_images**](ImagesApi.md#list_images) | **GET** /api/v1/images/images/ | 
[**list_screening_modes**](ImagesApi.md#list_screening_modes) | **GET** /api/v1/images/screening_modes/ | 
[**list_set_tags**](ImagesApi.md#list_set_tags) | **GET** /api/v1/images/set_tags/ | 
[**list_set_versions**](ImagesApi.md#list_set_versions) | **GET** /api/v1/images/set_versions/ | 
[**partial_update_image**](ImagesApi.md#partial_update_image) | **PATCH** /api/v1/images/images/{id}/ | 
[**partial_update_image_registration**](ImagesApi.md#partial_update_image_registration) | **PATCH** /api/v1/images/registration/{id}/ | 
[**partial_update_image_set**](ImagesApi.md#partial_update_image_set) | **PATCH** /api/v1/images/image_sets/{id}/ | 
[**partial_update_screening_mode**](ImagesApi.md#partial_update_screening_mode) | **PATCH** /api/v1/images/screening_modes/{id}/ | 
[**partial_update_set_tag**](ImagesApi.md#partial_update_set_tag) | **PATCH** /api/v1/images/set_tags/{id}/ | 
[**partial_update_set_version**](ImagesApi.md#partial_update_set_version) | **PATCH** /api/v1/images/set_versions/{id}/ | 
[**register_images_image**](ImagesApi.md#register_images_image) | **POST** /api/v1/images/images/{id}/register_images/ | 
[**retrieve_image**](ImagesApi.md#retrieve_image) | **GET** /api/v1/images/images/{id}/ | 
[**retrieve_image_registration**](ImagesApi.md#retrieve_image_registration) | **GET** /api/v1/images/registration/{id}/ | 
[**retrieve_image_set**](ImagesApi.md#retrieve_image_set) | **GET** /api/v1/images/image_sets/{id}/ | 
[**retrieve_screening_mode**](ImagesApi.md#retrieve_screening_mode) | **GET** /api/v1/images/screening_modes/{id}/ | 
[**retrieve_set_tag**](ImagesApi.md#retrieve_set_tag) | **GET** /api/v1/images/set_tags/{id}/ | 
[**retrieve_set_version**](ImagesApi.md#retrieve_set_version) | **GET** /api/v1/images/set_versions/{id}/ | 
[**slide_information_image**](ImagesApi.md#slide_information_image) | **GET** /api/v1/images/images/{id}/slide_information/ | 
[**thumbnail_image**](ImagesApi.md#thumbnail_image) | **GET** /api/v1/images/images/{id}/thumbnail/ | 
[**update_image**](ImagesApi.md#update_image) | **PUT** /api/v1/images/images/{id}/ | 
[**update_image_registration**](ImagesApi.md#update_image_registration) | **PUT** /api/v1/images/registration/{id}/ | 
[**update_image_set**](ImagesApi.md#update_image_set) | **PUT** /api/v1/images/image_sets/{id}/ | 
[**update_screening_mode**](ImagesApi.md#update_screening_mode) | **PUT** /api/v1/images/screening_modes/{id}/ | 
[**update_set_tag**](ImagesApi.md#update_set_tag) | **PUT** /api/v1/images/set_tags/{id}/ | 
[**update_set_version**](ImagesApi.md#update_set_version) | **PUT** /api/v1/images/set_versions/{id}/ | 

# **add_set_version**
> SetVersion add_set_version(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.SetVersion() # SetVersion |  (optional)

try:
    api_response = api_instance.add_set_version(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->add_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SetVersion**](SetVersion.md)|  | [optional] 

### Return type

[**SetVersion**](SetVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image**
> Image create_image(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.Image() # Image |  (optional)

try:
    api_response = api_instance.create_image(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_registration**
> ImageRegistration create_image_registration(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.ImageRegistration() # ImageRegistration |  (optional)

try:
    api_response = api_instance.create_image_registration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_image_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageRegistration**](ImageRegistration.md)|  | [optional] 

### Return type

[**ImageRegistration**](ImageRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_set**
> ImageSet create_image_set(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.ImageSet() # ImageSet |  (optional)

try:
    api_response = api_instance.create_image_set(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_image_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageSet**](ImageSet.md)|  | [optional] 

### Return type

[**ImageSet**](ImageSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_screening_mode**
> ScreeningMode create_screening_mode(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.ScreeningMode() # ScreeningMode |  (optional)

try:
    api_response = api_instance.create_screening_mode(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_screening_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScreeningMode**](ScreeningMode.md)|  | [optional] 

### Return type

[**ScreeningMode**](ScreeningMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_set_tag**
> SetTag create_set_tag(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.SetTag() # SetTag |  (optional)

try:
    api_response = api_instance.create_set_tag(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetTag**](SetTag.md)|  | [optional] 

### Return type

[**SetTag**](SetTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_set_version**
> SetVersion create_set_version(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
body = swagger_client.SetVersion() # SetVersion |  (optional)

try:
    api_response = api_instance.create_set_version(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetVersion**](SetVersion.md)|  | [optional] 

### Return type

[**SetVersion**](SetVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_image**
> destroy_image(id, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
filename = 'filename_example' # str | filename (optional)
filename__contains = 'filename__contains_example' # str | filename__contains (optional)
time = 'time_example' # str | time (optional)
time__contains = 'time__contains_example' # str | time__contains (optional)
mpp = 'mpp_example' # str | mpp (optional)
mpp__range = 'mpp__range_example' # str | mpp__range (optional)
objective_power = 'objective_power_example' # str | objectivePower (optional)
objective_power__range = 'objective_power__range_example' # str | objectivePower__range (optional)
width = 'width_example' # str | width (optional)
width__range = 'width__range_example' # str | width__range (optional)
height = 'height_example' # str | height (optional)
height__range = 'height__range_example' # str | height__range (optional)
image_set = 'image_set_example' # str | image_set (optional)
image_type = 'image_type_example' # str | image_type (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
num_annotations = 'num_annotations_example' # str | num_annotations (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_instance.destroy_image(id, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **filename** | **str**| filename | [optional] 
 **filename__contains** | **str**| filename__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__contains** | **str**| time__contains | [optional] 
 **mpp** | **str**| mpp | [optional] 
 **mpp__range** | **str**| mpp__range | [optional] 
 **objective_power** | **str**| objectivePower | [optional] 
 **objective_power__range** | **str**| objectivePower__range | [optional] 
 **width** | **str**| width | [optional] 
 **width__range** | **str**| width__range | [optional] 
 **height** | **str**| height | [optional] 
 **height__range** | **str**| height__range | [optional] 
 **image_set** | **str**| image_set | [optional] 
 **image_type** | **str**| image_type | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **num_annotations** | **str**| num_annotations | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_image_registration**
> destroy_image_registration(id, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
target_image = 'target_image_example' # str | target_image (optional)
source_image = 'source_image_example' # str | source_image (optional)
registration_error__range = 'registration_error__range_example' # str | registration_error__range (optional)
runtime__range = 'runtime__range_example' # str | runtime__range (optional)

try:
    api_instance.destroy_image_registration(id, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_image_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **target_image** | **str**| target_image | [optional] 
 **source_image** | **str**| source_image | [optional] 
 **registration_error__range** | **str**| registration_error__range | [optional] 
 **runtime__range** | **str**| runtime__range | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_image_set**
> destroy_image_set(id, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
path = 'path_example' # str | path (optional)
path__contains = 'path__contains_example' # str | path__contains (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
location = 'location_example' # str | location (optional)
location__contains = 'location__contains_example' # str | location__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
time = 'time_example' # str | time (optional)
time__range = 'time__range_example' # str | time__range (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
public = 'public_example' # str | public (optional)
main_annotation_type = 'main_annotation_type_example' # str | main_annotation_type (optional)
set_tags = 'set_tags_example' # str | set_tags (optional)
set_versions = 'set_versions_example' # str | set_versions (optional)
product = 'product_example' # str | product (optional)
collaboration_type = 'collaboration_type_example' # str | collaboration_type (optional)
priority = 'priority_example' # str | priority (optional)
zip_state = 'zip_state_example' # str | zip_state (optional)
images = 'images_example' # str | images (optional)

try:
    api_instance.destroy_image_set(id, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_image_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **path** | **str**| path | [optional] 
 **path__contains** | **str**| path__contains | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **location** | **str**| location | [optional] 
 **location__contains** | **str**| location__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **public** | **str**| public | [optional] 
 **main_annotation_type** | **str**| main_annotation_type | [optional] 
 **set_tags** | **str**| set_tags | [optional] 
 **set_versions** | **str**| set_versions | [optional] 
 **product** | **str**| product | [optional] 
 **collaboration_type** | **str**| collaboration_type | [optional] 
 **priority** | **str**| priority | [optional] 
 **zip_state** | **str**| zip_state | [optional] 
 **images** | **str**| images | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_screening_mode**
> destroy_screening_mode(id, id=id, image=image, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)

try:
    api_instance.destroy_screening_mode(id, id=id, image=image, user=user)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_screening_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_set_tag**
> destroy_set_tag(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_instance.destroy_set_tag(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_set_version**
> destroy_set_version(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_instance.destroy_set_version(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
except ApiException as e:
    print("Exception when calling ImagesApi->destroy_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patch_image**
> Image get_patch_image(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_patch_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_patch_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_registrations**
> InlineResponse2008 list_image_registrations(limit=limit, offset=offset, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
target_image = 'target_image_example' # str | target_image (optional)
source_image = 'source_image_example' # str | source_image (optional)
registration_error__range = 'registration_error__range_example' # str | registration_error__range (optional)
runtime__range = 'runtime__range_example' # str | runtime__range (optional)

try:
    api_response = api_instance.list_image_registrations(limit=limit, offset=offset, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_image_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **target_image** | **str**| target_image | [optional] 
 **source_image** | **str**| source_image | [optional] 
 **registration_error__range** | **str**| registration_error__range | [optional] 
 **runtime__range** | **str**| runtime__range | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_sets**
> InlineResponse2004 list_image_sets(limit=limit, offset=offset, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
path = 'path_example' # str | path (optional)
path__contains = 'path__contains_example' # str | path__contains (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
location = 'location_example' # str | location (optional)
location__contains = 'location__contains_example' # str | location__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
time = 'time_example' # str | time (optional)
time__range = 'time__range_example' # str | time__range (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
public = 'public_example' # str | public (optional)
main_annotation_type = 'main_annotation_type_example' # str | main_annotation_type (optional)
set_tags = 'set_tags_example' # str | set_tags (optional)
set_versions = 'set_versions_example' # str | set_versions (optional)
product = 'product_example' # str | product (optional)
collaboration_type = 'collaboration_type_example' # str | collaboration_type (optional)
priority = 'priority_example' # str | priority (optional)
zip_state = 'zip_state_example' # str | zip_state (optional)
images = 'images_example' # str | images (optional)

try:
    api_response = api_instance.list_image_sets(limit=limit, offset=offset, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_image_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **path** | **str**| path | [optional] 
 **path__contains** | **str**| path__contains | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **location** | **str**| location | [optional] 
 **location__contains** | **str**| location__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **public** | **str**| public | [optional] 
 **main_annotation_type** | **str**| main_annotation_type | [optional] 
 **set_tags** | **str**| set_tags | [optional] 
 **set_versions** | **str**| set_versions | [optional] 
 **product** | **str**| product | [optional] 
 **collaboration_type** | **str**| collaboration_type | [optional] 
 **priority** | **str**| priority | [optional] 
 **zip_state** | **str**| zip_state | [optional] 
 **images** | **str**| images | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_images**
> InlineResponse2003 list_images(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
filename = 'filename_example' # str | filename (optional)
filename__contains = 'filename__contains_example' # str | filename__contains (optional)
time = 'time_example' # str | time (optional)
time__contains = 'time__contains_example' # str | time__contains (optional)
mpp = 'mpp_example' # str | mpp (optional)
mpp__range = 'mpp__range_example' # str | mpp__range (optional)
objective_power = 'objective_power_example' # str | objectivePower (optional)
objective_power__range = 'objective_power__range_example' # str | objectivePower__range (optional)
width = 'width_example' # str | width (optional)
width__range = 'width__range_example' # str | width__range (optional)
height = 'height_example' # str | height (optional)
height__range = 'height__range_example' # str | height__range (optional)
image_set = 'image_set_example' # str | image_set (optional)
image_type = 'image_type_example' # str | image_type (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
num_annotations = 'num_annotations_example' # str | num_annotations (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.list_images(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **filename** | **str**| filename | [optional] 
 **filename__contains** | **str**| filename__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__contains** | **str**| time__contains | [optional] 
 **mpp** | **str**| mpp | [optional] 
 **mpp__range** | **str**| mpp__range | [optional] 
 **objective_power** | **str**| objectivePower | [optional] 
 **objective_power__range** | **str**| objectivePower__range | [optional] 
 **width** | **str**| width | [optional] 
 **width__range** | **str**| width__range | [optional] 
 **height** | **str**| height | [optional] 
 **height__range** | **str**| height__range | [optional] 
 **image_set** | **str**| image_set | [optional] 
 **image_type** | **str**| image_type | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **num_annotations** | **str**| num_annotations | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_screening_modes**
> InlineResponse2007 list_screening_modes(limit=limit, offset=offset, id=id, image=image, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.list_screening_modes(limit=limit, offset=offset, id=id, image=image, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_screening_modes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_set_tags**
> InlineResponse2005 list_set_tags(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.list_set_tags(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_set_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_set_versions**
> InlineResponse2006 list_set_versions(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.list_set_versions(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_set_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_image**
> Image partial_update_image(id, body=body, id2=id2, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.Image() # Image |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
filename = 'filename_example' # str | filename (optional)
filename__contains = 'filename__contains_example' # str | filename__contains (optional)
time = 'time_example' # str | time (optional)
time__contains = 'time__contains_example' # str | time__contains (optional)
mpp = 'mpp_example' # str | mpp (optional)
mpp__range = 'mpp__range_example' # str | mpp__range (optional)
objective_power = 'objective_power_example' # str | objectivePower (optional)
objective_power__range = 'objective_power__range_example' # str | objectivePower__range (optional)
width = 'width_example' # str | width (optional)
width__range = 'width__range_example' # str | width__range (optional)
height = 'height_example' # str | height (optional)
height__range = 'height__range_example' # str | height__range (optional)
image_set = 'image_set_example' # str | image_set (optional)
image_type = 'image_type_example' # str | image_type (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
num_annotations = 'num_annotations_example' # str | num_annotations (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.partial_update_image(id, body=body, id2=id2, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Image**](Image.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **filename** | **str**| filename | [optional] 
 **filename__contains** | **str**| filename__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__contains** | **str**| time__contains | [optional] 
 **mpp** | **str**| mpp | [optional] 
 **mpp__range** | **str**| mpp__range | [optional] 
 **objective_power** | **str**| objectivePower | [optional] 
 **objective_power__range** | **str**| objectivePower__range | [optional] 
 **width** | **str**| width | [optional] 
 **width__range** | **str**| width__range | [optional] 
 **height** | **str**| height | [optional] 
 **height__range** | **str**| height__range | [optional] 
 **image_set** | **str**| image_set | [optional] 
 **image_type** | **str**| image_type | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **num_annotations** | **str**| num_annotations | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_image_registration**
> ImageRegistration partial_update_image_registration(id, body=body, id2=id2, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ImageRegistration() # ImageRegistration |  (optional)
id2 = 'id_example' # str | id (optional)
target_image = 'target_image_example' # str | target_image (optional)
source_image = 'source_image_example' # str | source_image (optional)
registration_error__range = 'registration_error__range_example' # str | registration_error__range (optional)
runtime__range = 'runtime__range_example' # str | runtime__range (optional)

try:
    api_response = api_instance.partial_update_image_registration(id, body=body, id2=id2, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_image_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ImageRegistration**](ImageRegistration.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **target_image** | **str**| target_image | [optional] 
 **source_image** | **str**| source_image | [optional] 
 **registration_error__range** | **str**| registration_error__range | [optional] 
 **runtime__range** | **str**| runtime__range | [optional] 

### Return type

[**ImageRegistration**](ImageRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_image_set**
> ImageSet partial_update_image_set(id, body=body, id2=id2, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ImageSet() # ImageSet |  (optional)
id2 = 'id_example' # str | id (optional)
path = 'path_example' # str | path (optional)
path__contains = 'path__contains_example' # str | path__contains (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
location = 'location_example' # str | location (optional)
location__contains = 'location__contains_example' # str | location__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
time = 'time_example' # str | time (optional)
time__range = 'time__range_example' # str | time__range (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
public = 'public_example' # str | public (optional)
main_annotation_type = 'main_annotation_type_example' # str | main_annotation_type (optional)
set_tags = 'set_tags_example' # str | set_tags (optional)
set_versions = 'set_versions_example' # str | set_versions (optional)
product = 'product_example' # str | product (optional)
collaboration_type = 'collaboration_type_example' # str | collaboration_type (optional)
priority = 'priority_example' # str | priority (optional)
zip_state = 'zip_state_example' # str | zip_state (optional)
images = 'images_example' # str | images (optional)

try:
    api_response = api_instance.partial_update_image_set(id, body=body, id2=id2, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_image_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ImageSet**](ImageSet.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **path** | **str**| path | [optional] 
 **path__contains** | **str**| path__contains | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **location** | **str**| location | [optional] 
 **location__contains** | **str**| location__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **public** | **str**| public | [optional] 
 **main_annotation_type** | **str**| main_annotation_type | [optional] 
 **set_tags** | **str**| set_tags | [optional] 
 **set_versions** | **str**| set_versions | [optional] 
 **product** | **str**| product | [optional] 
 **collaboration_type** | **str**| collaboration_type | [optional] 
 **priority** | **str**| priority | [optional] 
 **zip_state** | **str**| zip_state | [optional] 
 **images** | **str**| images | [optional] 

### Return type

[**ImageSet**](ImageSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_screening_mode**
> ScreeningMode partial_update_screening_mode(id, body=body, id2=id2, image=image, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ScreeningMode() # ScreeningMode |  (optional)
id2 = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.partial_update_screening_mode(id, body=body, id2=id2, image=image, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_screening_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ScreeningMode**](ScreeningMode.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**ScreeningMode**](ScreeningMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_set_tag**
> SetTag partial_update_set_tag(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.SetTag() # SetTag |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.partial_update_set_tag(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SetTag**](SetTag.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetTag**](SetTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_set_version**
> SetVersion partial_update_set_version(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.SetVersion() # SetVersion |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.partial_update_set_version(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->partial_update_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SetVersion**](SetVersion.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetVersion**](SetVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_images_image**
> Image register_images_image(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.Image() # Image |  (optional)

try:
    api_response = api_instance.register_images_image(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->register_images_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image**
> Image retrieve_image(id, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
filename = 'filename_example' # str | filename (optional)
filename__contains = 'filename__contains_example' # str | filename__contains (optional)
time = 'time_example' # str | time (optional)
time__contains = 'time__contains_example' # str | time__contains (optional)
mpp = 'mpp_example' # str | mpp (optional)
mpp__range = 'mpp__range_example' # str | mpp__range (optional)
objective_power = 'objective_power_example' # str | objectivePower (optional)
objective_power__range = 'objective_power__range_example' # str | objectivePower__range (optional)
width = 'width_example' # str | width (optional)
width__range = 'width__range_example' # str | width__range (optional)
height = 'height_example' # str | height (optional)
height__range = 'height__range_example' # str | height__range (optional)
image_set = 'image_set_example' # str | image_set (optional)
image_type = 'image_type_example' # str | image_type (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
num_annotations = 'num_annotations_example' # str | num_annotations (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.retrieve_image(id, id=id, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **filename** | **str**| filename | [optional] 
 **filename__contains** | **str**| filename__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__contains** | **str**| time__contains | [optional] 
 **mpp** | **str**| mpp | [optional] 
 **mpp__range** | **str**| mpp__range | [optional] 
 **objective_power** | **str**| objectivePower | [optional] 
 **objective_power__range** | **str**| objectivePower__range | [optional] 
 **width** | **str**| width | [optional] 
 **width__range** | **str**| width__range | [optional] 
 **height** | **str**| height | [optional] 
 **height__range** | **str**| height__range | [optional] 
 **image_set** | **str**| image_set | [optional] 
 **image_type** | **str**| image_type | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **num_annotations** | **str**| num_annotations | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image_registration**
> ImageRegistration retrieve_image_registration(id, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
target_image = 'target_image_example' # str | target_image (optional)
source_image = 'source_image_example' # str | source_image (optional)
registration_error__range = 'registration_error__range_example' # str | registration_error__range (optional)
runtime__range = 'runtime__range_example' # str | runtime__range (optional)

try:
    api_response = api_instance.retrieve_image_registration(id, id=id, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **target_image** | **str**| target_image | [optional] 
 **source_image** | **str**| source_image | [optional] 
 **registration_error__range** | **str**| registration_error__range | [optional] 
 **runtime__range** | **str**| runtime__range | [optional] 

### Return type

[**ImageRegistration**](ImageRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image_set**
> ImageSet retrieve_image_set(id, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
path = 'path_example' # str | path (optional)
path__contains = 'path__contains_example' # str | path__contains (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
location = 'location_example' # str | location (optional)
location__contains = 'location__contains_example' # str | location__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
time = 'time_example' # str | time (optional)
time__range = 'time__range_example' # str | time__range (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
public = 'public_example' # str | public (optional)
main_annotation_type = 'main_annotation_type_example' # str | main_annotation_type (optional)
set_tags = 'set_tags_example' # str | set_tags (optional)
set_versions = 'set_versions_example' # str | set_versions (optional)
product = 'product_example' # str | product (optional)
collaboration_type = 'collaboration_type_example' # str | collaboration_type (optional)
priority = 'priority_example' # str | priority (optional)
zip_state = 'zip_state_example' # str | zip_state (optional)
images = 'images_example' # str | images (optional)

try:
    api_response = api_instance.retrieve_image_set(id, id=id, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **path** | **str**| path | [optional] 
 **path__contains** | **str**| path__contains | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **location** | **str**| location | [optional] 
 **location__contains** | **str**| location__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **public** | **str**| public | [optional] 
 **main_annotation_type** | **str**| main_annotation_type | [optional] 
 **set_tags** | **str**| set_tags | [optional] 
 **set_versions** | **str**| set_versions | [optional] 
 **product** | **str**| product | [optional] 
 **collaboration_type** | **str**| collaboration_type | [optional] 
 **priority** | **str**| priority | [optional] 
 **zip_state** | **str**| zip_state | [optional] 
 **images** | **str**| images | [optional] 

### Return type

[**ImageSet**](ImageSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_screening_mode**
> ScreeningMode retrieve_screening_mode(id, id=id, image=image, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.retrieve_screening_mode(id, id=id, image=image, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_screening_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**ScreeningMode**](ScreeningMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_set_tag**
> SetTag retrieve_set_tag(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.retrieve_set_tag(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetTag**](SetTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_set_version**
> SetVersion retrieve_set_version(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.retrieve_set_version(id, id=id, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetVersion**](SetVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slide_information_image**
> Image slide_information_image(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.slide_information_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->slide_information_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thumbnail_image**
> Image thumbnail_image(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.thumbnail_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->thumbnail_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> Image update_image(id, body=body, id2=id2, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.Image() # Image |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
filename = 'filename_example' # str | filename (optional)
filename__contains = 'filename__contains_example' # str | filename__contains (optional)
time = 'time_example' # str | time (optional)
time__contains = 'time__contains_example' # str | time__contains (optional)
mpp = 'mpp_example' # str | mpp (optional)
mpp__range = 'mpp__range_example' # str | mpp__range (optional)
objective_power = 'objective_power_example' # str | objectivePower (optional)
objective_power__range = 'objective_power__range_example' # str | objectivePower__range (optional)
width = 'width_example' # str | width (optional)
width__range = 'width__range_example' # str | width__range (optional)
height = 'height_example' # str | height (optional)
height__range = 'height__range_example' # str | height__range (optional)
image_set = 'image_set_example' # str | image_set (optional)
image_type = 'image_type_example' # str | image_type (optional)
annotation_type = 'annotation_type_example' # str | annotation_type (optional)
num_annotations = 'num_annotations_example' # str | num_annotations (optional)
verified = 'verified_example' # str | verified (optional)

try:
    api_response = api_instance.update_image(id, body=body, id2=id2, name=name, name__contains=name__contains, filename=filename, filename__contains=filename__contains, time=time, time__contains=time__contains, mpp=mpp, mpp__range=mpp__range, objective_power=objective_power, objective_power__range=objective_power__range, width=width, width__range=width__range, height=height, height__range=height__range, image_set=image_set, image_type=image_type, annotation_type=annotation_type, num_annotations=num_annotations, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Image**](Image.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **filename** | **str**| filename | [optional] 
 **filename__contains** | **str**| filename__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__contains** | **str**| time__contains | [optional] 
 **mpp** | **str**| mpp | [optional] 
 **mpp__range** | **str**| mpp__range | [optional] 
 **objective_power** | **str**| objectivePower | [optional] 
 **objective_power__range** | **str**| objectivePower__range | [optional] 
 **width** | **str**| width | [optional] 
 **width__range** | **str**| width__range | [optional] 
 **height** | **str**| height | [optional] 
 **height__range** | **str**| height__range | [optional] 
 **image_set** | **str**| image_set | [optional] 
 **image_type** | **str**| image_type | [optional] 
 **annotation_type** | **str**| annotation_type | [optional] 
 **num_annotations** | **str**| num_annotations | [optional] 
 **verified** | **str**| verified | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image_registration**
> ImageRegistration update_image_registration(id, body=body, id2=id2, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ImageRegistration() # ImageRegistration |  (optional)
id2 = 'id_example' # str | id (optional)
target_image = 'target_image_example' # str | target_image (optional)
source_image = 'source_image_example' # str | source_image (optional)
registration_error__range = 'registration_error__range_example' # str | registration_error__range (optional)
runtime__range = 'runtime__range_example' # str | runtime__range (optional)

try:
    api_response = api_instance.update_image_registration(id, body=body, id2=id2, target_image=target_image, source_image=source_image, registration_error__range=registration_error__range, runtime__range=runtime__range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_image_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ImageRegistration**](ImageRegistration.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **target_image** | **str**| target_image | [optional] 
 **source_image** | **str**| source_image | [optional] 
 **registration_error__range** | **str**| registration_error__range | [optional] 
 **runtime__range** | **str**| runtime__range | [optional] 

### Return type

[**ImageRegistration**](ImageRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image_set**
> ImageSet update_image_set(id, body=body, id2=id2, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ImageSet() # ImageSet |  (optional)
id2 = 'id_example' # str | id (optional)
path = 'path_example' # str | path (optional)
path__contains = 'path__contains_example' # str | path__contains (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
location = 'location_example' # str | location (optional)
location__contains = 'location__contains_example' # str | location__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
time = 'time_example' # str | time (optional)
time__range = 'time__range_example' # str | time__range (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
public = 'public_example' # str | public (optional)
main_annotation_type = 'main_annotation_type_example' # str | main_annotation_type (optional)
set_tags = 'set_tags_example' # str | set_tags (optional)
set_versions = 'set_versions_example' # str | set_versions (optional)
product = 'product_example' # str | product (optional)
collaboration_type = 'collaboration_type_example' # str | collaboration_type (optional)
priority = 'priority_example' # str | priority (optional)
zip_state = 'zip_state_example' # str | zip_state (optional)
images = 'images_example' # str | images (optional)

try:
    api_response = api_instance.update_image_set(id, body=body, id2=id2, path=path, path__contains=path__contains, name=name, name__contains=name__contains, location=location, location__contains=location__contains, description=description, description__contains=description__contains, time=time, time__range=time__range, team=team, creator=creator, public=public, main_annotation_type=main_annotation_type, set_tags=set_tags, set_versions=set_versions, product=product, collaboration_type=collaboration_type, priority=priority, zip_state=zip_state, images=images)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_image_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ImageSet**](ImageSet.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **path** | **str**| path | [optional] 
 **path__contains** | **str**| path__contains | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **location** | **str**| location | [optional] 
 **location__contains** | **str**| location__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **time** | **str**| time | [optional] 
 **time__range** | **str**| time__range | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **public** | **str**| public | [optional] 
 **main_annotation_type** | **str**| main_annotation_type | [optional] 
 **set_tags** | **str**| set_tags | [optional] 
 **set_versions** | **str**| set_versions | [optional] 
 **product** | **str**| product | [optional] 
 **collaboration_type** | **str**| collaboration_type | [optional] 
 **priority** | **str**| priority | [optional] 
 **zip_state** | **str**| zip_state | [optional] 
 **images** | **str**| images | [optional] 

### Return type

[**ImageSet**](ImageSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screening_mode**
> ScreeningMode update_screening_mode(id, body=body, id2=id2, image=image, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.ScreeningMode() # ScreeningMode |  (optional)
id2 = 'id_example' # str | id (optional)
image = 'image_example' # str | image (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.update_screening_mode(id, body=body, id2=id2, image=image, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_screening_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ScreeningMode**](ScreeningMode.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **image** | **str**| image | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**ScreeningMode**](ScreeningMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_set_tag**
> SetTag update_set_tag(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.SetTag() # SetTag |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.update_set_tag(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SetTag**](SetTag.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetTag**](SetTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_set_version**
> SetVersion update_set_version(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | 
body = swagger_client.SetVersion() # SetVersion |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)

try:
    api_response = api_instance.update_set_version(id, body=body, id2=id2, name=name, name__contains=name__contains, imagesets=imagesets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_set_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SetVersion**](SetVersion.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **imagesets** | **str**| imagesets | [optional] 

### Return type

[**SetVersion**](SetVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

