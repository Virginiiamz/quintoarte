from odoo import models, fields, api


class enmarcado (models.Model):
    _name = 'quintoarte.enmarcado'
    _description = 'Enmarcado'
    
    enmarcado_id = fields.Integer("Enmarcado ID", required=True, readonly=False)
    metros = fields.Float("Metros", required=True, size = 30, readonly=False)
    precio_total = fields.Float("Precio total", required=True, readonly=False)
    fecha_enmarcado = fields.Date("Fecha Enmarcado", required=True, readonly=False)
    

    marco_id = fields.Many2one("quintoarte.marco",string="Marco")
    cuadro_id = fields.Many2one("quintoarte.cuadro",string="Cuadro")
    cliente_id = fields.Many2one("quintoarte.cliente",string="Cliente")
