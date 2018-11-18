# -*- coding: utf-8 -*-

{
    'name': u'Accesses holder',
    'summary': "Accesses holder",
    'version': '10.0.1.0.0',
    'category': 'Contract',
    'author': "Yauheni Yakimchyk",
    'license': 'AGPL-3',
    'depends': ['base', 'project','mail'],
    'data': [
        'views/accesses_holder_view.xml',
        'security/ir.model.access.csv',
        'security/agreement_security.xml',
        ],
    'installable': True,
}
