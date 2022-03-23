# Copyright 2022 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'L10n Mx Edi Decimal Fix',
    'description': """
        Adds https://github.com/odoo/enterprise/pull/21061/commits/a6e84dae3e5972464d8a9039f56640a10cde0bdc as a patch.""",
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': [
        'account', 'l10n_mx_edi'
    ],
    'data': [
    ],
    'demo': [
    ],
    'post_load': 'post_load',
}
