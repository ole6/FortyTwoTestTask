from django.test import TestCase
from hello.models import Person


class HomeTests(TestCase):

    def test_home_template(self):
        """test home template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertInHTML(
            '<link href="/static/css/bootstrap.min.css" rel="stylesheet">',
            response.content
        )
        self.assertInHTML(
            '<h1>42 Coffee Cups Test Assignment</h1>', response.content)

    def test_person_model(self):
        """test Person model"""

        person_list = Person.objects.all()
        self.assertEqual(person_list.count(), 1)

        p = person_list[0]

        self.assertEqual(p.first_name, 'Oleh')
        self.assertEqual(p.last_name, 'Lytovchenko')
        self.assertEqual(p.birth, '26.06.1984')
        self.assertEqual(p.email, 'lytowchenko@gmail.com')
        self.assertEqual(p.jabber, 'lytovchenko@42cc.co')
        self.assertEqual(p.skype, 'lytovchenkoo')
        self.assertEqual(p.site, 'lytovchenko.com')
