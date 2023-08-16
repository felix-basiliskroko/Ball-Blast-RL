import gym
from gym.spaces import Tuple, Box, Discrete
import numpy as np
import pyautogui


class BallBlastEnv(gym.Env):
    def __init__(self, border_left, border_right):
        super(BallBlastEnv, self).__init__()

        action_space = Tuple([
            Discrete(border_right - border_left),  # X Coordinate of the window
            Box(low=0, high=1, shape=(1,))  # Speed of the respective action
        ])

        observation_space = Box(low=0, high=255, shape=(782, 1160, 1), dtype=np.uint8)

        self.game_over = False
        self.state = self.__get_screenshot()

    def reset(self):
        self.__reset_level()

    def step(self, action):
        reward = None
        done = None

        if self.state[0]:  # Level complete
            self.__reset_level()
            return None, 5, True, {}

        # ...

        self.state = self.__get_screenshot()
        state = self.state

        return state, reward, done, {}

    def render(self, mode='human'):
        return None  # No need for rendering, i think

    def __reset_level(self):
        return None

    def __get_screenshot(self):
        img = pyautogui.screenshot(region=(2544, 55, 900, 1300))
        img = img.crop((0, 0, img.width - 118, img.height - 140))  # crop image
        skip_button = img.crop((120, 1160 - 20, 320, 1160))  # "Skip Button" - To check if level is over lol
        # TODO method should also return flag whether or not the level is finished (using the Skip Button)
        grayscale_img = img.convert('L')  # convert to grayscale
        return grayscale_img

    def __yield_reward(self):
        # TODO Implement adequate reward function, maybe some CNN that determines the score, as well as the earned money per timestep
        return None
