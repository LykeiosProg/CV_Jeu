import heros

class Move:
    def moving(self, Heros_move_x, Heros_move_y):
        self.x = self.x + Heros_move_x
        self.y = self.y + Heros_move_y

Heros = Move()
Heros.x = 1
Heros.y = 1
print("Heros: x =", Heros.x, "y =", Heros.y)
Heros.moving(2,5)
print("Heros: x =", Heros.x, "y =", Heros.y)