import pygame 
from time import sleep
class Shape(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def draw(self):
        raise NotImplementedError()

    def move(self, dir):
        if dir == 'up':
            self.y -= 5
        elif dir == 'down':
            self.y += 5
        elif dir == 'left':
            self.x -= 5 
        elif dir == 'right':
            self.x += 5 

    @staticmethod
    def factory(type):
        if type == 'circle':
            return Circle(100, 100)
        if type  == 'square':
            return Square(100, 100)
        if type == 'triangle':
            return Triangle(100, 100)
        assert 0, 'Bad shape requested: ' + type

class Square(Shape):
    def draw(self):
        pygame.draw.rect(
            surface=screen,
            color = (255, 255, 0),
            rect = pygame.Rect(self.x, self.y, 25, 25)
        )
class Triangle(Shape):
    def draw(self):
        pygame.draw.polygon(
            surface=screen,
            color=(150, 160, 150),
            points=[(self.x, self.y), (self.x+24, self.y), (self.x+12, self.y-24)]  
        )

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(
            surface=screen,
            color=(0, 255, 255),
            center=(self.x, self.y),
            radius=12
        )


if __name__ == '__main__':
    window_dim = 700, 700
    screen = pygame.display.set_mode(window_dim)
    obj = Shape.factory('square')
    player_quits = False 
    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True 

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]: 
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')

            if pressed[pygame.K_s]:
                obj = Shape.factory('square')
            if pressed[pygame.K_t]:
                obj = Shape.factory('triangle')
            if pressed[pygame.K_c]:
                obj = Shape.factory('circle')

            screen.fill((0,0,0))
            obj.draw()
        pygame.display.flip()
