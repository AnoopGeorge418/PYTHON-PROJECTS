# from Restaturant import Restaurant, users # importing different classes
import Restaturant as r # importing entire module

restaurant = r.Restaurant('The Great kitchen', 'Chinese')
print(restaurant.number_served)

user1 = r.users('Monkey D ', 'Luffy', 'Meat')
user2 = r.users('Roranoa ', 'Zoro', 'Three sword style')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'Login attempts for {user1.f_name}{user1.l_name}: {user1.login_attempts}')
user1.reset_login_attempts()
print(f'Login attempts for {user1.f_name}{user1.l_name} after reset: {user1.login_attempts}')