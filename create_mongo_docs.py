from mongoengine import Document, ReferenceField, StringField, connect
from mongoengine.connection import get_db


def connect_db():
    connect('test')


def drop_all():
    try:
        db = connect('test')
        db.drop_database('test')
    except Exception as e:
        print("Error dropping database [{}]".format(e.message))


class Company(Document):
    name = StringField(max_length=200, required=True)


class User(Document):
    first_name = StringField(max_length=200, required=True)
    last_name = StringField(max_length=200, required=True)
    company = ReferenceField(Company)

def build_sample_docs():
    company1 = Company(name="Acme Corporation")
    company1.save()
    company2 = Company(name="Sands Corporation")
    company2.save()

    user1 = User(first_name="Jack", last_name="Barnaby", company=company1)
    user1.save()
    user2 = User(first_name="Jill", last_name="Hill", company=company2)
    user2.save()


if __name__ == "__main__":
    drop_all()
    connect_db()
    build_sample_docs()
