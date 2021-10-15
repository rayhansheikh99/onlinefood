from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'shop'
    

class UsersConfig(AppConfig):
    name = 'shop'

    def ready(self):
        import shop.signals
    