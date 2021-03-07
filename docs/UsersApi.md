# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](UsersApi.md#create_team) | **POST** /api/v1/users/teams/ | 
[**create_team_membership**](UsersApi.md#create_team_membership) | **POST** /api/v1/users/team_membership/ | 
[**create_user**](UsersApi.md#create_user) | **POST** /api/v1/users/users/ | 
[**destroy_team**](UsersApi.md#destroy_team) | **DELETE** /api/v1/users/teams/{id}/ | 
[**destroy_team_membership**](UsersApi.md#destroy_team_membership) | **DELETE** /api/v1/users/team_membership/{id}/ | 
[**destroy_user**](UsersApi.md#destroy_user) | **DELETE** /api/v1/users/users/{id}/ | 
[**list_team_memberships**](UsersApi.md#list_team_memberships) | **GET** /api/v1/users/team_membership/ | 
[**list_teams**](UsersApi.md#list_teams) | **GET** /api/v1/users/teams/ | 
[**list_users**](UsersApi.md#list_users) | **GET** /api/v1/users/users/ | 
[**partial_update_team**](UsersApi.md#partial_update_team) | **PATCH** /api/v1/users/teams/{id}/ | 
[**partial_update_team_membership**](UsersApi.md#partial_update_team_membership) | **PATCH** /api/v1/users/team_membership/{id}/ | 
[**partial_update_user**](UsersApi.md#partial_update_user) | **PATCH** /api/v1/users/users/{id}/ | 
[**retrieve_team**](UsersApi.md#retrieve_team) | **GET** /api/v1/users/teams/{id}/ | 
[**retrieve_team_membership**](UsersApi.md#retrieve_team_membership) | **GET** /api/v1/users/team_membership/{id}/ | 
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /api/v1/users/users/{id}/ | 
[**update_team**](UsersApi.md#update_team) | **PUT** /api/v1/users/teams/{id}/ | 
[**update_team_membership**](UsersApi.md#update_team_membership) | **PUT** /api/v1/users/team_membership/{id}/ | 
[**update_user**](UsersApi.md#update_user) | **PUT** /api/v1/users/users/{id}/ | 

# **create_team**
> Team create_team(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.Team() # Team |  (optional)

try:
    api_response = api_instance.create_team(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team_membership**
> TeamMembership create_team_membership(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.TeamMembership() # TeamMembership |  (optional)

try:
    api_response = api_instance.create_team_membership(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_team_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamMembership**](TeamMembership.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.User() # User |  (optional)

try:
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_team**
> destroy_team(id, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
members = 'members_example' # str | members (optional)
image_sets = 'image_sets_example' # str | image_sets (optional)

try:
    api_instance.destroy_team(id, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)
except ApiException as e:
    print("Exception when calling UsersApi->destroy_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **members** | **str**| members | [optional] 
 **image_sets** | **str**| image_sets | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_team_membership**
> destroy_team_membership(id, id=id, is_admin=is_admin, team=team, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
is_admin = 'is_admin_example' # str | is_admin (optional)
team = 'team_example' # str | team (optional)
user = 'user_example' # str | user (optional)

try:
    api_instance.destroy_team_membership(id, id=id, is_admin=is_admin, team=team, user=user)
except ApiException as e:
    print("Exception when calling UsersApi->destroy_team_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **is_admin** | **str**| is_admin | [optional] 
 **team** | **str**| team | [optional] 
 **user** | **str**| user | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_user**
> destroy_user(id, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
username = 'username_example' # str | username (optional)
username__contains = 'username__contains_example' # str | username__contains (optional)
is_superuser = 'is_superuser_example' # str | is_superuser (optional)
is_staff = 'is_staff_example' # str | is_staff (optional)
is_active = 'is_active_example' # str | is_active (optional)
last_login = 'last_login_example' # str | last_login (optional)
team = 'team_example' # str | team (optional)

try:
    api_instance.destroy_user(id, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)
except ApiException as e:
    print("Exception when calling UsersApi->destroy_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **username** | **str**| username | [optional] 
 **username__contains** | **str**| username__contains | [optional] 
 **is_superuser** | **str**| is_superuser | [optional] 
 **is_staff** | **str**| is_staff | [optional] 
 **is_active** | **str**| is_active | [optional] 
 **last_login** | **str**| last_login | [optional] 
 **team** | **str**| team | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_memberships**
> InlineResponse2002 list_team_memberships(limit=limit, offset=offset, id=id, is_admin=is_admin, team=team, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
is_admin = 'is_admin_example' # str | is_admin (optional)
team = 'team_example' # str | team (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.list_team_memberships(limit=limit, offset=offset, id=id, is_admin=is_admin, team=team, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_team_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **is_admin** | **str**| is_admin | [optional] 
 **team** | **str**| team | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> InlineResponse2001 list_teams(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
members = 'members_example' # str | members (optional)
image_sets = 'image_sets_example' # str | image_sets (optional)

try:
    api_response = api_instance.list_teams(limit=limit, offset=offset, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **members** | **str**| members | [optional] 
 **image_sets** | **str**| image_sets | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> InlineResponse200 list_users(limit=limit, offset=offset, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
id = 'id_example' # str | id (optional)
username = 'username_example' # str | username (optional)
username__contains = 'username__contains_example' # str | username__contains (optional)
is_superuser = 'is_superuser_example' # str | is_superuser (optional)
is_staff = 'is_staff_example' # str | is_staff (optional)
is_active = 'is_active_example' # str | is_active (optional)
last_login = 'last_login_example' # str | last_login (optional)
team = 'team_example' # str | team (optional)

try:
    api_response = api_instance.list_users(limit=limit, offset=offset, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **id** | **str**| id | [optional] 
 **username** | **str**| username | [optional] 
 **username__contains** | **str**| username__contains | [optional] 
 **is_superuser** | **str**| is_superuser | [optional] 
 **is_staff** | **str**| is_staff | [optional] 
 **is_active** | **str**| is_active | [optional] 
 **last_login** | **str**| last_login | [optional] 
 **team** | **str**| team | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_team**
> Team partial_update_team(id, body=body, id2=id2, name=name, name__contains=name__contains, members=members, image_sets=image_sets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.Team() # Team |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
members = 'members_example' # str | members (optional)
image_sets = 'image_sets_example' # str | image_sets (optional)

try:
    api_response = api_instance.partial_update_team(id, body=body, id2=id2, name=name, name__contains=name__contains, members=members, image_sets=image_sets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->partial_update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Team**](Team.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **members** | **str**| members | [optional] 
 **image_sets** | **str**| image_sets | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_team_membership**
> TeamMembership partial_update_team_membership(id, body=body, id2=id2, is_admin=is_admin, team=team, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.TeamMembership() # TeamMembership |  (optional)
id2 = 'id_example' # str | id (optional)
is_admin = 'is_admin_example' # str | is_admin (optional)
team = 'team_example' # str | team (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.partial_update_team_membership(id, body=body, id2=id2, is_admin=is_admin, team=team, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->partial_update_team_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**TeamMembership**](TeamMembership.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **is_admin** | **str**| is_admin | [optional] 
 **team** | **str**| team | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_user**
> User partial_update_user(id, body=body, id2=id2, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.User() # User |  (optional)
id2 = 'id_example' # str | id (optional)
username = 'username_example' # str | username (optional)
username__contains = 'username__contains_example' # str | username__contains (optional)
is_superuser = 'is_superuser_example' # str | is_superuser (optional)
is_staff = 'is_staff_example' # str | is_staff (optional)
is_active = 'is_active_example' # str | is_active (optional)
last_login = 'last_login_example' # str | last_login (optional)
team = 'team_example' # str | team (optional)

try:
    api_response = api_instance.partial_update_user(id, body=body, id2=id2, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->partial_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**User**](User.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **username** | **str**| username | [optional] 
 **username__contains** | **str**| username__contains | [optional] 
 **is_superuser** | **str**| is_superuser | [optional] 
 **is_staff** | **str**| is_staff | [optional] 
 **is_active** | **str**| is_active | [optional] 
 **last_login** | **str**| last_login | [optional] 
 **team** | **str**| team | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_team**
> Team retrieve_team(id, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
members = 'members_example' # str | members (optional)
image_sets = 'image_sets_example' # str | image_sets (optional)

try:
    api_response = api_instance.retrieve_team(id, id=id, name=name, name__contains=name__contains, members=members, image_sets=image_sets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **members** | **str**| members | [optional] 
 **image_sets** | **str**| image_sets | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_team_membership**
> TeamMembership retrieve_team_membership(id, id=id, is_admin=is_admin, team=team, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
is_admin = 'is_admin_example' # str | is_admin (optional)
team = 'team_example' # str | team (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.retrieve_team_membership(id, id=id, is_admin=is_admin, team=team, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_team_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **is_admin** | **str**| is_admin | [optional] 
 **team** | **str**| team | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> User retrieve_user(id, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
id = 'id_example' # str | id (optional)
username = 'username_example' # str | username (optional)
username__contains = 'username__contains_example' # str | username__contains (optional)
is_superuser = 'is_superuser_example' # str | is_superuser (optional)
is_staff = 'is_staff_example' # str | is_staff (optional)
is_active = 'is_active_example' # str | is_active (optional)
last_login = 'last_login_example' # str | last_login (optional)
team = 'team_example' # str | team (optional)

try:
    api_response = api_instance.retrieve_user(id, id=id, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id** | **str**| id | [optional] 
 **username** | **str**| username | [optional] 
 **username__contains** | **str**| username__contains | [optional] 
 **is_superuser** | **str**| is_superuser | [optional] 
 **is_staff** | **str**| is_staff | [optional] 
 **is_active** | **str**| is_active | [optional] 
 **last_login** | **str**| last_login | [optional] 
 **team** | **str**| team | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(id, body=body, id2=id2, name=name, name__contains=name__contains, members=members, image_sets=image_sets)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.Team() # Team |  (optional)
id2 = 'id_example' # str | id (optional)
name = 'name_example' # str | name (optional)
name__contains = 'name__contains_example' # str | name__contains (optional)
members = 'members_example' # str | members (optional)
image_sets = 'image_sets_example' # str | image_sets (optional)

try:
    api_response = api_instance.update_team(id, body=body, id2=id2, name=name, name__contains=name__contains, members=members, image_sets=image_sets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Team**](Team.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **name** | **str**| name | [optional] 
 **name__contains** | **str**| name__contains | [optional] 
 **members** | **str**| members | [optional] 
 **image_sets** | **str**| image_sets | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_membership**
> TeamMembership update_team_membership(id, body=body, id2=id2, is_admin=is_admin, team=team, user=user)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.TeamMembership() # TeamMembership |  (optional)
id2 = 'id_example' # str | id (optional)
is_admin = 'is_admin_example' # str | is_admin (optional)
team = 'team_example' # str | team (optional)
user = 'user_example' # str | user (optional)

try:
    api_response = api_instance.update_team_membership(id, body=body, id2=id2, is_admin=is_admin, team=team, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_team_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**TeamMembership**](TeamMembership.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **is_admin** | **str**| is_admin | [optional] 
 **team** | **str**| team | [optional] 
 **user** | **str**| user | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(id, body=body, id2=id2, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.User() # User |  (optional)
id2 = 'id_example' # str | id (optional)
username = 'username_example' # str | username (optional)
username__contains = 'username__contains_example' # str | username__contains (optional)
is_superuser = 'is_superuser_example' # str | is_superuser (optional)
is_staff = 'is_staff_example' # str | is_staff (optional)
is_active = 'is_active_example' # str | is_active (optional)
last_login = 'last_login_example' # str | last_login (optional)
team = 'team_example' # str | team (optional)

try:
    api_response = api_instance.update_user(id, body=body, id2=id2, username=username, username__contains=username__contains, is_superuser=is_superuser, is_staff=is_staff, is_active=is_active, last_login=last_login, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**User**](User.md)|  | [optional] 
 **id2** | **str**| id | [optional] 
 **username** | **str**| username | [optional] 
 **username__contains** | **str**| username__contains | [optional] 
 **is_superuser** | **str**| is_superuser | [optional] 
 **is_staff** | **str**| is_staff | [optional] 
 **is_active** | **str**| is_active | [optional] 
 **last_login** | **str**| last_login | [optional] 
 **team** | **str**| team | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

