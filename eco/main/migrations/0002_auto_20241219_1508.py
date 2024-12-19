from django.db import migrations
from datetime import date

def create_test_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Habit = apps.get_model('main', 'Habit')
    UserHabit = apps.get_model('main', 'UserHabit')
    Goal = apps.get_model('main', 'Goal')

    user = User.objects.create_user(username='testuser', password='testpassword')

    habit1 = Habit.objects.create(name='Recycle Plastic', description='Recycle plastic waste', points=10)
    habit2 = Habit.objects.create(name='Bike to Work', description='Use a bicycle for daily commuting', points=20)
    habit3 = Habit.objects.create(name='Stop throwing Cesium-137', description='Stop throwing Cesium-137 on anoying children', points=50)

    UserHabit.objects.create(user=user, habit=habit1, frequency='daily', start_date=date.today())
    UserHabit.objects.create(user=user, habit=habit2, frequency='weekly', start_date=date.today())
    UserHabit.objects.create(user=user, habit=habit3, frequency='monthly', start_date=date.today())

    Goal.objects.create(user=user, description='Reduce carbon footprint by 20%', target_date=date(2024, 12, 31), achieved=False)
    Goal.objects.create(user=user, description='Plant 100 trees this year', target_date=date(2024, 6, 30), achieved=True)

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(create_test_data),
    ]
