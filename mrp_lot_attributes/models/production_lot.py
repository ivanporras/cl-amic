# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductionLot(models.Model):
    _inherit = "stock.production.lot"

    colada = fields.Char(
        string='COLADA'
    )
    tt = fields.Char(
        string='TT',
        help='Tratamiento Termico'
    )
    paquete = fields.Char(
        string='PAQUETE'
    )
    ot = fields.Char(
        string='OT',
        help='Orden de Trabajo'
    )
    remito_proveedor = fields.Char(
        string='Remito Proveedor'
    )
    fecha_remito = fields.Date(
    )
    aceria = fields.Char(

    )
    attributes = fields.Char(
        compute="_compute_attributes",
        readonly=True
    )
    unit_weight = fields.Float(
        help="Peso unitario del producto calculado como peso del "
             "lote / product_qty"
    )

    @property
    def unit_weight(self):
        """ Peso unitario del producto, lo que pesa cada producto
        """
        # si el producto no tiene lista de materiales el peso es el declarado
        # en el producto
        if not self.product_id.bom_ids:
            return self.product_id.weight

        # si el producto no tiene lista de materiales entonces hay que sacar
        # el precio del lote
        else:
            return self.unit_weight

    @unit_weight.setter
    def unit_weight(self, value):
        """ se define el peso unitario como el total / la qty
        """
        self.unit_weight = value / self.product_qty

    def _compute_attributes(self):
        for rec in self:
            ret = []
            if rec.ot:
                ret.append(rec.ot)
            if rec.aceria:
                ret.append('Aceria=%s' % rec.aceria)
            if rec.colada:
                ret.append('Colada=%s' % rec.colada)
            if rec.paquete:
                ret.append('Paquete=%s' % rec.paquete)
            if rec.tt:
                ret.append('TT=%s' % rec.tt)
            if rec.remito_proveedor:
                ret.append('Remito %s' % rec.remito_proveedor)
            if rec.fecha_remito:
                ret.append('Fecha Remito %s' % rec.fecha_remito)

            rec.attributes = '(' + ','.join(ret) + ')'

    def propagate_from(self, parent_lot):
        """ Mover los atributos de un lote a otro teniendo en cuenta que si
            ya existe no lo tengo que copiar.
        """

        def propagate_attr(source, dest):

            # no hay nada, escribo False en el atributo
            if not dest and not source:
                return False

            # hay algo en el lote origen y nada en el destino escribo origen
            if not dest and source:
                return source

            # hay algo en el lote destino y nada en el origen, no lo toco
            if dest and not source:
                return dest

            # hay cosas en los dos lotes, si en el atributo destino no esta el
            # atributo origen, si esta no toco el destino.
            if dest.find(source) == -1:
                return dest + ', ' + source
            else:
                return dest

        self.ot = propagate_attr(parent_lot.ot, self.ot)
        self.tt = propagate_attr(parent_lot.tt, self.tt)
        self.colada = propagate_attr(parent_lot.colada, self.colada)
        self.paquete = propagate_attr(parent_lot.paquete, self.paquete)
        self.remito_proveedor = propagate_attr(parent_lot.remito_proveedor,
                                               self.remito_proveedor)
        self.fecha_remito = propagate_attr(parent_lot.fecha_remito,
                                           self.fecha_remito)
        self.aceria = propagate_attr(parent_lot.aceria, self.aceria)
