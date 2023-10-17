import ray
import ray.tune
from ray.rllib.algorithms.ppo import PPO
from BigBrainEnv import BigBrainEnv


class BigBrain:
    def __init__(self):
        pass

    def get_agent(self, max_moves, sides):
        config = {
            "env": BigBrainEnv,
            "env_config": {
                "sides": sides,
            },
            "framework": "torch",
            "model": {
                "fcnet_hiddens": [32],
                "fcnet_activation": "linear",
            },
        }

        stop = {"episode_reward_min": max_moves}
        ray.shutdown()
        ray.init(
            num_cpus=3,
            include_dashboard=False,
            ignore_reinit_error=True,
            log_to_driver=False,
        )

        analysis = ray.tune.run(
            "PPO",
            config=config,
            stop=stop,
            checkpoint_at_end=True,
        )

        trial = analysis.get_best_trial("episode_reward_mean", "max")
        checkpoint = analysis.get_best_checkpoint(
            trial,
            "training_iteration",
            "max",
        )

        agent = PPO(config=config)
        agent.restore(checkpoint)
        return agent

    def solve(self, max_moves, sides):
        print('Training agent...')
        agent = self.get_agent(max_moves, sides)
        env = BigBrainEnv()
        obs, info = env.reset()
        print('\n\n\nAgent Trained, time to solve:')
        done = False

        while not done:
            action = agent.compute_single_action(observation=obs)
            obs, reward, done, truncated, info = env.step(action)

        env.close()
        ray.shutdown()
        return str(info['path'])
