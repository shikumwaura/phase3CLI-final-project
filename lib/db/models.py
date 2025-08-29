from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///order_management.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    _customer_name = Column("customer_name", String, nullable=False)
    products = relationship("Product", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, customer_name={self.customer_name})>"

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Customer name must be a non-empty string.")
        self._customer_name = value

    @classmethod
    def create(cls, customer_name):
        order = cls(customer_name=customer_name)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, order_id):
        return session.query(cls).filter_by(id=order_id).first()

    def delete(self):
        session.delete(self)
        session.commit()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, order_id={self.order_id})>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Product name must be a non-empty string.")
        self._name = value

    @classmethod
    def create(cls, name, order):
        product = cls(name=name, order=order)
        session.add(product)
        session.commit()
        return product

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, product_id):
        return session.query(cls).filter_by(id=product_id).first()

    def delete(self):
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
