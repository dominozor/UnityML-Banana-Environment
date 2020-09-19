[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Navigation

### Introduction

We will train an agent to navigate that collects bananas in a large, square world surrended with walls.  

![Trained Agent][image1]

## Rewards
- **`+1`** - collecting a yellow banana
- **`-1`** - collecting a blue banana

## State Space
The state space has 37 dimensions
The velocity in all probability has two dimensions, the remaining 35 dimensions are describing the banana environment. Ray based perception means, instead of using pixels as projections, ray trajectories are used to determine the objects at agent's forward direction.

- **Ray Perception (35)**

    7 rays projecting from the agent at the following angles (and returned in this order):
    
    [20, 90, 160, 45, 135, 70, 110] # 90 is directly in front of the agent

- **Ray (5)**

    Each ray is projected into the scene. If it encounters one of four detectable objects the value at that position in the array is set to 1. Finally there is a distance measure which is a fraction of the ray length.
    
    [Banana, Wall, BadBanana, Agent, Distance]
    
    for example;
    
    [0, 1, 1, 0, 0.2]
    
    There is a BadBanana detected 20% of the way along the ray and a wall behind it.

## Action Space
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

## Goal of the Environment
The task is episodic, and in order to solve the environment, agent must get an average score of +13 over 100 consecutive episodes.

### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

2. Place the file in the project folder, and unzip (or decompress) the file. 

### Model

There is a pre-trained model which is Double Dueling DQN for now. You can see details from `Report.pdf` 

### Starting Project Environment
You can see the conda environment library list from `banana.env`.

Project can be run by starting Jupiter Notebook first:

`jupiter notebook /path/to/project/folder`


### Training

Follow the instructions in `Navigation_Train.ipynb` to get started with training the model from scratch (maybe with adding your own changes) 

### Testing 

If you want to test pre-created model, you should follow the instructions in `Navigation_Test.ipynb` 
