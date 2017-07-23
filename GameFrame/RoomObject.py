
class RoomObject:

    def __init__(self, room, x, y):
        self.room = room
        self.depth = 0
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.width = 0
        self.height = 0
        self.image = 0
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0
        self.handle_key_events = False
        self.handle_mouse_events = False

        self.collision_object_types = set()
        self.collision_objects = []

    def set_image(self, image):
        self.image = image

    def register_collision_object(self, collision_object):
        self.collision_object_types.add(collision_object)

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def delete_object(self, obj):
        self.room.delete_object(obj)

    def remove_object(self, obj):
        for index, list_obj in enumerate(self.collision_objects):
            if list_obj is obj:
                self.collision_objects.pop(index)

    def step(self):
        pass

    def check_collisions(self):
        for item in self.collision_objects:
            if self.rect.colliderect(item.rect):
                self.handle_collision(item)

    def handle_collision(self, other):
        pass

    def key_pressed(self, key):
        pass

    def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right):
        pass

    def bounce(self, other):

        # self is to the side of other
        if other.rect.top < self.rect.centery < other.rect.bottom:
            self.x_speed *= -1

        # self is above or below other
        if other.rect.left < self.rect.centerx < other.rect.right:
            self.y_speed *= -1

    def blocked(self):

        self.x = self.prev_x
        self.y = self.prev_y
