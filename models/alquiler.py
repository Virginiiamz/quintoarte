# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alquiler(models.Model):
    _name = 'quintoarte.alquiler'
    _description = 'Alquiler de un marco o cuadro'

    alquiler_id = fields.Integer("", autogenerated=True, readonly=True)
    fecha_inicio = fields.Date("Fecha de inicio", required=True)
    fecha_fin = fields.Date("Fecha de fin", required=True)
    precio_total = fields.Float("Precio total", (10,2), readonly=True)
    observacion = fields.Text("Observación")
    direccion = fields.Char("Dirección")
    
    cuadro_ids = fields.Many2many("quintoarte.cuadro", "cuadro_id", string="Cuadros")
    empleado_id = fields.Many2one("quintoarte.empleado", string="Empleado")
    cliente_id = fields.Many2one("quintoarte.cliente", string="Cliente")