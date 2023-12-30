from ursina import *

# objects are created mainly through the use of OOP

class Shape(Entity):
	def __init__(self, model, position):
		super().__init__(
			parent = scene,
			model = model,
			position = position,
			texture = 'brick')
	def update(self):
		speed = 5
		if held_keys['a']:
			self.x -= speed * time.dt
			self.rotation_y -= speed
		if held_keys['s']:
			self.y -= speed * time.dt
			self.rotation_x -= speed
		if held_keys['w']:
			self.y += speed * time.dt 
			self.rotation_x += speed
		if held_keys['d']:
			self.x += speed * time.dt
			self.rotation_y += speed

# update is run every frame
def update():
	punch_sound.play()

app = Ursina() # instance of Application

cubeone = Shape('cube', (1,2))
cubetwo = Shape('cube', (2,1))

punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)

app.run() # running the application
