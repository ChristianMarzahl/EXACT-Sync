# swagger_client.AdministrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](AdministrationApi.md#create_product) | **POST** /api/v1/administration/products/ | 
[**destroy_product**](AdministrationApi.md#destroy_product) | **DELETE** /api/v1/administration/products/{id}/ | 
[**list_products**](AdministrationApi.md#list_products) | **GET** /api/v1/administration/products/ | 
[**partial_update_product**](AdministrationApi.md#partial_update_product) | **PATCH** /api/v1/administration/products/{id}/ | 
[**retrieve_product**](AdministrationApi.md#retrieve_product) | **GET** /api/v1/administration/products/{id}/ | 
[**update_product**](AdministrationApi.md#update_product) | **PUT** /api/v1/administration/products/{id}/ | 

# **create_product**
> Product create_product(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
body = swagger_client.Product() # Product |  (optional)

try:
    api_response = api_instance.create_product(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_product**
> destroy_product(id, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)
annotationtype = 'annotationtype_example' # str | annotationtype (optional)

try:
    api_instance.destroy_product(id, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)
except ApiException as e:
    print("Exception when calling AdministrationApi->destroy_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **imagesets** | **str**| imagesets | [optional] 
 **annotationtype** | **str**| annotationtype | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> InlineResponse20015 list_products(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)
annotationtype = 'annotationtype_example' # str | annotationtype (optional)

try:
    api_response = api_instance.list_products(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **imagesets** | **str**| imagesets | [optional] 
 **annotationtype** | **str**| annotationtype | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_product**
> Product partial_update_product(id, body=body, id2=id2, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
id = 'id_example' # str | 
body = swagger_client.Product() # Product |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)
annotationtype = 'annotationtype_example' # str | annotationtype (optional)

try:
    api_response = api_instance.partial_update_product(id, body=body, id2=id2, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->partial_update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Product**](Product.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **imagesets** | **str**| imagesets | [optional] 
 **annotationtype** | **str**| annotationtype | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_product**
> Product retrieve_product(id, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)
annotationtype = 'annotationtype_example' # str | annotationtype (optional)

try:
    api_response = api_instance.retrieve_product(id, id=id, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->retrieve_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **imagesets** | **str**| imagesets | [optional] 
 **annotationtype** | **str**| annotationtype | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> Product update_product(id, body=body, id2=id2, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationApi()
id = 'id_example' # str | 
body = swagger_client.Product() # Product |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
description = 'description_example' # str | description (optional)
description__contains = 'description__contains_example' # str | description__contains (optional)
team = 'team_example' # str | team (optional)
creator = 'creator_example' # str | creator (optional)
imagesets = 'imagesets_example' # str | imagesets (optional)
annotationtype = 'annotationtype_example' # str | annotationtype (optional)

try:
    api_response = api_instance.update_product(id, body=body, id2=id2, name=name, name__contains=name__contains, description=description, description__contains=description__contains, team=team, creator=creator, imagesets=imagesets, annotationtype=annotationtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Product**](Product.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **description** | **str**| description | [optional] 
 **description__contains** | **str**| description__contains | [optional] 
 **team** | **str**| team | [optional] 
 **creator** | **str**| creator | [optional] 
 **imagesets** | **str**| imagesets | [optional] 
 **annotationtype** | **str**| annotationtype | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

