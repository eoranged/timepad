# InvoiceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный номер платежа | 
**company_payment_request_id** | **int** | Номер запроса оплаты компанией | 
**invoice_num** | **int** | Номер платёжного документа | 
**tickets_count** | **int** | Количество билетов | 
**amount** | **float** | Сумма платежа | 
**amount_in_words** | **str** | Сумма платежа словами | [optional] 
**status** | **str** | Статус платежа | [optional] 
**orders** | **list[int]** | Номера заказов | [optional] 
**created_at** | **str** | Дата создания платежа | [optional] 
**paid_at** | **str** | Дата оплаты платежа | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

