import logging

from psycopg2 import sql

from odoo import fields


def pre_init_hook(cr):
    # print('\n* pre_init_hook', dir(cr))
    logger = logging.getLogger(__name__)
    now = fields.Datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE sale_order SET commitment_date='{}' WHERE commitment_date is NULL"
    cr.execute(sql.format(now))
    logger.info("Updated commitment_date of %s sale order%s to %s", cr.rowcount,
        "s" if cr.rowcount > 1 else "", now)
