ARG PYTHON_IMAGE
ARG PYTHON_IMAGE_VERSION

FROM ${PYTHON_IMAGE}:${PYTHON_IMAGE_VERSION}

WORKDIR /opt/rsrc_web

COPY rsrc_web/ rsrc_web/
COPY tests/ tests/
COPY README.md .
COPY requirements-tests.txt .
COPY requirements.txt .
COPY setup.py .
COPY setup.cfg .

RUN pip install -r requirements-tests.txt
RUN pip install -r requirements.txt
RUN pip install -e .
