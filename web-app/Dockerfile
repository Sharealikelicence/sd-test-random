# Use image digest for deterministic build.
FROM node:19.0.1@sha256:6da4e30e3952e460fe4ad256e46a8b79acce46dd596bbe4ef882d5ec0d1ef6cb

# Add non-privileged user with specific UID/GID as they would be undeterministic otherwise.
RUN groupadd -g 1001 -r webapp && useradd -u 1001 -m -r -g webapp webapp
USER webapp

WORKDIR /home/webapp

COPY --chown=webapp:webapp . .

CMD ["npm", "start"]
