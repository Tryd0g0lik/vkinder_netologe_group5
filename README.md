## Требования
 - Создать группу в Вконтакте, от имени которой будет общаться разрабатываемый бот.
[Как настроить группу для бота и получить токен](https://github.com/netology-code/adpy-team-diplom/blob/main/group_settings.md)


 - Создать кнопки в чате для взаимодействия с ботом.
 - бот и все части кода объединены в главной ветке (master/main).


 - Результат программы записывается в БД.
 - Количество таблиц должно быть не меньше трех.
 - Приложить схему БД.


 - Программа декомпозирована на функции/классы/модули/пакеты.
 - Написана документация по использованию программы


 - Код программы удовлетворяет PEP8
> Перед отправкой решения на проверку проверьте код с помощью линтеров.

## db

**db - Модель БД** 

**Users** - таблица пользователей начавших разговор с Ботом (далее рег-пользователь)
>
> Users.id - ID-пользователя начавшего общение с БД
>
> Users.token - уникальный идентификатор планируется добавить позже в данный момент = ID-пользователя

**Elected_users** - таблица избранных пользователей относительно рег-пользователя
> Elected_users.id_user - id рег-пользователя
>
> Elected_users.id_elected_user - id избранного пользователя
>
> Elected_users.id_list - id листа для которого избран пользователь по отношению к рег-пользователю

**Lists** - таблица листов (избранный, черный)
> Lists.id - уникальный идентификатор
>
> Lists.name - наименование листа
>
> List.desc - описание листа

**Filters** - таблица фильтров для ведения поиска
> Filters.id - уникальный идентификатор
>
> Filsers.code_filter - код фильтра, соответствует названию фильтров из API VK

**Search_values** - таблица поисковых значений для рег-пользователя
> Search_values.id_user - id рег-пользователя
>
> Search_values.id_filter - id фильтра поиска
>
> Search_values.value - значение поиска

**LastMessages** - таблица последних отправленных сообщений от бота, для того чтоб при рестарте для зачистки последнего сообщения
> LastMessages.id - уникальный идентификатор строки
>
> LastMessages.id_user - id-пользователя полученных сообщений от бота
>
> LastMessages.id_message - id-сообщения
>
> LastMessages.offset - поле со сдвигом по листингу поиска. В дальнейшем планировалось для того чтоб правильно определять положение в поиске

## .env

**.env - Настройка окружения** 
>Переименуйте файл c настройками .env_example -> .env и настройте задайте ваши параметры
> 
>DSN=postgresql://postgres:password@localhost:5432/BOT_DB - подключение к БД
>
>TOKEN_BOT=8b6d106...b4585c - Токен полученный при создании бота
>
>GROUP_ID=21...1 - ID вашей группы в контакте
>
>TOKEN_API_VK=vk1.a.PwtBfYyVT...mZ - токен доступа для работы с API VK


### Цель проекта
**Разработать программу-бота** для взаимодействия с людьми, с целью:
 - знакомств в социальной сети Вконтакте. 
 - и диалог с пользователем.

**Свойства бота**
 - знать (возраст, пол, город) о пользователе, который общается с ботом.


 - бот осуществляет поиск других людей (пользователей ВК).
 - максимальная выдача при поиске - 1000 человек.


 - получить три самые популярные, по количеству лайков, фотографии из профиля найденого в результатах поиска.


 - Выводить в чат с ботом информацию о пользователе в формате
 > Имя
 > 
 > Фамилия 
 > 
 > Cсылка на профиль три фотографии в виде attachment(https://dev.vk.com/method/messages.send)

 - Иметь команды или кнопки для перехода к следующему человеку.
 - Сохранить пользователя(лей) в список избранных.
> добавлять человека в избранный список используя БД
 - Вывести список избранных людей

#### Дополнительные требования (необязательные )
 - Получать токен от пользователя с нужными правами
 - Добавлять в чёрный список, чтобы он больше не попадался при поиске, используя БД.
 - Возможность ставить/убирать лайк выбранной фотографии.
 - К списку фотографий из аватарок добавлять список фотографий, где отмечен пользователь.
 - добавив поиск по интересам.
>Разбор похожих интересов (группы, книги, музыка, интересы) нужно будет провести с помощью анализа текста.

 - У каждого критерия поиска должен быть свой вес
> то есть совпадение по возрасту должно быть важнее общих групп, интересы по музыке - важнее книг, наличие общих друзей - важнее возраста и т.д.


