# QuestionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **int** | Уникальный текстовый идентификатор вопроса | 
**name** | **str** | Текст вопроса | 
**comment** | **str** | Подсказка под вопросом | [optional] 
**type** | **str** | Тип вопроса | 
**possible_answers** | [**list[AnswerResponse]**](AnswerResponse.md) | Список предлагаемых ответов (если вопрос предполагает такой список) | 
**is_mandatory** | **bool** | Является ли ответ на вопрос обязательным | 
**is_for_every_visitor** | **bool** | Выводить вопрос отдельно для каждого купленного билета | 
**meta** | **object** | Дополнительные данные | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

