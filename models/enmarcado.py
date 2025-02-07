from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError



class enmarcado (models.Model):
    _name = 'quintoarte.enmarcado'
    _description = 'Enmarcado'
    
    enmarcado_id = fields.Integer("Enmarcado ID", required=True, readonly=False)
    metros = fields.Float("Metros", required=True, size = 30, readonly=False)
    precio_total = fields.Float("Precio total", required=True, readonly=False)
    fecha_enmarcado = fields.Date("Fecha Enmarcado", required=True, readonly=False)
    
    estadoEnmarcado = fields.Selection([('enproceso','En proceso'),
                                ('terminado','Terminado')], 'Estado', default='enproceso', required=True)
    

    marco_id = fields.Many2one("quintoarte.marco",string="Marco")
    cuadro_id = fields.Many2one("quintoarte.cuadro",string="Cuadro")
    cliente_id = fields.Many2one("quintoarte.cliente",string="Cliente")

    def btn_submit_to_terminado(self):
            if not self.estadoEnmarcado:
                raise UserError("El campo 'estadoEnmarcado' está vacío o no válido.")
            if self.estadoEnmarcado == 'terminado':
                raise UserError("El enmarcado ya está marcado como 'Terminado'.")
            self.write({'estadoEnmarcado': 'terminado'})

    def btn_submit_to_enproceso(self):
        if self.estadoEnmarcado == 'enproceso':
            raise UserError("El enmarcado ya está marcado como 'En proceso'.")
        self.write({'estadoEnmarcado': 'enproceso'})