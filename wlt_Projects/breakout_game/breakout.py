from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    breaking_game = BreakoutGraphics()
    chance = NUM_LIVES
    score = 0
    while True:
        '''
        To end this game:
        1. crack every bricks
        2. loses 3 chances
        '''
        if chance == 0 or score == breaking_game.num_of_brick:
            break
        '''
        To start this game:
        Click th mouse
        '''
        if breaking_game.switch:
            vx = breaking_game.get_ball_vx()
            vy = breaking_game.get_ball_vy()
            while True:
                breaking_game.ball.move(vx, vy)
                # when the ball hit the wall
                if breaking_game.ball.x+breaking_game.ball.width > breaking_game.window.width \
                        or breaking_game.ball.x < 0:
                    vx = -vx
                # when the ball hit the ceiling
                elif breaking_game.ball.y < 0:
                    vy = -vy
                elif breaking_game.ball.y > breaking_game.window.height:
                    breaking_game.window.remove(breaking_game.ball)
                    breaking_game.switch = False
                    # need to reset the position of the ball, then regenerate
                    breaking_game.reset_ball()
                    breaking_game.window.add(breaking_game.ball)
                    chance -= 1
                    break
                '''
                there are 4 parts need to detect:
                ball.x, ball.y
                ball.x+ball.width, ball.y
                ball.x, ball.y+ball.height
                ball.x+ball.width, ball.y+ball.height
                
                '''
                hit_stuff_1 = breaking_game.window.get_object_at(breaking_game.ball.x, breaking_game.ball.y)
                hit_stuff_2 = breaking_game.window.get_object_at(breaking_game.ball.x+breaking_game.ball.width,
                                                                 breaking_game.ball.y)
                hit_stuff_3 = breaking_game.window.get_object_at(breaking_game.ball.x,
                                                                 breaking_game.ball.y+breaking_game.ball.height)
                hit_stuff_4 = breaking_game.window.get_object_at(breaking_game.ball.x+breaking_game.ball.width,
                                                                 breaking_game.ball.y+breaking_game.ball.height)
                if hit_stuff_1 is not None and hit_stuff_1 is not breaking_game.paddle:
                    breaking_game.window.remove(hit_stuff_1)
                    score += 1
                    vy = -vy
                elif hit_stuff_2 is not None and hit_stuff_2 is not breaking_game.paddle:
                    breaking_game.window.remove(hit_stuff_2)
                    score += 1
                    vy = -vy
                elif hit_stuff_3 is not None and hit_stuff_3 is not breaking_game.paddle:
                    breaking_game.window.remove(hit_stuff_3)
                    score += 1
                    vy = -vy
                elif hit_stuff_4 is not None and hit_stuff_4 is not breaking_game.paddle:
                    breaking_game.window.remove(hit_stuff_4)
                    score += 1
                    vy = -vy
                # only the bottom can hit the paddle and bounce back
                elif hit_stuff_3 is breaking_game.paddle or hit_stuff_4 is breaking_game.paddle:
                    if vy > 0:
                        vy = -vy
                pause(FRAME_RATE)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
