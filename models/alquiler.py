# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alquiler(models.Model):
    _name = 'quintoarte.alquiler'
    # _inherit = 'quintoarte.persona'
    _description = 'Alquiler de un marco o cuadro'

    alquiler_id = fields.Integer("", autogenerated=True)
    fecha_inicio = fields.Date("Fecha de inicio")
    fecha_fin = fields.Date("Fecha de fin")
    precio_total = fields.Float("Precio total", (10,2))
    observacion = fields.Text("Observación")
    direccion = fields.Char("Dirección")
    #cuadro_ids = fields.Many2many('')
    #empleado_id = fields.Many2one('res.partner', string="Empleado", required=True)
    # cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)