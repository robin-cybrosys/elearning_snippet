# Create a snippet to show latest 3 elearning courses. On click it should
# redirect to corresponding course. Dynamic snippet which shows elearning
# courses.
{
    'name': "E-Learning Snippet",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base','web','website_slides'],
    'data': [
        'snippets/elearning_snippet.xml',
        # 'snippets/elearning_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/elearning_snippet/static/src/js/dynamic.js',
        ],
    },
}
