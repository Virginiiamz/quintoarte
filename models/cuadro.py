# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cuadro(models.Model):
    _name = 'quintoarte.cuadro'
    _description = 'Un cuadro'

    titulo = fields.Char("Titulo", required=True)
    autor = fields.Char("Autor")
    anyo = fields.Integer("Año", size=4)
    ancho = fields.Integer("Ancho", size=3)
    alto = fields.Integer("Alto", size=3)
    precio_alquiler = fields.Float("Precio alquiler por día", readonly=True)
    propiedad = fields.Selection([('cliente', 'Cliente'), ('tienda', 'Tienda')], "Propiedad", default='cliente', required=True)
    foto = fields.Binary("Foto")

    alquiler_ids = fields.Many2many("quintoarte.alquiler", "alquiler_id", string="Alquileres")
    enmarcado_ids = fields.One2many("quintoarte.enmarcado","cuadro_id", string="Cuadros enmarcados")
