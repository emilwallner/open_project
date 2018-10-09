import torch

# Hardware usage
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MULTIPROCESSING = True

# Neural network
LR = 0.01

# DQN parameters
REPLAY_BUFFER_SIZE = 100000
LEARNING_STARTS = 100
LEARNING_FREQ = 4
BATCH_SIZE = 32
GAMMA = 0.99
# Epsilon is scheduled
TARGET_UPDATE_FREQ = 1000


# Logging parameter
LOG_FREQ = 100
ASSESS_FREQ = 50
SAVE_FREQ = 5000 #Not implemented yet

# Toy Corewar settings
NUM_ACTIONS = 225
NUM_REGISTERS = 4
MAX_LENGTH = 5
N_INSTRUCTIONS = 4
N_VARS = 3
N_VALS = 20
N_TARGETS = 4