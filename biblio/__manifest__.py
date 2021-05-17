{
    'name': 'Gestion bibliothèque',
    'description': 'Gestion de la catalogue de livre d’une bibliothèque.',
    'author': 'Cheikhou',
    'depends': ['base'],
    'data': [
        'views/library_menu.xml',
        'views/book_view.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        
    ],
    'application' : True,
     
} 
