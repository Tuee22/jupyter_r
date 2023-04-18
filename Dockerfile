FROM jupyter/r-notebook
RUN python3 -m pip install --upgrade pip wheel setuptools
RUN python3 -m pip install pandas openpyxl