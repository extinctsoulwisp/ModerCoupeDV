from app.model import Order
from app.model.orm import Database, OrderData
from app.model.pdf import create_customer_doc

if __name__ == '__main__':
    Database.init_superuser()
    with Database.Session() as session:
        order = Order(session.query(OrderData).filter(OrderData.id == 154).one())
        create_customer_doc(order)
