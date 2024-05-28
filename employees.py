from connector import Connector

class Employees:

    def get_all():
        query = "SELECT * FROM employees"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()

        return result