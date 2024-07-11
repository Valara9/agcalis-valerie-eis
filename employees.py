from connector import Connector

class Employees:

    def get_all():
        query = "SELECT * FROM employees"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()

        return result


    def add_employee(emp_id , lname, fname, mname):
        query = "INSERT INTO employees VALUES (%s , %s , %s, %s)"

        try:
            connector.cursor.execute(query, (emp_id , lname, fname, mname))
            connector.db.commit()

            return True
        except:
            return False