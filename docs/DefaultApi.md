# timepad.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_event**](DefaultApi.md#add_event) | **POST** /v1/events | Создать событие
[**add_order**](DefaultApi.md#add_order) | **POST** /v1/events/{event_id}/orders | Создать заказ (deprecated)
[**add_organization**](DefaultApi.md#add_organization) | **POST** /v1/organizations | Создать организацию
[**approve_event_order**](DefaultApi.md#approve_event_order) | **PATCH** /v1/events/{event_id}/orders/{order_id}/approve | Подтвердить заказ
[**authorize**](DefaultApi.md#authorize) | **GET** /oauth/authorize | Получить токен для работы с API
[**call_custom_method**](DefaultApi.md#call_custom_method) | **POST** /v1/organizations/{organization_id}/custom_method/{method_name} | Вызвать кастомный метод
[**delete_event_order**](DefaultApi.md#delete_event_order) | **PATCH** /v1/events/{event_id}/orders/{order_id}/delete | Удалить заказ
[**edit_event**](DefaultApi.md#edit_event) | **POST** /v1/events/{event_id} | Изменить событие
[**edit_event_order**](DefaultApi.md#edit_event_order) | **PATCH** /v1/events/{event_id}/orders/{order_id} | Изменить заказ
[**get_event_orders**](DefaultApi.md#get_event_orders) | **GET** /v1/events/{event_id}/orders | Получить заказы события
[**get_events**](DefaultApi.md#get_events) | **GET** /v1/events | Получить список событий
[**get_events_categories**](DefaultApi.md#get_events_categories) | **GET** /v1/dictionary/event_categories | Получить список категорий событий
[**get_events_statuses**](DefaultApi.md#get_events_statuses) | **GET** /v1/dictionary/event_statuses | Получить список статусов событий
[**get_single_event**](DefaultApi.md#get_single_event) | **GET** /v1/events/{event_id} | Получить событие по ID
[**get_single_event_order**](DefaultApi.md#get_single_event_order) | **GET** /v1/events/{event_id}/orders/{order_id} | Получить заказ по ID
[**get_tickets_statuses**](DefaultApi.md#get_tickets_statuses) | **GET** /v1/dictionary/tickets_statuses | Получить список статусов билетов
[**introspect_token**](DefaultApi.md#introspect_token) | **GET** /introspect | Получить информацию о пользователе API
[**introspect_token_post**](DefaultApi.md#introspect_token_post) | **POST** /introspect | Получить информацию о пользователе API
[**reject_event_order**](DefaultApi.md#reject_event_order) | **PATCH** /v1/events/{event_id}/orders/{order_id}/reject | Отклонить заказ

# **add_event**
> EventResponse add_event(body=body)

Создать событие

События создаются только от имени организаций. У пользователя, вызывающего этот метод, должны быть права на администрированое данной организации.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
body = timepad.CreateEvent() # CreateEvent | Описание создаваемого события (optional)

try:
    # Создать событие
    api_response = api_instance.add_event(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEvent**](CreateEvent.md)| Описание создаваемого события | [optional] 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order**
> RegistrationOrderResponse add_order(event_id, body=body)

Создать заказ (deprecated)

Создает новый заказ для события. Это API более не предоставляется. В случае, если вас это напрямую затронуло, обратитесь в службу поддержки.

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()
event_id = 56 # int | Номер события
body = timepad.CreateOrder() # CreateOrder | Описание создаваемого заказа (optional)

try:
    # Создать заказ (deprecated)
    api_response = api_instance.add_order(event_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события | 
 **body** | [**CreateOrder**](CreateOrder.md)| Описание создаваемого заказа | [optional] 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization**
> OrganizationResponse add_organization(body=body)

Создать организацию

Создает новую организацию на TimePad.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
body = timepad.CreateOrganization() # CreateOrganization | Описание созданной организации (optional)

try:
    # Создать организацию
    api_response = api_instance.add_organization(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrganization**](CreateOrganization.md)| Описание созданной организации | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_event_order**
> RegistrationOrderResponse approve_event_order(event_id, order_id)

Подтвердить заказ

Устанавливает заказу статус - подтверждено

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относится заказ
order_id = 56 # int | Номер заказа

try:
    # Подтвердить заказ
    api_response = api_instance.approve_event_order(event_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->approve_event_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относится заказ | 
 **order_id** | **int**| Номер заказа | 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize**
> authorize(client_id=client_id, redirect_uri=redirect_uri, response_type=response_type, scope=scope)

Получить токен для работы с API

Функция в закрытом тестировании. Для получения client_id обращайтесь в службу поддержки. Корректное выполнение этого запроса перенаправит пользователя на форму логина

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()
client_id = 'client_id_example' # str | Идентификатор клиента (optional)
redirect_uri = 'redirect_uri_example' # str | Ссылка на которую произойдёт редирект (optional)
response_type = 'response_type_example' # str | Возвращаемый тип ответа. Единственное поддерживаемое значение - token (optional)
scope = ['scope_example'] # list[str] | Запрашиваемые приложением разрешения через запятую. Возможные значения: add_events, add_organizations, edit_events, view_private_events, view_visitors, edit_visitors, add_cash_payments, edit_organizations_hooks (optional)

try:
    # Получить токен для работы с API
    api_instance.authorize(client_id=client_id, redirect_uri=redirect_uri, response_type=response_type, scope=scope)
except ApiException as e:
    print("Exception when calling DefaultApi->authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Идентификатор клиента | [optional] 
 **redirect_uri** | **str**| Ссылка на которую произойдёт редирект | [optional] 
 **response_type** | **str**| Возвращаемый тип ответа. Единственное поддерживаемое значение - token | [optional] 
 **scope** | [**list[str]**](str.md)| Запрашиваемые приложением разрешения через запятую. Возможные значения: add_events, add_organizations, edit_events, view_private_events, view_visitors, edit_visitors, add_cash_payments, edit_organizations_hooks | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_custom_method**
> CustomMethodApiResponse call_custom_method(organization_id, method_name, body=body)

Вызвать кастомный метод

Вызывает кастомный метод, определенный специально для вашей организации

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
organization_id = 56 # int | Идентификатор организации
method_name = 'method_name_example' # str | Название кастомного метода
body = timepad.CallCustomMethod() # CallCustomMethod | Дополнительные параметры, передаваемые методу (optional)

try:
    # Вызвать кастомный метод
    api_response = api_instance.call_custom_method(organization_id, method_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->call_custom_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Идентификатор организации | 
 **method_name** | **str**| Название кастомного метода | 
 **body** | [**CallCustomMethod**](CallCustomMethod.md)| Дополнительные параметры, передаваемые методу | [optional] 

### Return type

[**CustomMethodApiResponse**](CustomMethodApiResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_order**
> RegistrationOrderResponse delete_event_order(event_id, order_id)

Удалить заказ

Устанавливает заказу статус - удалено

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относится заказ
order_id = 56 # int | Номер заказа

try:
    # Удалить заказ
    api_response = api_instance.delete_event_order(event_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_event_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относится заказ | 
 **order_id** | **int**| Номер заказа | 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_event**
> EventResponse edit_event(event_id, body=body)

Изменить событие

Для того, чтобы редактировать события, вам нужно вызывать метод от имени пользователя, обладающего административным доступом к организации, в котором событие было создано.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер редактируемого события
body = timepad.EditEvent() # EditEvent | Список изменённых параметров события (optional)

try:
    # Изменить событие
    api_response = api_instance.edit_event(event_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер редактируемого события | 
 **body** | [**EditEvent**](EditEvent.md)| Список изменённых параметров события | [optional] 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_event_order**
> RegistrationOrderResponse edit_event_order(event_id, order_id, body=body)

Изменить заказ

Изменяет состав заказа. Этот метод позволяет только изменить ответы на вопросы анкеты регистрации, пометить билеты в заказе как прошедшие контроль доступа или пометить билеты в заказе как оплаченные оффлайн. Менять состав билетов в заказе, параметры платежа, скидок и так далее данный метод не дает.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относится заказ
order_id = 56 # int | Номер заказа
body = timepad.EditOrder() # EditOrder | Список изменённых параметров заказа (optional)

try:
    # Изменить заказ
    api_response = api_instance.edit_event_order(event_id, order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_event_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относится заказ | 
 **order_id** | **int**| Номер заказа | 
 **body** | [**EditOrder**](EditOrder.md)| Список изменённых параметров заказа | [optional] 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_orders**
> RegistrationOrdersResponse get_event_orders(event_id, limit=limit, skip=skip, email=email, fields=fields)

Получить заказы события

Метод возвращает список заказов. Внимание! Это не выгрузка списка билетов, это именно выгрузка списка заказов. Информация по конкретным билетам находится внутри объекта заказа.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относятся заказы
limit = 56 # int | Сколько элементов списка вывести (optional)
skip = 56 # int | С какого элемента списка начать вывод (optional)
email = 'email_example' # str | email пользователя (optional)
fields = ['fields_example'] # list[str] | Список полей, которые нужно вывести (optional)

try:
    # Получить заказы события
    api_response = api_instance.get_event_orders(event_id, limit=limit, skip=skip, email=email, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относятся заказы | 
 **limit** | **int**| Сколько элементов списка вывести | [optional] 
 **skip** | **int**| С какого элемента списка начать вывод | [optional] 
 **email** | **str**| email пользователя | [optional] 
 **fields** | [**list[str]**](str.md)| Список полей, которые нужно вывести | [optional] 

### Return type

[**RegistrationOrdersResponse**](RegistrationOrdersResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventsResponse get_events(fields=fields, limit=limit, skip=skip, sort=sort, category_ids=category_ids, category_ids_exclude=category_ids_exclude, cities=cities, cities_exclude=cities_exclude, organization_ids=organization_ids, organization_ids_exclude=organization_ids_exclude, event_ids=event_ids, event_ids_exclude=event_ids_exclude, keywords=keywords, keywords_exclude=keywords_exclude, access_statuses=access_statuses, moderation_statuses=moderation_statuses, price_min=price_min, price_max=price_max, ad_partner_percent_min=ad_partner_percent_min, ad_partner_percent_max=ad_partner_percent_max, ad_partner_profit_min=ad_partner_profit_min, ad_partner_profit_max=ad_partner_profit_max, starts_at_min=starts_at_min, starts_at_max=starts_at_max, created_at_min=created_at_min, created_at_max=created_at_max)

Получить список событий

Получение публичной информации о событиях не требует аутентификации. Количество запросов в минуту ограничено.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Список полей, которые нужно вывести (optional)
limit = 56 # int | Сколько элементов списка вывести (optional)
skip = 56 # int | С какого элемента списка начать вывод (optional)
sort = ['sort_example'] # list[str] | Поле, по которому сортировать (optional)
category_ids = [56] # list[int] | Категории, к которым принадлежат события (optional)
category_ids_exclude = [56] # list[int] | Категории, к которым не принадлежат события (optional)
cities = ['cities_example'] # list[str] | Города, события из которых выводить (optional)
cities_exclude = ['cities_exclude_example'] # list[str] | Города, события из которых не выводить (optional)
organization_ids = [56] # list[int] | Номера организаций, события из которых выводить (optional)
organization_ids_exclude = [56] # list[int] | Номера организаций, события из которых не выводить (optional)
event_ids = [56] # list[int] | Номера событий, которые нужно вывести (optional)
event_ids_exclude = [56] # list[int] | Номера событий, которые нужно пропустить (optional)
keywords = ['keywords_example'] # list[str] | Слова, которые должны быть в названии или описании события (optional)
keywords_exclude = ['keywords_exclude_example'] # list[str] | Слова, которых не должно быть в названии или описании события (optional)
access_statuses = ['access_statuses_example'] # list[str] | Список режимов доступа, в которых находятся события. Возможные значения: private, draft, link_only, public. Доступно только организаторам (optional)
moderation_statuses = ['moderation_statuses_example'] # list[str] | Список уровней качества, установленных для события модератором. Возможные значения: featured, shown, hidden, not_moderated. (optional)
price_min = 56 # int | Цена, выше которой должен стоить хотя бы один билет события (optional)
price_max = 56 # int | Цена, ниже которой должен стоить хотя бы один билет события (optional)
ad_partner_percent_min = 56 # int | Хотя бы у одного вида билета события партнёрская комиссия в процентах выше этого значения (optional)
ad_partner_percent_max = 56 # int | Хотя бы у одного вида билета партнёрская комиссия в процентах ниже этого значения (optional)
ad_partner_profit_min = 56 # int | Хотя бы у одного вида билета партнёрская комиссия в рублях выше этого значения (optional)
ad_partner_profit_max = 56 # int | Хотя бы у одного вида билета партнёрская комиссия в рублях ниже этого значения (optional)
starts_at_min = '2013-10-20T19:20:30+01:00' # datetime | Дата начала события позднее этого значения (optional)
starts_at_max = '2013-10-20T19:20:30+01:00' # datetime | Дата начала события раньше этого значения (optional)
created_at_min = '2013-10-20T19:20:30+01:00' # datetime | Дата создания события на Timepad позднее этого значения (optional)
created_at_max = '2013-10-20T19:20:30+01:00' # datetime | Дата создания события на Timepad раньше этого значения (optional)

try:
    # Получить список событий
    api_response = api_instance.get_events(fields=fields, limit=limit, skip=skip, sort=sort, category_ids=category_ids, category_ids_exclude=category_ids_exclude, cities=cities, cities_exclude=cities_exclude, organization_ids=organization_ids, organization_ids_exclude=organization_ids_exclude, event_ids=event_ids, event_ids_exclude=event_ids_exclude, keywords=keywords, keywords_exclude=keywords_exclude, access_statuses=access_statuses, moderation_statuses=moderation_statuses, price_min=price_min, price_max=price_max, ad_partner_percent_min=ad_partner_percent_min, ad_partner_percent_max=ad_partner_percent_max, ad_partner_profit_min=ad_partner_profit_min, ad_partner_profit_max=ad_partner_profit_max, starts_at_min=starts_at_min, starts_at_max=starts_at_max, created_at_min=created_at_min, created_at_max=created_at_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Список полей, которые нужно вывести | [optional] 
 **limit** | **int**| Сколько элементов списка вывести | [optional] 
 **skip** | **int**| С какого элемента списка начать вывод | [optional] 
 **sort** | [**list[str]**](str.md)| Поле, по которому сортировать | [optional] 
 **category_ids** | [**list[int]**](int.md)| Категории, к которым принадлежат события | [optional] 
 **category_ids_exclude** | [**list[int]**](int.md)| Категории, к которым не принадлежат события | [optional] 
 **cities** | [**list[str]**](str.md)| Города, события из которых выводить | [optional] 
 **cities_exclude** | [**list[str]**](str.md)| Города, события из которых не выводить | [optional] 
 **organization_ids** | [**list[int]**](int.md)| Номера организаций, события из которых выводить | [optional] 
 **organization_ids_exclude** | [**list[int]**](int.md)| Номера организаций, события из которых не выводить | [optional] 
 **event_ids** | [**list[int]**](int.md)| Номера событий, которые нужно вывести | [optional] 
 **event_ids_exclude** | [**list[int]**](int.md)| Номера событий, которые нужно пропустить | [optional] 
 **keywords** | [**list[str]**](str.md)| Слова, которые должны быть в названии или описании события | [optional] 
 **keywords_exclude** | [**list[str]**](str.md)| Слова, которых не должно быть в названии или описании события | [optional] 
 **access_statuses** | [**list[str]**](str.md)| Список режимов доступа, в которых находятся события. Возможные значения: private, draft, link_only, public. Доступно только организаторам | [optional] 
 **moderation_statuses** | [**list[str]**](str.md)| Список уровней качества, установленных для события модератором. Возможные значения: featured, shown, hidden, not_moderated. | [optional] 
 **price_min** | **int**| Цена, выше которой должен стоить хотя бы один билет события | [optional] 
 **price_max** | **int**| Цена, ниже которой должен стоить хотя бы один билет события | [optional] 
 **ad_partner_percent_min** | **int**| Хотя бы у одного вида билета события партнёрская комиссия в процентах выше этого значения | [optional] 
 **ad_partner_percent_max** | **int**| Хотя бы у одного вида билета партнёрская комиссия в процентах ниже этого значения | [optional] 
 **ad_partner_profit_min** | **int**| Хотя бы у одного вида билета партнёрская комиссия в рублях выше этого значения | [optional] 
 **ad_partner_profit_max** | **int**| Хотя бы у одного вида билета партнёрская комиссия в рублях ниже этого значения | [optional] 
 **starts_at_min** | **datetime**| Дата начала события позднее этого значения | [optional] 
 **starts_at_max** | **datetime**| Дата начала события раньше этого значения | [optional] 
 **created_at_min** | **datetime**| Дата создания события на Timepad позднее этого значения | [optional] 
 **created_at_max** | **datetime**| Дата создания события на Timepad раньше этого значения | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_categories**
> EventsCategoriesApiResponse get_events_categories()

Получить список категорий событий

Получает список категорий событий

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()

try:
    # Получить список категорий событий
    api_response = api_instance.get_events_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_events_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventsCategoriesApiResponse**](EventsCategoriesApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_statuses**
> EventsStatusesApiResponse get_events_statuses()

Получить список статусов событий

Получает список статусов событий

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()

try:
    # Получить список статусов событий
    api_response = api_instance.get_events_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_events_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventsStatusesApiResponse**](EventsStatusesApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_event**
> EventResponse get_single_event(event_id, fields=fields)

Получить событие по ID

Получение полной информации по событию. С помощью параметра fields можно регулировать набор полей, который вернет метод.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, которые нужно вывести
fields = ['fields_example'] # list[str] | Список полей, которые нужно вывести (optional)

try:
    # Получить событие по ID
    api_response = api_instance.get_single_event(event_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_single_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, которые нужно вывести | 
 **fields** | [**list[str]**](str.md)| Список полей, которые нужно вывести | [optional] 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_event_order**
> RegistrationOrderResponse get_single_event_order(event_id, order_id, fields=fields)

Получить заказ по ID

Получает заказ по его ID. Обращаем внимание, что номер на билете - это ID билета, а не заказа.

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относится заказ
order_id = 56 # int | Номер заказа
fields = ['fields_example'] # list[str] | Список полей, которые нужно вывести (optional)

try:
    # Получить заказ по ID
    api_response = api_instance.get_single_event_order(event_id, order_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_single_event_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относится заказ | 
 **order_id** | **int**| Номер заказа | 
 **fields** | [**list[str]**](str.md)| Список полей, которые нужно вывести | [optional] 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets_statuses**
> TicketsStatusesApiResponse get_tickets_statuses()

Получить список статусов билетов

Получает список статусов билетов

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()

try:
    # Получить список статусов билетов
    api_response = api_instance.get_tickets_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tickets_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TicketsStatusesApiResponse**](TicketsStatusesApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_token**
> Introspect introspect_token(token=token)

Получить информацию о пользователе API

Получить информацию о токене соответственно стандарту ietf-oauth-introspection

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()
token = 'token_example' # str | Идентификатор токена (optional)

try:
    # Получить информацию о пользователе API
    api_response = api_instance.introspect_token(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->introspect_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Идентификатор токена | [optional] 

### Return type

[**Introspect**](Introspect.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_token_post**
> Introspect introspect_token_post(token=token)

Получить информацию о пользователе API

Получить информацию о токене соответственно стандарту ietf-oauth-introspection. Аналогичен методу 'GET /introspect', но может быть использован в том случае, когда нужно по каким-либо причинам скрыть проверяемый токен.

### Example
```python
from __future__ import print_function
import time
import timepad
from timepad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timepad.DefaultApi()
token = 'token_example' # str |  (optional)

try:
    # Получить информацию о пользователе API
    api_response = api_instance.introspect_token_post(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->introspect_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**Introspect**](Introspect.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_event_order**
> RegistrationOrderResponse reject_event_order(event_id, order_id)

Отклонить заказ

Устанавливает заказу статус - отклонено

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
api_instance = timepad.DefaultApi(timepad.ApiClient(configuration))
event_id = 56 # int | Номер события, к которому относится заказ
order_id = 56 # int | Номер заказа

try:
    # Отклонить заказ
    api_response = api_instance.reject_event_order(event_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reject_event_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Номер события, к которому относится заказ | 
 **order_id** | **int**| Номер заказа | 

### Return type

[**RegistrationOrderResponse**](RegistrationOrderResponse.md)

### Authorization

[timepad_implicit](../README.md#timepad_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

