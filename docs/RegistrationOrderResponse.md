# RegistrationOrderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный номер заказа | 
**created_at** | **date** | Дата создания заказа | 
**status** | [**OrderStatusResponse**](OrderStatusResponse.md) |  | 
**mail** | **str** | Адрес электронной почты заказчика билетов. Если режим регистрации на ваше событие находится в положении &amp;laquo;Простая регистрация&amp;raquo; или &amp;laquo;Мультирегистрация&amp;raquo;, здесь будет находиться адрес электронной почты из поля &amp;laquo;E-mail&amp;raquo; формы покупки билетов. Если режим регистрации выставлен как &amp;laquo;Мультианкета&amp;raquo;, то здесь будет находится адрес электронной почты первого участника. В некоторых случаях, когда форма регистрации настроена на отображение отдельной формы заказчика, в этом поле будет находится адрес электронной почты из этой формы. | [optional] 
**payment** | [**PaymentResponse**](PaymentResponse.md) |  | [optional] 
**tickets** | [**list[TicketResponse]**](TicketResponse.md) | Список регистраций | 
**answers** | **dict(str, str)** | Массив Ответов | 
**promocodes** | **list[str]** | Список промокодов | [optional] 
**event** | [**OrderEventResponse**](OrderEventResponse.md) |  | [optional] 
**referrer** | [**OrderReferrerResponse**](OrderReferrerResponse.md) |  | [optional] 
**subscribed_to_newsletter** | **bool** | Подписка на анонсы событий организатора | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

