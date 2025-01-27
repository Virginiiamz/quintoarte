from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class persona (models.Model):
    _name = 'quintoarte.persona'
    _description = 'Una persona'
    
    dni = fields.Char("DNI", required=True, size = 9, readonly=False)
    nombre = fields.Char("Nombre", required=True, size = 30, readonly=False)
    apellidos = fields.Char("Apellidos", required=True, size = 64, readonly=False)
    direccion = fields.Char("Direccion", required=True, size = 64, readonly=False)
    telefono = fields.Char("Telefono", required=True, size = 9, readonly=False)
    
    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            # Validar si el teléfono tiene un formato numérico de 10 dígitos
            if not re.match(r'^\d{9}$', record.telefono):
                raise ValidationError("El número de teléfono debe ser numérico y contener 9 caracteres.")