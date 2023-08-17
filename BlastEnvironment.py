import gymnasium as gym
from gymnasium.spaces import Tuple, Box, Discrete
import numpy as np
import pyautogui
from CustomInteraction import drag_mouse


class BallBlastEnv(gym.Env):
    def __init__(self, border_left, border_right):
        super(BallBlastEnv, self).__init__()

        action_space = Tuple([
            Discrete(border_right - border_left),  # X Coordinate of the window
            Box(low=0, high=1, shape=(1,))  # Speed of the respective action
        ])

        observation_space = Box(low=0, high=255, shape=(782, 1160, 1), dtype=np.uint8)

        self.border_right = border_right
        self.border_left = border_left
        self.game_over = False
        self.state = self._get_screenshot()
        self.curr_x = int((border_right - border_left) / 2)  # Set initial position (center of screen)

    def reset(self, seed=None, optione=None):
        super().reset(seed=seed)

    def step(self, action):
        reward = None
        done = None

        if self.state[0]:  # Level complete
            self.__reset_level()
            return None, 3, True, {}
        elif self._is_failed():
        else:  # Level incomplete
            drag_mouse(curr_x=self.curr_x, new_x=action[0], speed=action[1])  # adjust x position
            self.curr_x = action[0]  # adjust new current position
        # ...

        self.state = self._get_screenshot()
        state = self.state

        return state, reward, done, {}

    def render(self, mode='human'):
        return None  # No need for rendering, i think

    def _get_screenshot(self):
        img = pyautogui.screenshot(region=(2544, 55, 900, 1300))
        img = img.crop((0, 0, img.width - 118, img.height - 140))  # crop image
        skip_button = img.crop((120, 1160 - 20, 320, 1160))  # "Skip Button" - To check if level is over lol
        # TODO method should also return flag whether or not the level is finished (using the Skip Button)
        return img.convert('L')  # convert to grayscale

    def _init_mousepos(self):
        return int((self.border_right - self.border_left) / 2)

    def __yield_reward(self):
        # TODO Implement adequate reward function, maybe some CNN that determines the score, as well as the earned
        #  money per timestep
        return None

    def _is_failed(self):
        # TODO Implement method that determines whether or not the canon as colided with a ball (level failed)
        return None
