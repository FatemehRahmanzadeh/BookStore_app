# ایمپورت ماژول تست جنگو برای اپ های حاوی پیج های استاتیک
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomepageTests(SimpleTestCase):
    """
    برای تست تمپلیت ها
    """

    def setUp(self):
        """
        برای جلوگیری از تکرار بی رویه متغیرها و ثوابت
        """
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """
        تست وجود صفحه ی هوم پیج با استفاده از کد وضعیت اچ تی تی پی 200
        """
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     """
    #     تست لود شدن صفحه با استفاده از نام یو آر ال
    #     """
    #     # response = self.client.get(reverse('home'))
    #     self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """
        تست اینکه صفحه هوم از تمپلیت درستی استفاده می کند
        """
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        """
        تست اینکه کد اچ تی ام ال و متن آن درست باشد
        """
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        """
        تست اینکه صفحه اچ تی ام ال غلط نداشته باشد
        """
        # response = self.client.get('/')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
