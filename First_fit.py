# Define the memory blocks and processes
memory_blocks = [150, 550, 250, 350, 650]  # Initial memory block sizes
processes = [262, 467, 162, 476]  # Processes and their memory requirements

# Allocate memory using First Fit
def first_fit(memory_blocks, processes):
    # Create a list to store the allocation for each process (-1 indicates unallocated)
    allocation = [-1] * len(processes)

    for i, process in enumerate(processes):
        for j, block in enumerate(memory_blocks):
            # If the block can accommodate the process
            if block >= process:
                allocation[i] = j  # Allocate the block to the process
                memory_blocks[j] -= process  # Reduce the size of the block
                break  # Move to the next process

    return allocation, memory_blocks

# Run the first fit allocation
allocation, remaining_blocks = first_fit(memory_blocks, processes)

# Display results
print("Process Allocation:")
for i, block in enumerate(allocation):
    if block != -1:
        print(f"Process {i+1} (Size: {processes[i]} KB) -> Block {block+1}")
    else:
        print(f"Process {i+1} (Size: {processes[i]} KB) -> Not Allocated")

print("\nRemaining Memory Blocks:")
for i, block in enumerate(remaining_blocks):
    print(f"Block {i+1}: {block} KB")
