# TicketTypeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный номер типа билета | 
**name** | **str** | Название типа билета | 
**description** | **str** | Описание типа билета | [optional] 
**buy_amount_min** | **float** | Минимальное количество билетов в одной покупке | 
**buy_amount_max** | **float** | Максимальное количество билетов в одной покупке | 
**price** | **float** | Цена билета | 
**is_promocode_locked** | **bool** | Закрыт ли этот тип билета введённым промокодом | 
**remaining** | **int** | Сколько билетов осталось | 
**sale_ends_at** | **date** | Дата окончания продажи типа билета | 
**sale_starts_at** | **date** | Дата начала продажи типа билета | [optional] 
**public_key** | **str** | Публичный ключ для расшифровки QR-кода билета этого типа | 
**is_active** | **bool** | Активность типа билета | 
**ad_partner_profit** | **float** | Партнёрская прибыль | [optional] 
**send_personal_links** | **bool** | Отправка персональных сссылок | [optional] 
**sold** | **float** | Количество проданных билетов | [optional] 
**attended** | **float** | Количество посетивших людей | [optional] 
**limit** | **float** | Ограничение на количество билетов в этом типе билета | [optional] 
**status** | **str** | Статус типа билета | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

