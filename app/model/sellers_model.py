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
    __payment_blocked_reason = db.Column('payment_blocked_reason', db.String(length=16))

    def __init__(self, brand: str = '', mobile_phone: str = '', about: str = '', cnpj: str = ''
                , company_name: str = '', iugu_account_id: str = '', origin: str = '', blocked: bool = False
                , paused: bool = False, certificate_url: str = '', ctr: str = '', features: str = ''
                , ie: str = '', status: str = '', terms_of_use_version: str = '', logo_url: str = ''
                , phone: str = '', account_executive_id: str = '', invite_id: str = '', invoice_default_serial_number: int = 0
                , business_type: str = '', invoice_initial_number: int = 0, owner_id: str = '', branded_stores: str = ''
                , last_blocked_on, blocked_reason: str = '', has_withdraw_rejection: bool = False, olist_responsible: str = ''
                , signup_origin: str= '', plan_type: str ='', search_vector: str='', portifolio_size: int = 0
                , is_manufacturer: bool = False, payment_blocked: bool = False, payment_blocked_reason: str  = ''):

        self.__brand = brand
        self.__mobile_phone = mobile_phone
        self.__about = about
        self.__cnpj = cnpj
        self.__company_name = company_name
        self.__iugu_account_id = iugu_account_id
        self.__origin = origin
        self.__blocked = blocked
        self.__paused = paused
        self.__certificate_url = certificate_url
        self.__ctr = ctr
        self.__features = features
        self.__ie = ie
        self.__status = status
        self.__terms_of_use_version = terms_of_use_version
        self.__logo_url = logo_url
        self.__phone = phone
        self.__account_executive_id = account_executive_id
        self.__invite_id = invite_id
        self.__invoice_default_serial_number = invoice_default_serial_number
        self.__business_type = business_type
        self.__invoice_initial_number = invoice_initial_number
        self.__owner_id = owner_id
        self.__branded_stores = branded_stores
        self.__last_blocked_on = last_blocked_on
        self.__blocked_reason = blocked_reason
        self.__has_withdraw_rejection = has_withdraw_rejection
        self.__olist_responsible = olist_responsible
        self.__signup_origin = signup_origin
        self.__plan_type = plan_type
        self.__search_vector = search_vector
        self.__portifolio_size = portifolio_size
        self.__is_manufacturer = is_manufacturer
        self.__payment_blocked = payment_blocked
        self.__payment_blocked_reason = payment_blocked_reason
        super().__init__(id, created_at, updated_at)

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def mobile_phone(self) -> str:
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone: str):
        self.__mobile_phone = mobile_phone

    @property
    def about(self) -> str:
        return self.__about

    @about.setter
    def about(self, about: str):
        self.__about = about

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj

    @property
    def company_name(self) -> str:
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name: str):
        self.__company_name = company_name

    @property
    def iugu_account_id(self) -> str:
        return self.__iugu_account_id

    @iugu_account_id.setter
    def iugu_account_id(self, iugu_account_id: str):
        self.__iugu_account_id = iugu_account_id

    @property
    def origin(self) -> str:
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin

    @property
    def blocked(self) -> bool:
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked

    @property
    def paused(self) -> bool:
        return self.__paused

    @paused.setter
    def paused(self, paused: bool):
        self.__paused = paused

    @property
    def certificate_url(self) -> str:
        return self.__certificate_url

    @certificate_url.setter
    def certificate_url(self, certificate_url: str):
        self.__certificate_url = certificate_url

    @property
    def ctr(self) -> str:
        return self.__ctr

    @ctr.setter
    def ctr(self, ctr: str):
        self.__ctr = ctr

    @property
    def features(self) -> str:
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features

    @property
    def ie(self) -> str:
        return self.__ie

    @ie.setter
    def ie(self, ie: str):
        self.__ie = ie

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def terms_of_use_version(self) -> str:
        return self.__terms_of_use_version

    @terms_of_use_version.setter
    def terms_of_use_version(self, terms_of_use_version: str):
        self.__terms_of_use_version = terms_of_use_version

    @property
    def logo_url(self) -> str:
        return self.__logo_url

    @logo_url.setter
    def logo_url(self, logo_url: str):
        self.__logo_url = logo_url

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def account_executive_id(self) -> str:
        return self.__account_executive_id

    @account_executive_id.setter
    def account_executive_id(self, account_executive_id: str):
        self.__account_executive_id = account_executive_id

    @property
    def invite_id(self) -> str:
        return self.__invite_id

    @invite_id.setter
    def invite_id(self, invite_id: str):
        self.__invite_id = invite_id

    @property
    def invoice_default_serial_number(self) -> int:
        return self.__invoice_default_serial_number

    @invoice_default_serial_number.setter
    def invoice_default_serial_number(self, invoice_default_serial_number: int):
        self.__invoice_default_serial_number = invoice_default_serial_number

    @property
    def business_type(self) -> str:
        return self.__business_type

    @business_type.setter
    def business_type(self, business_type: str):
        self.__business_type = business_type

    @property
    def invoice_initial_number(self) -> int:
        return self.__invoice_initial_number

    @invoice_initial_number.setter
    def invoice_initial_number(self, invoice_initial_number: int):
        self.__invoice_initial_number = invoice_initial_number

    @property
    def owner_id(self) -> str:
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self.__owner_id = owner_id

    @property
    def branded_stores(self) -> str:
        return self.__branded_stores

    @branded_stores.setter
    def branded_stores(self, branded_stores: str):
        self.__branded_stores = branded_stores

    @property
    def last_blocked_on(self):
        return self.__last_blocked_on

    @last_blocked_on.setter
    def last_blocked_on(self, last_blocked_on):
        self.__last_blocked_on = last_blocked_on

    @property
    def blocked_reason(self) -> str:
        return self.__blocked_reason

    @blocked_reason.setter
    def blocked_reason(self, blocked_reason: str):
        self.__blocked_reason = blocked_reason

    @property
    def has_withdraw_rejection(self) -> bool:
        return self.__has_withdraw_rejection

    @has_withdraw_rejection.setter
    def has_withdraw_rejection(self, has_withdraw_rejection: bool):
        self.__has_withdraw_rejection = has_withdraw_rejection

    @property
    def olist_responsible(self) -> str:
        return self.__olist_responsible

    @olist_responsible.setter
    def olist_responsible(self, olist_responsible: str):
        self.__olist_responsible = olist_responsible

    @property
    def signup_origin(self) -> str:
        return self.__signup_origin

    @signup_origin.setter
    def signup_origin(self, signup_origin: str):
        self.__signup_origin = signup_origin

    @property
    def plan_type(self) -> str:
        return self.__plan_type

    @plan_type.setter
    def plan_type(self, plan_type: str):
        self.__plan_type = plan_type

    @property
    def search_vector(self) -> str:
        return self.__search_vector

    @search_vector.setter
    def search_vector(self, search_vector: str):
        self.__search_vector = search_vector

    @property
    def portifolio_size(self) -> int:
        return self.__portifolio_size

    @portifolio_size.setter
    def portifolio_size(self, portifolio_size: int):
        self.__portifolio_size = portifolio_size

    @property
    def is_manufacturer(self) -> bool:
        return self.__is_manufacturer

    @is_manufacturer.setter
    def is_manufacturer(self, is_manufacturer: bool):
        self.__is_manufacturer = is_manufacturer

    @property
    def payment_blocked(self) -> bool:
        return self.__payment_blocked

    @payment_blocked.setter
    def payment_blocked(self, payment_blocked: bool):
        self.__payment_blocked = payment_blocked

    @property
    def payment_blocked_reason(self) -> str:
        return self.__payment_blocked_reason

    @payment_blocked_reason.setter
    def payment_blocked_reason(self, payment_blocked_reason: str):
        self.__payment_blocked_reason = payment_blocked_reason

    def to_json(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'brand': self.brand,
            'mobile_phone': self.mobile_phone,
            'abour': self.about,
            'cnpj': self.cnpj,
            'company_name': self.company_name,
            'iugu_account_id': self.iugu_account_id,
            'origin': self.origin,
            'blocked': self.blocked,
            'paused': self.paused,
            'certificate_url': self.certificate_url,
            'ctr': self.ctr,
            'features': self.features,
            'ie': self.ie,
            'status': self.status,
            'terms_of_use_version': self.__terms_of_use_version,
            'logo_url': self.logo_url,
            'phone': self.phone,
            'account_executive_id': self.account_executive_id,
            'invite_id': self.invite_id,
            'invoice_default_serial_number': self.invoice_default_serial_number,
            'business_type': self.business_type,
            'invoice_initial_number': self.invoice_default_serial_number,
            'owner_id': self.owner_id,
            'branded_stores': self.branded_stores,
            'last_blocked_on': self.last_blocked_on,
            'blocked_reason': self.blocked_reason,
            'has_withdraw_rejection': self.has_withdraw_rejection,
            'olist_responsible': self.olist_responsible,
            'signup_origin': self.signup_origin,
            'plan_type': self.plan_type,
            'search_vector': self.search_vector,
            'portifolio_size': self.portifolio_size,
            'is_manufacturer': self.is_manufacturer,
            'payment_blocked': self.payment_blocked,
            'payment_blocked_reason': self.payment_blocked_reason
        }