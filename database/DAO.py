from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Distinct Order_method_type from go_methods """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Order_method_type"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Distinct year(Date) FROM go_daily_sales """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year(Date)"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllProdotti(anno,metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(Product_number)
        FROM go_daily_sales 
        WHERE year(Date) = %s AND  Order_method_code = %s 
        group by Product_number """

        cursor.execute(query, (anno, metodo,))

        for row in cursor:
            result.append(row["Product_number"])

        cursor.close()
        conn.close()
        return result


