# Update PASS & MAIL accordingly
PASS="xxxxx"
MAIL="xxx@mail.com"
script="
from django.contrib.auth import get_user_model
User = get_user_model()

password = '$PASS';
email = '$MAIL';

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python manage.py shell
