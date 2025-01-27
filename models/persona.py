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
    
    # Valida si el telefono tiene 9 caracteres y es numerico
    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if not re.match(r'^\d{9}$', record.telefono):
                raise ValidationError("El número de teléfono debe ser numérico y contener 9 caracteres.")
          
    # Valida si el DNI tiene 8 caracteres y es alfanumerico  
    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if not re.match(r'^\d{8}[a-zA-Z]$', record.dni):
                raise ValidationError("El DNI debe contener 8 dígitos y 1 letra.")