import hashlib
import streamlit as st
st.title("Block Chain Simple Demonstration to prove Data Integrity")
t1 = st.text_input("Enter text1")
t2 = st.text_input("Enter text2")
t3 = st.text_input("Enter text3")
t4 = st.text_input("Enter text4")
class GeekCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



block1 = GeekCoinBlock('firstblock', [t1,t2])

print(f"Block 1 data: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")

block2 = GeekCoinBlock(block1.block_hash, [t3, t4])

print(f"Block 2 data: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")
if (t1!='' and t2!='' and t3!='' and t4!=''):
    st.write("Block 1 data:", block1.block_data)
    st.write("Block 1 hash:", block1.block_hash)
    st.write("Block 2 data:", block2.block_data)
    st.write("Block 2 hash:", block2.block_hash)
