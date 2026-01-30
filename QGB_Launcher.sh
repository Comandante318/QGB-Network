#!/bin/bash
python3 blockchain.py &
streamlit run app.py --server.headless true
