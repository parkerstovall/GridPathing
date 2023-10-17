import gymnasium as gym
import GridManager as gm


class BigBrainEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    sides = 2

    def __init__(self, env_config=None):

        if env_config and env_config["sides"]:
            self.sides = env_config["sides"]

        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Dict({
            "row": gym.spaces.Discrete(self.sides),
            "col": gym.spaces.Discrete(self.sides),
        })
        self.max_steps = (self.sides ** 2) - 1
        self.info = {'path': []}
        self.up = 0
        self.right = 1
        self.down = 2
        self.left = 3
        self.reset()

    def get_obs(self):
        return {"row": self.row, "col": self.col}

    def reset(self, *, seed=None, options=None):
        self.count = 0
        self.info = {'path': []}
        self.board, self.row, self.col = gm.build_board(self.sides, False)
        self.observation = self.get_obs()
        self.reward = 0
        self.done = False
        return self.observation, {}

    def step(self, action):
        assert self.action_space.contains(action)

        dir = None

        if action == self.up:
            dir = 'w'
        elif action == self.right:
            dir = 'd'
        elif action == self.down:
            dir = 's'
        elif action == self.left:
            dir = 'a'
        # gm.print_board(self.board, self.row, self.col)
        if gm.can_move(dir, self.row, self.col, self.board, False):
            self.board, self.row, self.col, score = gm.make_move(
                dir,
                self.board,
                self.row,
                self.col
            )

            self.reward = score
            self.observation = self.get_obs()
        else:
            self.reward = -1

        self.count += 1
        self.info["path"].append(dir)
        self.info["score"] = self.reward
        self.info["board"] = self.board
        self.info["row"] = self.row
        self.info["col"] = self.col

        if self.count == self.max_steps:
            self.done = True

        return self.observation, self.reward, self.done, self.done, self.info

    def render(self):
        obs = self.get_obs()
        return obs

    def close(self):
        pass
