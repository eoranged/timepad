# Introspect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Действует ли этот токен | 
**client_id** | **str** | Идентификатор клиента API, которым получен токен | 
**user_id** | **str** | Идентификатор пользователя, которым получен токен | 
**user_email** | **str** | Электронная почта пользователя, которым получен токен | 
**organizations** | [**list[OrganizationResponse]**](OrganizationResponse.md) | Организации, к которым есть доступ у пользователя | 
**orders** | [**list[RegistrationOrderResponse]**](RegistrationOrderResponse.md) | Заказы, которые пользователь сделал в системе | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

