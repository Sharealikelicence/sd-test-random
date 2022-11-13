# Use slim image as base to reduce the image size and possible security vulnerability attack surfaces. Also, add image digest for deterministic build.
FROM python:3.11.0-slim@sha256:f8cc89f5e47347703ec0c2b755464d7db2fa16f255ab860c4b24ba6ef2402020

# Suppress root user warning when upgrading pip.
RUN pip install --root-user-action=ignore --upgrade pip

# Add non-privileged user with specific UID/GID as they would be undeterministic otherwise.
RUN groupadd -g 1000 -r sdtr && useradd -u 1000 -m -r -g sdtr sdtr
USER sdtr

WORKDIR /home/sdtr

# Install required modules as user.
COPY --chown=sdtr:sdtr requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

ENV PATH="/home/sdtr/.local/bin:${PATH}"

# Copy all remaining files at the end so that the previous build layers can be reused more readily.
COPY --chown=sdtr:sdtr . .

CMD [ "python", "./main.py" ]
