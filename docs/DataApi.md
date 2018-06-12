# skyquery.DataApi

All URIs are relative to *http://localhost/dobos/skyquery-v1.4/Api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_table**](DataApi.md#download_table) | **GET** /V1/Data.svc/{datasetName}/{tableName} | Downloads a table in any supported data format.
[**drop_table**](DataApi.md#drop_table) | **DELETE** /V1/Data.svc/{datasetName}/{tableName} | Drops a table from the user database.
[**upload_table**](DataApi.md#upload_table) | **PUT** /V1/Data.svc/{datasetName}/{tableName} | Uploads a table to a user database.


# **download_table**
> download_table(dataset_name, table_name, accept, top=top)

Downloads a table in any supported data format.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.DataApi()
dataset_name = 'dataset_name_example' # str | 
table_name = 'table_name_example' # str | 
accept = 'application/json' # str | File format mime type. (default to application/json)
top = 'top_example' # str |  (optional)

try:
    # Downloads a table in any supported data format.
    api_instance.download_table(dataset_name, table_name, accept, top=top)
except ApiException as e:
    print("Exception when calling DataApi->download_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **table_name** | **str**|  | 
 **accept** | **str**| File format mime type. | [default to application/json]
 **top** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_table**
> RestError drop_table(dataset_name, table_name)

Drops a table from the user database.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.DataApi()
dataset_name = 'dataset_name_example' # str | 
table_name = 'table_name_example' # str | 

try:
    # Drops a table from the user database.
    api_response = api_instance.drop_table(dataset_name, table_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->drop_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **table_name** | **str**|  | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_table**
> RestError upload_table(dataset_name, table_name, content_type, data)

Uploads a table to a user database.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.DataApi()
dataset_name = 'dataset_name_example' # str | 
table_name = 'table_name_example' # str | 
content_type = 'application/json' # str | File format mime type. (default to application/json)
data = skyquery.null() #  | 

try:
    # Uploads a table to a user database.
    api_response = api_instance.upload_table(dataset_name, table_name, content_type, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->upload_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **table_name** | **str**|  | 
 **content_type** | **str**| File format mime type. | [default to application/json]
 **data** | [****](.md)|  | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

