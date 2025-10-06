# zeus-plugin-registry

This repository maintains a list of plugins which are made available in the Zeus C2 system's plugin manager.

## Plugin schema

Plugins are added manually to the `plugins.yml` file. Each plugin in the list must conform to the following schema:

- `name` (String): A human-readable name for the plugin, displayed in Zeus UI
- `repository` (String): A git repository URL to pull the plugin source code from.
- `ref` (String) The git commit hash to use when pulling the plugin source code.

At build time, `plugins.yml` is transformed into a machine-readable build output (see blow).

## Build & deployment process

During its CI build, this repository performs several steps on the `plugins.yml` file, to make it ready for distribution to Zeus C2 nodes:

- The validity of the `plugins.yml` file is checked
- In order, each of the plugins is built:
  - The git repository is checked out.
  - The docker container is built
- All plugins are uploaded to the internal Zydro registry
- A single `plugins.json` file is generated and uploaded to the production API