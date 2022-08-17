from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)/2, y=window_height/2-ball_radius/2)
        self.ball.filled = True
        self.ball.fill_color = 'navy'
        self.ball.color = 'navy'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__ball_vx = 0
        self.__ball_vy = 0
        self.switch = False

        # Initialize our mouse listeners
        onmousemoved(self.when_mouse_move)
        onmouseclicked(self.when_mouse_click)

        # Draw bricks
        self.num_of_brick = brick_cols*brick_rows
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=j*(brick_width+brick_spacing),
                              y=brick_offset+i*(brick_height+brick_spacing))
                brick.filled = True
                if i <= 1:
                    brick.fill_color = 'Red'
                elif i <= 3:
                    brick.fill_color = 'Orange'
                elif i <= 5:
                    brick.fill_color = 'Yellow'
                elif i <= 7:
                    brick.fill_color = 'Green'
                elif i <= 9:
                    brick.fill_color = 'Blue'
                self.window.add(brick)

    # Velocity getter
    def get_ball_vx(self):
        return self.__ball_vx

    def get_ball_vy(self):
        return self.__ball_vy

    def when_mouse_move(self, mouse):
        if mouse.x < self.paddle.width:
            self.paddle.x = 0
        elif mouse.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x-self.paddle.width

    def when_mouse_click(self, mouse):
        self.switch = True
        self.__ball_vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__ball_vx = -self.__ball_vx
        self.__ball_vy = INITIAL_Y_SPEED

    def reset_ball(self):
        self.ball.x = (self.window.width-self.ball.width/2)/2
        self.ball.y = (self.window.height-self.ball.height/2)/2