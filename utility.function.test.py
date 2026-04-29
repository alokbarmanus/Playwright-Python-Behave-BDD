from features.utilities.memory_manager import MemoryManager

def sample_memory_usage():
    memory = MemoryManager()
    # Set a value
    memory.set('username', 'test_user')
    # Retrieve the value
    user = memory.get('username')
    print(f"Username from memory: {user}")
    # Set another value
    memory.set('session_id', 12345)
    # Retrieve another value
    session = memory.get('session_id')
    print(f"Session ID from memory: {session}")
    # Clear memory
    memory.clear()
    print(f"After clear, username: {memory.get('username')}")

if __name__ == "__main__":
    sample_memory_usage()
