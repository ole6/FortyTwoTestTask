from django.test import TestCase


class HomeTests(TestCase):

    def test_home_template(self):
        "test home template"
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertInHTML(
            '<link href="/static/css/bootstrap.min.css" rel="stylesheet">',
            response.content
        )
        self.assertInHTML(
            '<h1>42 Coffee Cups Test Assignment</h1>', response.content)
