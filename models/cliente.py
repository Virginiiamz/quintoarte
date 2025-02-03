from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class cliente (models.Model):
    _inherit = 'quintoarte.persona'
    _name = 'quintoarte.cliente'
    _description = 'Un cliente'
    
    es_vip = fields.Boolean(string='Es VIP', default=False, required=False)
    tipo = fields.Selection([('particular', 'Particular'),
                                ('empresa publica', 'Empresa publica'),
                                ('empresa privada', 'Empresa privada'),
                                ('asociacion', 'Asociacion')], "Tipo de cliente", default='particular', required=True)
    
    state = fields.Selection([('no_paga','No paga'),
                                ('paga_siempre','Paga Siempre')], 'Estado', default='paga_siempre', required=True)
    
    alquiler_ids = fields.One2many("quintoarte.alquiler","cliente_id",string="Alquileres")
    enmarcado_ids = fields.One2many("quintoarte.enmarcado","cliente_id", string="Cuadros enmarcados")
    
    def btn_submit_to_pagasiempre(self):
        if not self.state:
            raise UserError("El campo 'state' está vacío o no válido.")
        if self.state == 'paga_siempre':
            raise UserError("El cliente ya está marcado como 'Paga Siempre'.")
        self.write({'state': 'paga_siempre'})

    def btn_submit_to_nopaga(self):
        if self.state == 'no_paga':
            raise UserError("El cliente ya está marcado como 'No Paga'.")
        self.write({'state': 'no_paga'})