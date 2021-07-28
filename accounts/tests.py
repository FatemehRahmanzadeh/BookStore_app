from django.contrib.auth import get_user_model
from django.test import TestCase


# برای را کردن تست ها: python manage.py test
# وقتی این کامند اجرا می شود، یک دیتابیس موقت به نام دیفالت ایجاد می شود که
# داده های تست در دیتابیس اصلی وارد نشود. بعد از اتمام موفق تست این دیتابیس پاک می شود

class CustomUserTests(TestCase):
    def test_create_user(self):
        """
        برای تست ساخت یوزر جدید
        """
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        برای تست ساخت سوپریوزر جدید. تفاوتش با تست قبلی در این است که این یوزر باید دو اتریبیوت اضافه بر حالت قبلی فعال باشد:
        is_staff=True
        is_superuser=True
        """
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


