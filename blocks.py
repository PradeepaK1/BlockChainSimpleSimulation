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


t11='sun'
t22='moon'
t33='earth'
t44='mars'
block3 = GeekCoinBlock('firstblock', [t11, t22])
block4 = GeekCoinBlock(block3.block_hash, [t33, t44])
if(block1.block_data==block3.block_data and block2.block_hash==block4.block_hash):
    st.write("Data Integrity Verified, Data Valid(Same as encoded data)")
    st.write("Block 1 data:", block1.block_data)
    st.write("Block 1 hash:", block1.block_hash)    
    st.write("Block 3 data:", block3.block_data)
    st.write("Block 3 hash:", block3.block_hash)
    st.write("Block 2 data:", block2.block_data)
    st.write("Block 2 hash:", block2.block_hash)    
    st.write("Block 4 data:", block4.block_data)
    st.write("Block 4 hash:", block4.block_hash)
else:
    st.write("Data Integrity Not Verified, Data Invalid(Not same as encoded data)")
    st.write("Data Integrity Verified, Data Valid(Same as encoded data)")
    st.write("Block 1 data:", block1.block_data)
    st.write("Block 1 hash:", block1.block_hash)    
    st.write("Block 3 data:", block3.block_data)
    st.write("Block 3 hash:", block3.block_hash)
    st.write("Block 2 data:", block2.block_data)
    st.write("Block 2 hash:", block2.block_hash)    
    st.write("Block 4 data:", block4.block_data)
    st.write("Block 4 hash:", block4.block_hash)
