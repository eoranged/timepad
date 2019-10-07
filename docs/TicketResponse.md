# TicketResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный номер билета | 
**number** | **str** | Номер билета | [optional] 
**price_nominal** | **float** | Номинальная цена билета на момент покупки. ВНИМАНИЕ! Эта цена не учитывает начисленные скидки на заказ и является ценой заказанной категории билета на момент его оплаты. | [optional] 
**answers** | **dict(str, str)** | Объект с ответами на вопросы анкеты | 
**ticket_type** | [**TicketTypeResponse**](TicketTypeResponse.md) |  | 
**attendance** | [**AttendanceResponse**](AttendanceResponse.md) |  | [optional] 
**place** | [**PlaceResponse**](PlaceResponse.md) |  | [optional] 
**codes** | [**CodesResponse**](CodesResponse.md) |  | [optional] 
**personal_link** | **str** | Персональная ссылка | [optional] 
**eticket_link** | **str** | Ссылка на электронный билет | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

