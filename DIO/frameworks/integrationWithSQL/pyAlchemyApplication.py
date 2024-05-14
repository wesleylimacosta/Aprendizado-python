from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)
    user = relationship("User", back_populates="address")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

print(User.__tablename__)
print(Address.__tablename__)

engine = create_engine('sqlite:///:memory:');
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())

with Session(engine) as session:
    wesley = User(
        name='Wesley',
        fullname='Wesley Lima Costa',
        address=[Address(email_address = 'wesley@gmail.com')]);

    Abimael = User(
        name='Abimael',
        fullname='Abimael Costa',
        address=[Address(email_address = 'abimael@gmail.com')]);

    session.add(wesley)
    session.add(Abimael)
    session.commit()

stmt = select(User).where(User.name.in_(['Wesley']))

order = select(User).order_by(User.fullname.desc());


stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for user in session.scalars(stmt_join):
    print(user)


connection = engine.connect();

results = connection.execute(stmt_join).fetchall();
for user in results:
    print(user)

stmt_count = select(func.count('*')).select_from(User);
for user in session.execute(stmt_count):
    print(user)