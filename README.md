#### Hello World

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

**db - Пользовательский профиль имеет** 
 - Имя, Псевдоним, 
 - email, (обязательно, без права изменений),
 - один телефон (не обязательно).
 - возраст по умолчанию 18 лет.
 - пол (не обязательно).
 - право быть только в одной стране и в одном городе, но в стране может быть много городов и в одном городе может 
   быть много пользователей.
 - только один уникальный токен.


 - галерею уникальных фотографий (png, jpg, gif). Пользователь может иметь много фотографий и фотографии могут 
   находится у многих пользователей имея определенный статус. 
> default - фотография из галлереи пользователя
> 
> faivorite - фотография из preview (аватарка) пользователя
> 
> favourite - статус фотографии после лайка и профиля (в избранном) у другого пользователя
> 
> blacklist - статус профиля (в черном списке) у другого пользователя
> 
> delete  - фотографию/профиль удалить
  - Каждая фотография имеет лайки (like) , по умолчанию ноль.



### Цель проекта
**Разработать программу-бота** для взаимодействия с людьми, с целью:
 - знакомств в социальной сети Вконтакте. 
 - и диалог с пользователем.

**Свойства бота**
 - знать (возраст, пол, город) о пользователе, который общается с ботом.


 - бот осуществляет поиск других людей (пользователей ВК).
 - максимальная выдача при поиске - 1000 человек.


 - получить три самые популярные, по количеству лайков, фотографии из профиля найденого в результатах поиска.


 - Выводить в чат с ботом информацию о пользователе в формате (**Вопрос**. _если пользователей несколько то всех 
   выводить?_)
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
 - Получать токен от пользователя с нужными правами (**Вопрос**. _На что получить права?_)
 - Добавлять в чёрный список, чтобы он больше не попадался при поиске, используя БД.
 - Возможность ставить/убирать лайк выбранной фотографии.
 - К списку фотографий из аватарок добавлять список фотографий, где отмечен пользователь.
 - добавив поиск по интересам.
>Разбор похожих интересов (группы, книги, музыка, интересы) нужно будет провести с помощью анализа текста.

 - У каждого критерия поиска должен быть свой вес
> то есть совпадение по возрасту должно быть важнее общих групп, интересы по музыке - важнее книг, наличие общих друзей - важнее возраста и т.д.


