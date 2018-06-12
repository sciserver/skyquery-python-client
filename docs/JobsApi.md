# skyquery.JobsApi

All URIs are relative to *http://localhost/dobos/skyquery-v1.4/Api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **DELETE** /V1/Jobs.svc/jobs/{guid} | Cancels a single job.
[**get_job**](JobsApi.md#get_job) | **GET** /V1/Jobs.svc/jobs/{guid} | Returns a single job.
[**get_queue**](JobsApi.md#get_queue) | **GET** /V1/Jobs.svc/queues/{queue} | Returns information about a job queue.
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /V1/Jobs.svc/queues/{queue}/jobs | Lists the jobs in the queue in descending order by submission time. Only jobs of the authenticated user are listed.
[**list_queues**](JobsApi.md#list_queues) | **GET** /V1/Jobs.svc/queues | Returns a list of all available job queues.
[**submit_job**](JobsApi.md#submit_job) | **POST** /V1/Jobs.svc/queues/{queue}/jobs | Submits a new job of any kind.


# **cancel_job**
> JobResponse cancel_job(guid)

Cancels a single job.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()
guid = 'guid_example' # str | 

try:
    # Cancels a single job.
    api_response = api_instance.cancel_job(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobResponse get_job(guid)

Returns a single job.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()
guid = 'guid_example' # str | 

try:
    # Returns a single job.
    api_response = api_instance.get_job(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue**
> QueueResponse get_queue(queue)

Returns information about a job queue.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()
queue = 'queue_example' # str | 

try:
    # Returns information about a job queue.
    api_response = api_instance.get_queue(queue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue** | **str**|  | 

### Return type

[**QueueResponse**](QueueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobListResponse list_jobs(queue, type=type, _from=_from, max=max)

Lists the jobs in the queue in descending order by submission time. Only jobs of the authenticated user are listed.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()
queue = 'queue_example' # str | 
type = 'type_example' # str |  (optional)
_from = '_from_example' # str |  (optional)
max = 'max_example' # str |  (optional)

try:
    # Lists the jobs in the queue in descending order by submission time. Only jobs of the authenticated user are listed.
    api_response = api_instance.list_jobs(queue, type=type, _from=_from, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue** | **str**|  | 
 **type** | **str**|  | [optional] 
 **_from** | **str**|  | [optional] 
 **max** | **str**|  | [optional] 

### Return type

[**JobListResponse**](JobListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queues**
> QueueListResponse list_queues()

Returns a list of all available job queues.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()

try:
    # Returns a list of all available job queues.
    api_response = api_instance.list_queues()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_queues: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueueListResponse**](QueueListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job**
> JobResponse submit_job(queue, job)

Submits a new job of any kind.

### Example
```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyquery.JobsApi()
queue = 'queue_example' # str | 
job = skyquery.JobRequest() # JobRequest | 

try:
    # Submits a new job of any kind.
    api_response = api_instance.submit_job(queue, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->submit_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue** | **str**|  | 
 **job** | [**JobRequest**](JobRequest.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

