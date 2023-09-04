import oracledb

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
        sql_query = f"""SELECT c.CITY_NAME as city_name,
            c.CITY_ROMAN_CHAR as roman_num,
            c.CITY_COORDINATES.X as x,
            c.CITY_COORDINATES.Y as y,
            c.CITY_COORDINATES.Z as Z
            FROM T_Concordia, TABLE(T_Concordia.concordia_map) t , TABLE(t.MAP_PROVINCE) p, TABLE(p.province_city) c
            WHERE t.map_name='Italia'
            AND p.province_name = 'LIGVRIA'"""
        self.cursor.execute(sql_query)

        for row in self.cursor:
            capitale = row[0]
            print("Capitale", capitale, "est la capitale de ", board)
            print(row)


board_instance = Board()
board_instance.get_capitale('Imperium')