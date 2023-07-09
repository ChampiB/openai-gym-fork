import os.path
import sys
import itertools

from setuptools import find_packages, setup

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gym"))
from version import VERSION

# Environment-specific dependencies.
extras = {}

# Meta dependency groups.
nomujoco_blacklist = set(["mujoco", "robotics", "accept-rom-license"])
nomujoco_groups = set(extras.keys()) - nomujoco_blacklist

extras["nomujoco"] = list(
    itertools.chain.from_iterable(map(lambda group: extras[group], nomujoco_groups))
)


all_blacklist = set(["accept-rom-license"])
all_groups = set(extras.keys()) - all_blacklist

extras["all"] = list(
    itertools.chain.from_iterable(map(lambda group: extras[group], all_groups))
)

setup(
    name="gym",
    version=VERSION,
    description="Gym: A universal API for reinforcement learning environments.",
    url="https://github.com/openai/gym",
    author="OpenAI",
    author_email="jkterry@umd.edu",
    license="",
    packages=[package for package in find_packages() if package.startswith("gym")],
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.0",
        "cloudpickle>=1.2.0",
        "importlib_metadata>=4.8.1; python_version < '3.8'",
    ],
    extras_require=extras,
    package_data={
        "gym": [
            "envs/mujoco/assets/*.xml",
            "envs/classic_control/assets/*.png",
            "envs/robotics/assets/LICENSE.md",
            "envs/robotics/assets/fetch/*.xml",
            "envs/robotics/assets/hand/*.xml",
            "envs/robotics/assets/stls/fetch/*.stl",
            "envs/robotics/assets/stls/hand/*.stl",
            "envs/robotics/assets/textures/*.png",
        ]
    },
    tests_require=["pytest", "mock"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
