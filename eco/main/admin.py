from django.contrib import admin
from .models import Habit, UserHabit, ActivityLog, Goal, Badge, UserBadge, Tip

admin.site.register(Habit)
admin.site.register(UserHabit)
admin.site.register(ActivityLog)
admin.site.register(Goal)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(Tip)
