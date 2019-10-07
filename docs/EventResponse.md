# EventResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный номер события | 
**created_at** | **date** | Дата создания события | [optional] 
**starts_at** | **date** | Дата начала события | 
**ends_at** | **date** | Дата конца события | [optional] 
**name** | **str** | Название события | 
**description_short** | **str** | Короткое описание события или подзаголовок | [optional] 
**description_html** | **str** | Полное описание события | [optional] 
**url** | **str** | Адрес события в timepad | 
**poster_image** | [**ImageResponse**](ImageResponse.md) |  | 
**ad_partner_percent** | **int** | Процент, который получают партнёры за продажу билета на это событие | [optional] 
**locale** | **str** | Язык события по умолчанию | [optional] 
**location** | [**LocationResponse**](LocationResponse.md) |  | [optional] 
**organization** | [**OrganizationResponse**](OrganizationResponse.md) |  | [optional] 
**categories** | [**list[CategoryResponse]**](CategoryResponse.md) | Категории события | 
**tickets_limit** | **int** | Максимальное количество человек, которые могут посетить событие | [optional] 
**ticket_types** | [**list[TicketTypeResponse]**](TicketTypeResponse.md) | Доступные типы билетов | [optional] 
**personal_links** | **list[str]** | Персональные ссылки. Доступно только при указании токена со разрешением view_private_events | [optional] 
**questions** | [**list[QuestionResponse]**](QuestionResponse.md) | Вопросы, задающиеся при регистрации | [optional] 
**age_limit** | **str** | Возрастное ограничение события | [optional] 
**widgets** | [**list[WidgetResponse]**](WidgetResponse.md) | Виджеты, доступные для события | [optional] 
**properties** | **list[str]** | Список особенностей события | [optional] 
**moderation_status** | **str** | Статус модерации | 
**access_status** | **str** | Статус доступа к событию | [optional] 
**registration_data** | [**RegistrationDataResponse**](RegistrationDataResponse.md) |  | [optional] 
**is_sending_free_tickets** | **bool** | Отправлять билеты на бесплатные регистрации | [optional] 
**personal_link_title** | **str** | Заголовок персональной ссылки. Доступно только при указании токена со разрешением view_private_events | [optional] 
**reservation_period** | **int** | Срок брони билета в часах. Нулевое значение соответствует неограниченному сроку | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

