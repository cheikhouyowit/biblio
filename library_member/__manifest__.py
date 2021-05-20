{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Daniel Reis',
    'data': [
        'views/book_view.xml',
        'views/menu_member.xml',
        'views/member_view.xml',
        'security/member_security.xml',
        'security/ir.model.access.csv',
        
    ],
    'depends': ['biblio','base'],
    'application': False,
}
