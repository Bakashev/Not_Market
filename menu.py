import models.products
import models.orders
import models.users
import connect_db


connect_db.configurate_engine()


class UserMenu():
    def __init__(self, login_reg, password_reg):

        with connect_db.Session(autoflush=False, bind=connect_db.engine) as db:
            res = db.query(models.users.User)
            for element in res:
                if element.username == login_reg and element.password == password_reg:
                    while True:
                        first_user_comand = '>\tТовары'
                        second_user_comand = '>\tКупить'
                        third_user_comand = '>\tПрофиль'
                        four_user_comand = '>\tТикет'
                        print(f'{first_user_comand}\n{second_user_comand}\n{third_user_comand}\n{four_user_comand}\n')
                        # global models
                        # global pasword
                        # global user_id
                        models.users.login = login_reg
                        models.users.pasword = password_reg
                        models.users.user_id = element.id
                        user_comand = input('Выберите команду:').lower()
                        if user_comand == 'товары':
                            models.products.Product.get_product()
                        elif user_comand == 'купить':
                            try:
                                buy = input('Введите номер заказа и количество: ').split()
                                models.orders.Orders.buy_product(int(buy[0]), int(buy[1]))
                            except ValueError:
                                print('введены не число')
                            except IndexError:
                                print('не верный формат ввода')


                        elif user_comand == 'профиль':
                            models.users.User.show_profile(models.users.user_id)
                        elif user_comand.lower() == 'тикет':
                            ticket = input('Введите свой билет:')
                            models.tickets.Ticket.use_ticket(ticket)
                        else:
                            exit = input('Вы хотите выйти? да\нет')
                            if exit.lower() == 'да':
                                break

class StartMenu():
    while True:
        first_row = '===Добро пожаловать в "Не магазин" ==='
        second_row = 'Здесь вы можете обменивать тикеты для того, чтобы приобретать товары'
        third_row = 'Для взоимодействия используйте команды:'
        print(f'\t\t\t\t{first_row}\n{second_row}\n{third_row}\n')
        first_comand = '>\tТовары'
        second_comand = '>\tЗарегистрироваться'
        third_comand = '>\tВойти'
        print(f'{first_comand}\n{second_comand}\n{third_comand}')
        result = input('Введите команду:').lower()
        if result == 'товары':
            models.products.Product.get_product()
        elif result == 'зарегистрироваться':
            login_reg = input('Введите логин >')
            password_reg = input('Введите пароль >')
            if models.users.User.is_exist(login_reg):
                models.users.User.create_user(login_reg, password_reg)


        elif result == 'войти':
            #models.users.User.user_entry()
            login_reg = input('Введите свой логин >')
            password_reg = input('Введите свой пароль >')
            menu_user = UserMenu(login_reg, password_reg)


        else:
            break
