from odoo import models, fields, api


class empleado (models.Model):
    _inherit = 'quintoarte.persona'
    _name = 'quintoarte.empleado'
    _description = 'Un empleado'
    
    sueldo = fields.Float("Sueldo", required=True, readonly=False)
    es_jefe = fields.Boolean(string='Es jefe', default=False, required=False)
    puesto = fields.Char(string='puesto', required=True, size = 60, readonly=False)
    
    alquiler_ids = fields.One2many("quintoarte.alquiler","alquiler_id",string="Alquileres")
     