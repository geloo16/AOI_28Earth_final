import data
import sender_stand_request

# Создание заказа, получение номера трека в переменную, возврат статус кода заказа по треку
def positive_assert_200():
	response = sender_stand_request.post_new_order(data.order_body)
	track = response.json()["track"]
	return sender_stand_request.get_order_from_track(track).status_code

# Проверка статус кода == 200
def test_get_order_from_track():
	assert positive_assert_200() == 200

# Александров Олег, 28 Earth, Дипломный проект. Инженер по тестированию +