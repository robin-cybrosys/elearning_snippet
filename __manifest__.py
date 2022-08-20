{
    'name': "E-Learning Snippet",
    'author': "My Company",
    'website': "http://www.cybrosys.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base','web','website_slides'],
    'data': [
        'snippets/elearning_snippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/elearning_snippet/static/src/js/dynamic.js',
        ],
    },
}
