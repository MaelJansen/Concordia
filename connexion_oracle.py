import oracledb
i
class Board:
    """_summary_
    """
    def __init__(self):

        self.connection = oracledb.connect(
            user="ETD",
            password="ETD",
            host="localhost",
            port=1521,
            sid="IUT12c"
        )
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""
            SELECT *
            FROM t_concordia""")
        
        # for fname in self.cursor:
        #     print("Values:", fname)
            
    def get_capitale(self, board):
        sql_query = f"""SELECT t.MAP_CAPITAL.CITY_NAME AS CAPITAL FROM T_Concordia, TABLE(T_Concordia.concordia_map) t WHERE t.map_name='{board}'"""
        self.cursor.execute(sql_query)

        for row in self.cursor:
            capitale = row[0]
            print("Capitale", capitale, "est la capitale de ", board)
            print(row)


board_instance = Board()
board_instance.get_capitale('Imperium')