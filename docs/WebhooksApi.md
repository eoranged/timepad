# timepad.WebhooksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hook**](WebhooksApi.md#add_hook) | **POST** /v1/organizations/{organization_id}/hooks | Создать webhook для организации
[**edit_hook**](WebhooksApi.md#edit_hook) | **POST** /v1/organizations/{organization_id}/hooks/{hook_id} | Изменить webhook
[**get_hook**](WebhooksApi.md#get_hook) | **GET** /v1/organizations/{organization_id}/hooks/{hook_id} | Получить webhook по ID
[**get_hooks**](WebhooksApi.md#get_hooks) | **GET** /v1/organizations/{organization_id}/hooks | Получить список webhook&#x27;ов

# **add_hook**
> WebhooksApiResponse add_hook(organization_id, body=body)

Создать webhook для организации

Позволяет добавить новый webhook в организацию. Подробнее о системе хуков и ее использовании можно прочитать в статье http://dev.timepad.ru/api/hooks/

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: timepad_implicit
configuration = timepad.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = timepad.WebhooksApi(timepad.ApiClient(configuration))
organization_id = 56 # int | Идентификатор организации
body = timepad.CreateHook() # CreateHook | Описание добавляемого webhook'а (optional)

try:
    # Создать webhook для организации
    api_response = api_instance.add_hook(organization_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Идентификатор организации | 
 **body** | [**CreateHook**](CreateHook.md)| Описание добавляемого webhook&#x27;а | [optional] 

### Return type

[**WebhooksApiResponse**](WebhooksApiResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_hook**
> WebhookApiResponse edit_hook(organization_id, hook_id, body=body)

Изменить webhook

Позволяет изменить webhook в организации. Подробнее о системе хуков и ее использовании можно прочитать в статье http://dev.timepad.ru/api/hooks/

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: timepad_implicit
configuration = timepad.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = timepad.WebhooksApi(timepad.ApiClient(configuration))
organization_id = 56 # int | Идентификатор организации
hook_id = 56 # int | Идентификатор webhook'а
body = timepad.EditHook() # EditHook | Поля для обновления webhook'а (optional)

try:
    # Изменить webhook
    api_response = api_instance.edit_hook(organization_id, hook_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->edit_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Идентификатор организации | 
 **hook_id** | **int**| Идентификатор webhook&#x27;а | 
 **body** | [**EditHook**](EditHook.md)| Поля для обновления webhook&#x27;а | [optional] 

### Return type

[**WebhookApiResponse**](WebhookApiResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> WebhookApiResponse get_hook(organization_id, hook_id)

Получить webhook по ID

Позволяет получить информацию о добавленном для организации webhook'е. Подробнее о системе хуков и ее использовании можно прочитать в статье http://dev.timepad.ru/api/hooks/

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: timepad_implicit
configuration = timepad.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = timepad.WebhooksApi(timepad.ApiClient(configuration))
organization_id = 56 # int | Идентификатор организации
hook_id = 56 # int | Идентификатор webhook'а

try:
    # Получить webhook по ID
    api_response = api_instance.get_hook(organization_id, hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Идентификатор организации | 
 **hook_id** | **int**| Идентификатор webhook&#x27;а | 

### Return type

[**WebhookApiResponse**](WebhookApiResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hooks**
> WebhooksApiResponse get_hooks(organization_id, type=type)

Получить список webhook'ов

Позволяет получить список webhook'ов для указанной организации. Подробнее о системе хуков и ее использовании можно прочитать в статье http://dev.timepad.ru/api/hooks/

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: timepad_implicit
configuration = timepad.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = timepad.WebhooksApi(timepad.ApiClient(configuration))
organization_id = 56 # int | Идентификатор организации
type = 'type_example' # str | Тип получаемых webhook'ов (optional)

try:
    # Получить список webhook'ов
    api_response = api_instance.get_hooks(organization_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Идентификатор организации | 
 **type** | **str**| Тип получаемых webhook&#x27;ов | [optional] 

### Return type

[**WebhooksApiResponse**](WebhooksApiResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

