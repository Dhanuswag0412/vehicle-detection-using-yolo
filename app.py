import sys
import os
import streamlit.web.cli as stcli

def run_app():
    # Find the path of gui.py relative to this file
    gui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vehicle_detection", "gui.py")
    sys.argv = ["streamlit", "run", gui_path]
    sys.exit(stcli.main())

if __name__ == "__main__":
    run_app()