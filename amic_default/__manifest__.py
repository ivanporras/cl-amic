# -----------------------------------------------------------------------------
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'AMIC-13',
    'version': '13.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for AMIC',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',
        'mrp',
        'hr',

        # additional applications
        'mrp_workorder',  # ordenes de trabajo
        # 'web_gantt', no anda bien.
        # 'mrp_mps',  # plan maestro de produccion
        'mrp_account',  # contabilidad analitica en fabricacion

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        'backend_theme_v11',
        # preview bom
        'mrp_bom_structure_html',

        # desarrollo especifico para amic
        'customer_product_names',  # nombres de prod <> por cliente
        'mrp_lot_attributes',  # caracteristicas de trazabilidad
        'mrp_ot',  # generacion de ordenes de trabajo
        'pre_printed_stock_picking',  # remito preimpreso
        'mrp_easy_prod',  # wizard para encontrar rapidamente la ot produccion
        'mrp_production_cancel',

        # requerido por la restriccion de menuitems
        'mail', 'calendar', 'contacts', 'mrp', 'sale', 'purchase', 'stock',
        'account', 'hr', 'base'
    ],
    'data': [
        'security/menuitem_security.xml',
        'views/menuitems.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'CPUs': '1',
    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '6000',
    'limit_time_real': '12000',

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    'git-repos': [

        'http://github.com/jobiols/cl-amic.git',
        'http://github.com/jobiols/odoo-addons.git',
        'git@github.com:jobiols/jeo-addons.git'
        #{'usr': 'jobiols', 'repo': 'jeo-addons', 'branch': '11.0', 'ssh': True,'host': 'github.com-jeo'},

        'http://github.com/ingadhoc/odoo-argentina.git',
        'http://github.com/ingadhoc/argentina-sale.git',
        'http://github.com/ingadhoc/account-financial-tools.git',
        'http://github.com/ingadhoc/account-payment.git',
        'http://github.com/ingadhoc/miscellaneous.git',
        'http://github.com/ingadhoc/argentina-reporting.git',
        'http://github.com/ingadhoc/reporting-engine.git',
        'http://github.com/ingadhoc/sale.git',
        'http://github.com/ingadhoc/odoo-support.git',
        'http://github.com/ingadhoc/product.git',
        'http://github.com/ingadhoc/stock.git',
        'http://github.com/ingadhoc/account-invoicing.git',
        'http://github.com/ingadhoc/patches.git',
        'http://github.com/oca/queue.git',
        'http://github.com/oca/partner-contact.git',
        'http://github.com/oca/web.git',
        'http://github.com/oca/server-tools.git',
        'http://github.com/oca/social.git',
        'http://github.com/oca/server-ux.git',
        'http://github.com/oca/server-brand.git',
        'http://github.com/oca/manufacture.git',
        'http://github.com/oca/manufacture-reporting.git',
        'http://github.com/oca/management-system.git',
        'http://github.com/oca/sale-workflow.git',
        'http://github.com/oca/stock-logistics-warehouse.git',
        'http://github.com/oca/stock-logistics-reporting.git',
        'http://github.com/oca/stock-logistics-workflow.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-ent:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ],

}
