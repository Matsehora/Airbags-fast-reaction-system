import struct
import time

def send_three_longs_to_cpp(long1, long2, long3):
    """Sends three long integers (8 bytes each) to a text file."""
    with open("../Temp_shared_memory/3_long.txt", "wb") as file:
        file.write(struct.pack("qqq", long1, long2, long3))  # Ensure 8-byte longs
        print("qqq", long1, long2, long3)


def receive_floats_from_cpp():
    """Receives two float values from a text file."""
    try:
        with open("../Temp_shared_memory/2_float.txt", "rb") as file:
            data = file.read(8)  # Read two floats (4+4 bytes)
            if len(data) == 8:
                lat, long = struct.unpack("ff", data)
                return long, lat  # Swap order to match original function
    except FileNotFoundError:
        print("Error: 2_float.txt not found.")
    return long, lat
