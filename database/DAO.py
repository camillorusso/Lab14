from database.DB_connect import DBConnect
from model.stores import Store
from model.nodes import Node
from model.edges import Edge
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """SELECT * from stores"""

        cursor.execute(query)

        for row in cursor:
            result.append(Store(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(store_id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select *
                    from orders o
                    where o.store_id = %s"""

        cursor.execute(query, (store_id,))

        for row in cursor:
            result.append(Node(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(store_id, giorni):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select o1.order_id as order_id1, o2.order_id as order_id2, (oi1.quantity + oi2.quantity) as peso, DATEDIFF(o1.order_date, o2.order_date) as verso
                    from orders o1, orders o2, order_items oi1, order_items oi2
                    where o1.store_id = %s and o2.store_id = %s and o1.order_id != o2.order_id and ABS(DATEDIFF(o1.order_date, o2.order_date)) < %s
                    and o1.order_id = oi1.order_id and o2.order_id = oi2.order_id
                    group by o1.order_id, o2.order_id
                    having verso > 0"""

        cursor.execute(query, (store_id,store_id,giorni,))

        for row in cursor:
            result.append(Edge(**row))

        cursor.close()
        conn.close()
        return result
