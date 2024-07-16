from django.test import TestCase
from .forms import ArticlesForm

class ArticlesFormTest(TestCase):
    def test_articles_form_valid_data(self):
        form = ArticlesForm(data={
            'title': 'Test Article',
            'anons': 'This is a test announcement',
            'full': 'This is the full content of the test article',
            'date': '2024-07-15 12:00:00',
        })

        self.assertTrue(form.is_valid())

    def test_articles_form_invalid_data(self):
        form = ArticlesForm(data={
            'title': '',
            'anons': '',
            'full': '',
            'date': '',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_articles_form_widgets(self):
        form = ArticlesForm()

        self.assertEqual(form.fields['title'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['title'].widget.attrs['placeholder'], 'Название статьи')
        self.assertEqual(form.fields['anons'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['anons'].widget.attrs['placeholder'], 'Анонс статьи')
        self.assertEqual(form.fields['date'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['date'].widget.attrs['placeholder'], 'Дата публикации')
        self.assertEqual(form.fields['full'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['full'].widget.attrs['placeholder'], 'Текст статьи')

if __name__ == "__main__":
    TestCase.main()
