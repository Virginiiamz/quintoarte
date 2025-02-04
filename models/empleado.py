from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class empleado (models.Model):
    _inherit = 'quintoarte.persona'
    _name = 'quintoarte.empleado'
    _description = 'Un empleado'
    
    sueldo = fields.Float("Sueldo", required=True, readonly=False)
    es_jefe = fields.Boolean(string='Es jefe', default=False, required=False)
    puesto = fields.Char(string='puesto', required=True, size = 60, readonly=False)
    
    # Valida si el sueldo es menor a 1200€
    @api.constrains('sueldo')
    def _check_sueldo(self):
        for record in self:
            if record.sueldo < 1200:
                raise ValidationError("El sueldo tiene que ser igual o superior a 1200€.")
    
    alquiler_ids = fields.One2many("quintoarte.alquiler","empleado_id",string="Alquileres")
     