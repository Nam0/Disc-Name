import torch

def print_memory_usage():
    print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 2:.2f} MB")
    print(f"Cached: {torch.cuda.memory_reserved() / 1024 ** 2:.2f} MB")
    print(f"Max Allocated: {torch.cuda.max_memory_allocated() / 1024 ** 2:.2f} MB")
    print(f"Max Cached: {torch.cuda.max_memory_reserved() / 1024 ** 2:.2f} MB")

print_memory_usage()
