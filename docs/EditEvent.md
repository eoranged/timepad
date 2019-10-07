# EditEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_types** | [**list[TicketTypeRequest]**](TicketTypeRequest.md) | Список видов билетов | [optional] 
**name** | **str** | Название события | [optional] 
**description_short** | **str** | Краткое описание/подзаголовок события | [optional] 
**description_html** | **str** | Полное описание с html-тегами | [optional] 
**starts_at** | **str** | Дата начала события в формате ISO | [optional] 
**ends_at** | **str** | Дата окончания события в формате ISO | [optional] 
**categories** | [**list[CategoryInclude]**](CategoryInclude.md) | Список категорий, в которые входит событие | [optional] 
**location** | [**LocationInclude**](LocationInclude.md) |  | [optional] 
**poster_image_url** | **str** | URL картинки события | [optional] 
**properties** | **list[str]** | Список настроек события (например, мультианкета) | [optional] 
**custom** | **object** | Объект с дополнительными полями, специфичными для данной организации | [optional] 
**questions** | [**list[QuestionInclude]**](QuestionInclude.md) | Список вопросов в анкете регистрации | [optional] 
**access_status** | **str** | Статус доступа к событию | [optional] 
**age_limit** | **str** | Возрастное ограничение события | [optional] 
**tickets_limit** | **int** | Максимальное количество человек, которые могут посетить событие. При достижении этого количества регистрация на событие закроется, даже если будут открытыми категории регистрации. Поставьте 0, чтобы снять ограничение. Учитывается количество как оплаченных, так и забронированных билетов. | [optional] 
**personal_links** | **list[str]** | Список персональных ссылок для билетов | [optional] 
**personal_link_title** | **bool** | Заголовок персональной ссылки (Например: Ваша ссылка на онлайн-трансляцию) | [optional] 
**is_sending_free_tickets** | **bool** | Отправлять билеты на бесплатные регистрации | [optional] 
**reservation_period** | **int** | Срок брони билета в часах. Нулевое значение соответствует неограниченному сроку | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

