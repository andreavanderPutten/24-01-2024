from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(year(gds.Date)) as anno
                    from go_sales.go_daily_sales gds """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["anno"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from go_sales.go_methods gm  """

        cursor.execute(query)

        for row in cursor:
            result.append((row["Order_method_code"], row["Order_method_type"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno, metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(gds.Product_number), sum(gds.Unit_sale_price*gds.Quantity) as ricavo
                from go_sales.go_daily_sales gds 
                where year(gds.Date) = %s and gds.Order_method_code = %s
                group by Product_number """

        cursor.execute(query, (anno, metodo, ))

        for row in cursor:
            result.append((row["Product_number"], row["ricavo"]))

        cursor.close()
        conn.close()
        return result