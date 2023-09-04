# Connexion à la base de données

1. dans un terminal externe, rentrer la commande suivante<br>
```
ssh -L 1521:info-atchoum.iut.bx:1521 \<idnum>@info-ssh1.iut.u-bordeaux.fr -p 6666
```

2. le script pour se connecter à la base :

```
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
            
    def get_capitale(self, board):
        sql_query = f"""SELECT t.MAP_CAPITAL.CITY_NAME AS CAPITAL FROM T_Concordia, TABLE(T_Concordia.concordia_map) t WHERE t.map_name='{board}'"""
        self.cursor.execute(sql_query)

        for row in self.cursor:
            capitale = row[0]
            print("Capitale", capitale, "est la capitale de ", board)
            print(row)


board_instance = Board()
board_instance.get_capitale('Imperium')
```