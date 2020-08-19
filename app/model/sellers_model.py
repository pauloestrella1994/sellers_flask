import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

from app.model.base_model import BaseModel

Base = declarative_base()

class Sellers(Base, BaseModel):

    __tablename__ = 'sellers'
    __brand = db.Column('brand', db.String(length=256))
    __mobile_phone = db.Column('mobile_phone', db.String(length=16))
    __about = db.Column('about', db.Text())
    __cnpj = db.Column('cnpj', db.String(length=14))
    __company_name = db.Column('company_name', db.String(length=255))
    __iugu_account_id = db.Column('iugu_account_id', db.String(length=64))
    __origin = db.Column('origin', db.String(length=16))
    __blocked = db.Column('blocked', db.Boolean())
    __paused = db.Column('paused', db.Boolean())
    __certificate_url = db.Column('certificate_url', db.String(length=200))
    __ctr = db.Column('ctr', db.String(length=14))
    __features = db.Column('features', db.String(length=256))
    __ie = db.Column('ie', db.String(length=14))
    __status = db.Column('status', db.String(length=14))
    __terms_of_use_version = db.Column('terms_of_use_version', db.Integer())
    __logo_url = db.Column('logo_url', db.String(length=200))
    __phone = db.Column('phone', db.String(length=16))
    __account_executive_id = db.Column('account_executive_id', db.String(length=36))
    __invite_id = db.Column('invite_id', db.String(length=36))
    __invoice_default_serial_number = db.Column('invoice_default_serial_number', db.Integer())
    __business_type = db.Column('business_type', db.String(length=255))
    __invoice_initial_number = db.Column('invoice_initial_number', db.Integer())
    __owner_id = db.Column('owner_id', db.String(length=36))
    __branded_stores = db.Column('branded_stores', db.String(length=256))
    __last_blocked_on = db.Column('last_blocked_on', db.TIMESTAMP())
    __blocked_reason = db.Column('blocked_reason', db.String(length=64))
    __has_withdraw_rejection = db.Column('has_withdraw_rejection', db.Boolean())
    __olist_responsible = db.Column('olist_responsible', db.String(length=254))
    __signup_origin = db.Column('signup_origin', db.String(length=32))
    __plan_type = db.Column('plan_type', db.String(length=16))
    __search_vector = db.Column('search_vector', db.Text())
    __portifolio_size = db.Column('portifolio_size', db.Integer())
    __is_manufacturer = db.Column('is_manufacturer', db.Boolean())
    __payment_blocked = db.Column('payment_blocked', db.Boolean())
    __payment_blocked_reason = db.Column('payment_blocked_reaosn', db.String(length=16))
    