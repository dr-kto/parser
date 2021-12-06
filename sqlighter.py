import sqlite3

class SQLighter:

    def __inti__(self, database_file):
        """Подключаемся к БД и сохраняем курсор соединение"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()    
        
    def subsciber_exists(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        """Добавляем подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?,?)", (user_id, status))


    def update_subscription(self, user_id, status):
        """Обновляем статус подписки"""
        return self.cursor.execute("Update `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()