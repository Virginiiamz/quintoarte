from odoo import models, fields, api


class marco (models.Model):
    _name = 'quintoarte.marco'
    _description = 'Un marco'
    
    marco_id = fields.Integer("Marco ID", required=True, readonly=False)
    nombre = fields.Char("Nombre", required=True, size = 30, readonly=False)
    descripcion = fields.Char("Descripcion", required=True, size = 64, readonly=False)
    foto = fields.Binary("Foto", required=True, readonly=False)
    precio_metro = fields.Float("Precio Metro", required=True, size = 30, readonly=False)
    
    enmarcado_ids = fields.One2many("quintoarte.enmarcado","marco_id", string="Cuadros enmarcados")
