import requests
import configuration
import data

# Функция для создания нового заказа
def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)
    
# Функция для получения заказа по треку (переводим трек в строку для формирования url)
def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_PATH + str(track), 
	                    headers = data.headers)

