# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields
from tools.translate import _

class product_product(osv.osv):

    _inherit = 'product.product'
    
    def _check_alt_product(self, cr, uid, ids): 
        for product in self.browse(cr, uid, ids):
            if product.alt_product_ids and product.sale_ok:
                return False
        return True
 
    _columns = {
            'selection_type': fields.selection([
                ('one','One'),
                ('multiple','Multiple')], 'Select'),
            'alt_product_ids':fields.many2many('product.product', 'alt_product_rel', 'generic_prod', 'alt_prod', 'Product List', domain=[('sale_ok', '=', True)]),
    }
    
    _defaults = {  
        'selection_type': lambda *a: 'one',
    }
    
    _constraints = [(
            _check_alt_product, 'Error: This product has alternative products, could not be sold.', ['alt_product_ids']
    )]
    
product_product()


#class stock_production_lot(osv.osv):
#    _inherit = 'stock.production.lot'
#    
#    def name_search(self,cr,uid, name="", args=[], operator="ilike", context={}, limit=100):
#        result = {}
#        res = super(stock_production_lot, self).name_search(cr,uid,name,args,operator,context)
#        if context.get('src_model') == 'mrp.lot.configurator.list':
#            if not res and args:
#                warning = {
#                'title': _('Not lot for this product!'),
#                'message': _('There is no lot for this product containing %s') % (name)
#                }
#                value = self.name_search(cr, uid, name, [], operator, context, limit)
#                result.update({'value':value})
#                result.update({'warning':warning})  
#                return value
#        return res
#stock_production_lot()