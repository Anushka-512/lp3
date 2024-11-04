import heapq
from collections import defaultdict, namedtuple

# Define a namedtuple for the nodes in the Huffman tree
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encoding(s):
    # Count the frequency of each character
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1

    # Build a priority queue (min-heap)
    h = []
    for ch, freq in freq.items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    # Build the Huffman tree using a greedy strategy
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    # Generate the Huffman codes by walking the tree
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

# Main program loop
while True:
    s = input("Enter the string to encode using Huffman Encoding: ")
    if not s:
        print("Please enter a valid non-empty string.")
        continue

    # Get Huffman encoding for the input string
    huffman_code = huffman_encoding(s)

    # Display Huffman codes
    print("Character with their corresponding Huffman Codes:")
    for ch in sorted(huffman_code):
        print(f"{ch}: {huffman_code[ch]}")

    # Check if the user wants to continue or exit
    choice = input("Do you want to encode another string? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting program.")
        break
