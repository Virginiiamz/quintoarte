from odoo import models, fields, api


class persona (models.Model):
    _name = 'quintoarte.persona'
    _description = 'Una persona'
    
    dni = fields.Char("DNI", required=True, size = 9, readonly=False)
    nombre = fields.Char("Nombre", required=True, size = 30, readonly=False)
    apellidos = fields.Char("Apellidos", required=True, size = 64, readonly=False)
    direccion = fields.Char("Direccion", required=True, size = 64, readonly=False)
    telefono = fields.Integer("Telefono", required=True, size = 30, readonly=False)