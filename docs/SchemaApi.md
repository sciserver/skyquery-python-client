# skyquery.SchemaApi

All URIs are relative to *http://localhost/dobos/skyquery-v1.4/Api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset**](SchemaApi.md#get_dataset) | **GET** /V1/Schema.svc/datasets/{datasetName} | Returns information about a single dataset
[**get_table**](SchemaApi.md#get_table) | **GET** /V1/Schema.svc/datasets/{datasetName}/tables/{tableName} | Returns information about a single table.
[**get_view**](SchemaApi.md#get_view) | **GET** /V1/Schema.svc/datasets/{datasetName}/views/{viewName} | Returns information about a single view.
[**list_datasets**](SchemaApi.md#list_datasets) | **GET** /V1/Schema.svc/datasets | Returns a list of all available datasets.
[**list_table_columns**](SchemaApi.md#list_table_columns) | **GET** /V1/Schema.svc/datasets/{datasetName}/tables/{tableName}/columns | Returns the list of columns of a table
[**list_tables**](SchemaApi.md#list_tables) | **GET** /V1/Schema.svc/datasets/{datasetName}/tables | Returns a list of the tables of a dataset.
[**list_view_columns**](SchemaApi.md#list_view_columns) | **GET** /V1/Schema.svc/datasets/{datasetName}/views/{viewName}/columns | Returns the list of columns of a view
[**list_views**](SchemaApi.md#list_views) | **GET** /V1/Schema.svc/datasets/{datasetName}/views | Returns a list of the views of a dataset.


# **get_dataset**
> Dataset get_dataset(dataset_name)

Returns information about a single dataset

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 

try:
    # Returns information about a single dataset
    api_response = api_instance.get_dataset(dataset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> Table get_table(dataset_name, table_name)

Returns information about a single table.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 
table_name = 'table_name_example' # str | 

try:
    # Returns information about a single table.
    api_response = api_instance.get_table(dataset_name, table_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **table_name** | **str**|  | 

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> View get_view(dataset_name, view_name)

Returns information about a single view.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 
view_name = 'view_name_example' # str | 

try:
    # Returns information about a single view.
    api_response = api_instance.get_view(dataset_name, view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **view_name** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets**
> DatasetListResponse list_datasets()

Returns a list of all available datasets.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()

try:
    # Returns a list of all available datasets.
    api_response = api_instance.list_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetListResponse**](DatasetListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_table_columns**
> ColumnListResponse list_table_columns(dataset_name, table_name)

Returns the list of columns of a table

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 
table_name = 'table_name_example' # str | 

try:
    # Returns the list of columns of a table
    api_response = api_instance.list_table_columns(dataset_name, table_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_table_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **table_name** | **str**|  | 

### Return type

[**ColumnListResponse**](ColumnListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tables**
> TableListResponse list_tables(dataset_name)

Returns a list of the tables of a dataset.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 

try:
    # Returns a list of the tables of a dataset.
    api_response = api_instance.list_tables(dataset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 

### Return type

[**TableListResponse**](TableListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_view_columns**
> ColumnListResponse list_view_columns(dataset_name, view_name)

Returns the list of columns of a view

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 
view_name = 'view_name_example' # str | 

try:
    # Returns the list of columns of a view
    api_response = api_instance.list_view_columns(dataset_name, view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_view_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 
 **view_name** | **str**|  | 

### Return type

[**ColumnListResponse**](ColumnListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_views**
> ViewListResponse list_views(dataset_name)

Returns a list of the views of a dataset.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.SchemaApi()
dataset_name = 'dataset_name_example' # str | 

try:
    # Returns a list of the views of a dataset.
    api_response = api_instance.list_views(dataset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 

### Return type

[**ViewListResponse**](ViewListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

