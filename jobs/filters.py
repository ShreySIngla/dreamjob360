from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class AlphabeticFilter(admin.SimpleListFilter):
    title = _('Starting with Alphabet')
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('a-z', 'A-Z'),
            ('z-a', 'Z-A'),
        )
     
    def queryset(self, request, queryset):
        value = self.value()
        print(value)
        if value == 'a-z':
            return queryset.order_by('title')
        elif value == 'z-a':
            return queryset.order_by('-title')
    # def queryset(self, request, queryset):
    #     if self.value() == 'a-z':
    #         return queryset.order_by('title')
    #     elif self.value() == 'z-a':
    #         return queryset.order_by('-title')


    # def lookups(self, request, model_admin):
    #     return (
    #         ('a', _('A')),
    #         ('b', _('B')),
    #         ('c', _('C')),
    #         ('d', _('D')),
    #         ('e', _('E')),
    #         ('f', _('F')),
    #         ('g', _('G')),
    #         ('h', _('H')),
    #         ('i', _('I')),
    #         ('j', _('J')),
    #         ('k', _('K')),
    #         ('l', _('L')),
    #         ('m', _('M')),
    #         ('n', _('N')),
    #         ('o', _('O')),
    #         ('p', _('P')),
    #         ('q', _('Q')),
    #         ('r', _('R')),
    #         ('s', _('S')),
    #         ('t', _('T')),
    #         ('u', _('U')),
    #         ('v', _('V')),
    #         ('w', _('W')),
    #         ('x', _('X')),
    #         ('y', _('V')),
    #         ('z', _('Z')),
            
            
    #     )

    # def queryset(self, request, queryset):
    #     value = self.value()
    #     if value:
    #         return queryset.filter(title__istartswith=value)
