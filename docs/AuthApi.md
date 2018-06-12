# skyquery.AuthApi

All URIs are relative to *http://localhost/dobos/skyquery-v1.4/Api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthApi.md#authenticate) | **POST** /V1/Auth.svc/ | Authenticates a user based on the submitted credentials.
[**find_user_groups**](AuthApi.md#find_user_groups) | **GET** /V1/Auth.svc/groups | 
[**get_current_user**](AuthApi.md#get_current_user) | **GET** /V1/Auth.svc/me | Returns information on the authenticated user.
[**get_current_user_role_in_group**](AuthApi.md#get_current_user_role_in_group) | **GET** /V1/Auth.svc/me/roles/{groupName} | Returns information on group membership.
[**get_current_user_roles**](AuthApi.md#get_current_user_roles) | **GET** /V1/Auth.svc/me/roles | Returns information on group membership.
[**get_user**](AuthApi.md#get_user) | **GET** /V1/Auth.svc/users/{name} | 
[**get_user_group**](AuthApi.md#get_user_group) | **GET** /V1/Auth.svc/groups/{name} | 
[**get_user_group_members**](AuthApi.md#get_user_group_members) | **GET** /V1/Auth.svc/groups/{name}/members | 
[**get_user_role_in_group**](AuthApi.md#get_user_role_in_group) | **GET** /V1/Auth.svc/users/{name}/roles/{groupName} | Returns information on group membership.
[**get_user_roles**](AuthApi.md#get_user_roles) | **GET** /V1/Auth.svc/users/{name}/roles | 


# **authenticate**
> RestError authenticate(auth_request)

Authenticates a user based on the submitted credentials.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
auth_request = skyquery.AuthRequest() # AuthRequest | 

try:
    # Authenticates a user based on the submitted credentials.
    api_response = api_instance.authenticate(auth_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_groups**
> UserGroupListResponse find_user_groups()



### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()

try:
    # 
    api_response = api_instance.find_user_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->find_user_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserGroupListResponse**](UserGroupListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserResponse get_current_user()

Returns information on the authenticated user.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()

try:
    # Returns information on the authenticated user.
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_role_in_group**
> UserMembershipResponse get_current_user_role_in_group(group_name)

Returns information on group membership.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
group_name = 'group_name_example' # str | 

try:
    # Returns information on group membership.
    api_response = api_instance.get_current_user_role_in_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_current_user_role_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 

### Return type

[**UserMembershipResponse**](UserMembershipResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_roles**
> UserMembershipListResponse get_current_user_roles()

Returns information on group membership.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()

try:
    # Returns information on group membership.
    api_response = api_instance.get_current_user_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_current_user_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserMembershipListResponse**](UserMembershipListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(name)



### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
name = 'name_example' # str | 

try:
    # 
    api_response = api_instance.get_user(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> UserGroupResponse get_user_group(name)



### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
name = 'name_example' # str | 

try:
    # 
    api_response = api_instance.get_user_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_members**
> UserMembershipListResponse get_user_group_members(name)



### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
name = 'name_example' # str | 

try:
    # 
    api_response = api_instance.get_user_group_members(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**UserMembershipListResponse**](UserMembershipListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_role_in_group**
> UserMembershipResponse get_user_role_in_group(name, group_name)

Returns information on group membership.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
name = 'name_example' # str | 
group_name = 'group_name_example' # str | 

try:
    # Returns information on group membership.
    api_response = api_instance.get_user_role_in_group(name, group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user_role_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **group_name** | **str**|  | 

### Return type

[**UserMembershipResponse**](UserMembershipResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> UserMembershipListResponse get_user_roles(name)



### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.AuthApi()
name = 'name_example' # str | 

try:
    # 
    api_response = api_instance.get_user_roles(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**UserMembershipListResponse**](UserMembershipListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

