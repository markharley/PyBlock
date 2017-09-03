# PyBlock
Simply python blockchain

# TODO
1. Use more interesting proof-of-work
2. Add transaction verification
3. Wallets
4. Write basic client
5. Block broadcasting
6. Transaction broadcasting - think about consistency and commiting of transactions
6. Peer announcement and discovery
   - Have a new node announce itself to the node from which is pulls the blockchain before it starts mining
   - Have nodes broadcast new nodes to its peers
7. Think about concurrency issues. Maybe want to rewrite in C++ with threading, mutex on blockchain, etc.
8. Separate logic from networking protocol so we can replace http if we want to later


# Interesting future stuff
1. Have a play with attacks on the chain. E.g., try to create a very long, seemingly valid, chain which could supersede the real chain
2. Think about generalising to have multiple PoWs on the same chain
