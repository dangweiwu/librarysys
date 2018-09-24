import xadmin
from users.models import Borrow
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "图书馆管理后台"
    site_footer = "图书馆"
    # menu_style = "accordion"


class UserAdmin():
    list_display = ['username', 'sn', 'name', 'department', 'classx']
    search_fields = ['username', 'sn', 'name']
    list_filter = ['username', 'name', 'department', 'classx']

    # def save_models(self):
    #     obj = self.new_obj
    #     data = self.request.POST
    #     if(data.get('password')):
    #         self.new_obj.password = obj.set_password(data.get('password'))
    #     super(UserAdmin, self).save_models()


class BorrowAdmin():
    list_display = ['user', 'books', 'time', 'back_time']
    search_fields = ['user', 'books', 'time', 'back_time']
    list_filter = ['user', 'books', 'time', 'back_time']


xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)

xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(Borrow, BorrowAdmin)
