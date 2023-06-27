from django.contrib import admin
from leave_app.models import Number,Form,Person
from django.contrib.auth.admin import UserAdmin


class PersonAdmin(UserAdmin):
    # readonly_fields = ('display_image',)
    
    # # def display_image(self, obj):
    # #     return obj.image_tag()

    # # display_image.short_description = 'Image'
    
    list_display = ("username", "email","nickname","team","position","leader","level",) # field ที่จะแสดง
    # add_fieldsets = ( #หน้าแรกต้องการให้กรอกข้อมูลอะไรบ้างที่สำคัญ
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),

    #             "fields": ("username", "email", "password1", "password2"),
    #         },
    #     ),
    # )
    
    fieldsets = (
        (None,{'fields':['username','first_name','last_name','email','nickname','tel','team','position','leader','level']}),
        ('category',{'fields':['last_login'], 'classes':['collapse']}),
    )
    
admin.site.register(Person, PersonAdmin)   #เรียกใช้ตาราง person บนหน้า admin

# Register your models here.

# admin.site.register(Person)

class NumberAdmin(admin.ModelAdmin):
    # Sequence Data
    fields = ['username', 'sick', 'personal' ,'vacation']

    # Show Data

    list_display = ['username', 'sick', 'personal' ,'vacation']

    list_per_page = 10

    list_max_show_all =  1000

    list_display_links = ['username', ] # Link to Edit

    list_editable = [] # Can change in 1st page

    list_filter = []

    search_fields = ['username'] # Lookup Field in List

    readonly_fields = []

admin.site.register(Number,NumberAdmin)


class FormAdmin(admin.ModelAdmin):
    # Sequence Data
    fields = ['username', 'typeleave', 'numberleave' ,'From_Date','To_Date','reason']

    # Show Data

    list_display = ['username', 'typeleave', 'numberleave' ,'From_Date','To_Date','reason']

    list_per_page = 10

    list_max_show_all =  1000

    list_display_links = ['username', ] # Link to Edit

    list_editable = [] # Can change in 1st page

    list_filter = []

    search_fields = ['username'] # Lookup Field in List

    readonly_fields = []

admin.site.register(Form,FormAdmin)




