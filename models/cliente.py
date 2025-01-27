from odoo import models, fields, api


class cliente (models.Model):
    _inherit = 'quintoarte.persona'
    _name = 'quintoarte.cliente'
    _description = 'Un cliente'
    
    es_vip = fields.Boolean(string='Es VIP', default=False, required=False)
    tipo = fields.Selection([('particular', 'Particular'),
                                ('empresa publica', 'Empresa publica'),
                                ('empresa privada', 'Empresa privada'),
                                ('asociacion', 'Asociacion')], "Tipo de cliente", default='particular', required=True)
    
    alquiler_ids = fields.One2many("quintoarte.alquiler","alquiler_id",string="Alquileres")
    enmarcado_ids = fields.One2many("quintoarte.enmarcado","cliente_id", string="Cuadros enmarcados")
     