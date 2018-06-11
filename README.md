# skyquery
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: null
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import skyquery 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import skyquery
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import skyquery
from skyquery.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = skyquery.AuthApi()
auth_request = skyquery.AuthRequest() # AuthRequest | null

try:
    # Authenticates a user based on the submitted credentials.
    api_response = api_instance.authenticate(auth_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authenticate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/dobos/skyquery-v1.4/Api/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authenticate**](docs/AuthApi.md#authenticate) | **POST** V1/Auth.svc/ | Authenticates a user based on the submitted credentials.
*AuthApi* | [**find_user_groups**](docs/AuthApi.md#find_user_groups) | **GET** V1/Auth.svc/groups | 
*AuthApi* | [**get_current_user**](docs/AuthApi.md#get_current_user) | **GET** V1/Auth.svc/me | Returns information on the authenticated user.
*AuthApi* | [**get_current_user_role_in_group**](docs/AuthApi.md#get_current_user_role_in_group) | **GET** V1/Auth.svc/me/roles/{groupName} | Returns information on group membership.
*AuthApi* | [**get_current_user_roles**](docs/AuthApi.md#get_current_user_roles) | **GET** V1/Auth.svc/me/roles | Returns information on group membership.
*AuthApi* | [**get_user**](docs/AuthApi.md#get_user) | **GET** V1/Auth.svc/users/{name} | 
*AuthApi* | [**get_user_group**](docs/AuthApi.md#get_user_group) | **GET** V1/Auth.svc/groups/{name} | 
*AuthApi* | [**get_user_group_members**](docs/AuthApi.md#get_user_group_members) | **GET** V1/Auth.svc/groups/{name}/members | 
*AuthApi* | [**get_user_role_in_group**](docs/AuthApi.md#get_user_role_in_group) | **GET** V1/Auth.svc/users/{name}/roles/{groupName} | Returns information on group membership.
*AuthApi* | [**get_user_roles**](docs/AuthApi.md#get_user_roles) | **GET** V1/Auth.svc/users/{name}/roles | 
*DataApi* | [**download_table**](docs/DataApi.md#download_table) | **GET** V1/Data.svc/{datasetName}/{tableName} | Downloads a table in any supported data format.
*DataApi* | [**drop_table**](docs/DataApi.md#drop_table) | **DELETE** V1/Data.svc/{datasetName}/{tableName} | Drops a table from the user database.
*DataApi* | [**upload_table**](docs/DataApi.md#upload_table) | **PUT** V1/Data.svc/{datasetName}/{tableName} | Uploads a table to a user database.
*JobsApi* | [**cancel_job**](docs/JobsApi.md#cancel_job) | **DELETE** V1/Jobs.svc/jobs/{guid} | Cancels a single job.
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** V1/Jobs.svc/jobs/{guid} | Returns a single job.
*JobsApi* | [**get_queue**](docs/JobsApi.md#get_queue) | **GET** V1/Jobs.svc/queues/{queue} | Returns information about a job queue.
*JobsApi* | [**list_jobs**](docs/JobsApi.md#list_jobs) | **GET** V1/Jobs.svc/queues/{queue}/jobs | Lists the jobs in the queue in descending order by submission time. Only jobs of the authenticated user are listed.
*JobsApi* | [**list_queues**](docs/JobsApi.md#list_queues) | **GET** V1/Jobs.svc/queues | Returns a list of all available job queues.
*JobsApi* | [**submit_job**](docs/JobsApi.md#submit_job) | **POST** V1/Jobs.svc/queues/{queue}/jobs | Submits a new job of any kind.
*SchemaApi* | [**get_dataset**](docs/SchemaApi.md#get_dataset) | **GET** V1/Schema.svc/datasets/{datasetName} | Returns information about a single dataset
*SchemaApi* | [**get_table**](docs/SchemaApi.md#get_table) | **GET** V1/Schema.svc/datasets/{datasetName}/tables/{tableName} | Returns information about a single table.
*SchemaApi* | [**get_view**](docs/SchemaApi.md#get_view) | **GET** V1/Schema.svc/datasets/{datasetName}/views/{viewName} | Returns information about a single view.
*SchemaApi* | [**list_datasets**](docs/SchemaApi.md#list_datasets) | **GET** V1/Schema.svc/datasets | Returns a list of all available datasets.
*SchemaApi* | [**list_table_columns**](docs/SchemaApi.md#list_table_columns) | **GET** V1/Schema.svc/datasets/{datasetName}/tables/{tableName}/columns | Returns the list of columns of a table
*SchemaApi* | [**list_tables**](docs/SchemaApi.md#list_tables) | **GET** V1/Schema.svc/datasets/{datasetName}/tables | Returns a list of the tables of a dataset.
*SchemaApi* | [**list_view_columns**](docs/SchemaApi.md#list_view_columns) | **GET** V1/Schema.svc/datasets/{datasetName}/views/{viewName}/columns | Returns the list of columns of a view
*SchemaApi* | [**list_views**](docs/SchemaApi.md#list_views) | **GET** V1/Schema.svc/datasets/{datasetName}/views | Returns a list of the views of a dataset.


## Documentation For Models

 - [AuthRequest](docs/AuthRequest.md)
 - [Column](docs/Column.md)
 - [ColumnListResponse](docs/ColumnListResponse.md)
 - [CopyJob](docs/CopyJob.md)
 - [Credentials](docs/Credentials.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetListResponse](docs/DatasetListResponse.md)
 - [DestinationTable](docs/DestinationTable.md)
 - [ExportJob](docs/ExportJob.md)
 - [FileFormat](docs/FileFormat.md)
 - [Headers](docs/Headers.md)
 - [ImportJob](docs/ImportJob.md)
 - [Job](docs/Job.md)
 - [JobDependency](docs/JobDependency.md)
 - [JobListResponse](docs/JobListResponse.md)
 - [JobRequest](docs/JobRequest.md)
 - [JobResponse](docs/JobResponse.md)
 - [QueryJob](docs/QueryJob.md)
 - [Queue](docs/Queue.md)
 - [QueueListResponse](docs/QueueListResponse.md)
 - [QueueResponse](docs/QueueResponse.md)
 - [RestError](docs/RestError.md)
 - [SourceTable](docs/SourceTable.md)
 - [SqlScriptJob](docs/SqlScriptJob.md)
 - [Table](docs/Table.md)
 - [TableListResponse](docs/TableListResponse.md)
 - [User](docs/User.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserGroupListResponse](docs/UserGroupListResponse.md)
 - [UserGroupResponse](docs/UserGroupResponse.md)
 - [UserMembership](docs/UserMembership.md)
 - [UserMembershipListResponse](docs/UserMembershipListResponse.md)
 - [UserMembershipResponse](docs/UserMembershipResponse.md)
 - [UserResponse](docs/UserResponse.md)
 - [View](docs/View.md)
 - [ViewListResponse](docs/ViewListResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



