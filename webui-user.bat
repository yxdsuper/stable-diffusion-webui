@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--skip-torch-cuda-test --gradio-debug --gradio-auth u1:p1,u2:p2,u3:p3

call webui.bat
