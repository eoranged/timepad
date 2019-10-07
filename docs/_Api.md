# timepad._Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_companies_list**](_Api.md#event_companies_list) | **GET** /v1/events/{event_id}/companies | Получить список реквизитов компаний
[**event_company**](_Api.md#event_company) | **GET** /v1/events/{event_id}/companies/{company_id} | Получить реквизиты юрлица по ID
[**event_company_payments**](_Api.md#event_company_payments) | **GET** /v1/events/{event_id}/company_payment_requests | Получить запросы на оплату от юрлица
[**event_company_payments_0**](_Api.md#event_company_payments_0) | **GET** /v1/events/{event_id}/company_payment_requests/{company_payment_request_id} | Получить запросы на оплату от юрлица по ID
[**event_company_payments_1**](_Api.md#event_company_payments_1) | **GET** /v1/events/{event_id}/invoices | Получить выставленные счета
[**event_company_payments_2**](_Api.md#event_company_payments_2) | **GET** /v1/events/{event_id}/invoices/{invoice_id} | Получить счет по ID

# **event_companies_list**
> CompaniesResponse event_companies_list(event_id, limit=limit, skip=skip)

Получить список реквизитов компаний

Список реквизитов юридических лиц, которые запросили счет для оплаты заказов от юрлица. Доступно только организаторам с доступом к финансовой информации.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
limit = 56 # int | Сколько элементов списка вывести (optional)
skip = 56 # int | С какого элемента списка начать вывод (optional)

try:
    # Получить список реквизитов компаний
    api_response = api_instance.event_companies_list(event_id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_companies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **limit** | **int**| Сколько элементов списка вывести | [optional] 
 **skip** | **int**| С какого элемента списка начать вывод | [optional] 

### Return type

[**CompaniesResponse**](CompaniesResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_company**
> CompanyResponse event_company(event_id, company_id)

Получить реквизиты юрлица по ID

Реквизиты юридического лица, запросившего счет для оплаты заказа от юрлица. Доступно только организаторам с доступом к финансовой информации.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
company_id = 56 # int | Номер реквизитов

try:
    # Получить реквизиты юрлица по ID
    api_response = api_instance.event_company(event_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **company_id** | **int**| Номер реквизитов | 

### Return type

[**CompanyResponse**](CompanyResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_company_payments**
> CompanyPaymentRequestsResponse event_company_payments(event_id, limit=limit, skip=skip)

Получить запросы на оплату от юрлица

Список запросов на оплату заказов от юрлица. Доступно только организаторам с доступом к финансовой информации.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
limit = 56 # int | Сколько элементов списка вывести (optional)
skip = 56 # int | С какого элемента списка начать вывод (optional)

try:
    # Получить запросы на оплату от юрлица
    api_response = api_instance.event_company_payments(event_id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_company_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **limit** | **int**| Сколько элементов списка вывести | [optional] 
 **skip** | **int**| С какого элемента списка начать вывод | [optional] 

### Return type

[**CompanyPaymentRequestsResponse**](CompanyPaymentRequestsResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_company_payments_0**
> CompanyPaymentRequestResponse event_company_payments_0(event_id, company_payment_request_id)

Получить запросы на оплату от юрлица по ID

Информация о запросе на оплату заказа от конкретного юрлица. Одно юрлицо может подать несколько разных запросов на оплату одного и того же события. Список заказов, которые привязаны к запросу не детерминированный, т.е. это догадка системы о том, какие именно заказы оплачиваются данным запросом. В реальности эти заказы могуть быть другими. Доступно только организаторам с доступом к финансовой информации.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
company_payment_request_id = 56 # int | Номер реквизитов компании

try:
    # Получить запросы на оплату от юрлица по ID
    api_response = api_instance.event_company_payments_0(event_id, company_payment_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_company_payments_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **company_payment_request_id** | **int**| Номер реквизитов компании | 

### Return type

[**CompanyPaymentRequestResponse**](CompanyPaymentRequestResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_company_payments_1**
> InvoicesResponse event_company_payments_1(event_id, limit=limit, skip=skip)

Получить выставленные счета

Метод возвращает список выставленных счетов в ответ на запросы компаний об оплате заказов от юрлиц. Метод доступен только организаторам с доступом к финансовой информации.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
limit = 56 # int | Сколько элементов списка вывести (optional)
skip = 56 # int | С какого элемента списка начать вывод (optional)

try:
    # Получить выставленные счета
    api_response = api_instance.event_company_payments_1(event_id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_company_payments_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **limit** | **int**| Сколько элементов списка вывести | [optional] 
 **skip** | **int**| С какого элемента списка начать вывод | [optional] 

### Return type

[**InvoicesResponse**](InvoicesResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_company_payments_2**
> InvoiceResponse event_company_payments_2(event_id, invoice_id)

Получить счет по ID

Метод возвращает информацию о выставленном счете для оплаты от юрлица.

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
api_instance = timepad._Api(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события
invoice_id = 56 # int | Номер счета

try:
    # Получить счет по ID
    api_response = api_instance.event_company_payments_2(event_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->event_company_payments_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **invoice_id** | **int**| Номер счета | 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

