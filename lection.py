# HTTP (HyperText Transfer Protocol) - протокол передачи гипертекстовой 
# информатции стал универсальным средством взаимодействия между узлами 
# в WWW(Всемирная паутина)

# Клиент <-> сервер

# Структура HTTP

# Стартовая строка (линия) -> определяет какое сообшение мы получили
#  Запрос : GET /wiki/HTTPS HTTP/1.0
#  Ответ  : HTTP/1.0 200 OK
#           HTTP/1.0 404 NOT Found
# User-Agent: Chrome /13/2
# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
#     'AppleWebKit/537.11 (KHTML, like Gecko) '
#     'Chrome/23.0.1271.64 Safari/537.11',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'none',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Connection': 'keep-alive'
# }

# 3. Тело сообшения (boat Body) - непосредсвенно данные запроса либо ответа
# {
#     'comment': 'GOAT BEST!'
# }

# Методы запроса -> 1. GET(для получения данных)
#                   2.POST(для создания данных)
#                   3.PUT(для полного обновления данных)
#                   4.PATCH(Для частичного обновления)
#                   5.DELETE(для удаления данных)

# Статусы Ответа
# 1XXX - Информатционные
# 2XXX - Запрос так или иначе прошел успешно
# 3XXX - перенаправление
# 4XXX - Ошибки на стороне клиента
# 5XXX - Ошибки на стороне серевера

