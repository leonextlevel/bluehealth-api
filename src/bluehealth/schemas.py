from apiflask import PaginationSchema, Schema
from apiflask.fields import Date, DateTime, Integer, List, Nested, String
from apiflask.validators import Range


class PaginationQuery(Schema):
    page = Integer(load_default=1)
    per_page = Integer(load_default=10, validate=Range(max=50))


class PatientOut(Schema):
    uuid = String(data_key='id')
    first_name = String()
    last_name = String()
    date_of_birth = Date()


class PatientFilter(Schema):
    first_name = String()
    last_name = String()


class PatientPaginationOut(Schema):
    results = List(Nested(PatientOut))
    pagination = Nested(PaginationSchema)


class PharmacyOut(Schema):
    uuid = String(data_key='id')
    name = String()
    city = String()


class PharmacyFilter(Schema):
    name = String()
    city = String()


class PharmacyPaginationOut(Schema):
    results = List(Nested(PharmacyOut))
    pagination = Nested(PaginationSchema)


class TransactionOut(Schema):
    uuid = String(data_key='id')
    amount = Integer()
    timestamp = DateTime(data_key='date')
    patient = Nested(PatientOut)
    pharmacy = Nested(PharmacyOut)


class TransactionFilter(Schema):
    patient_first_name = String()
    patient_last_name = String()


class TransactionPaginationOut(Schema):
    results = List(Nested(TransactionOut))
    pagination = Nested(PaginationSchema)
