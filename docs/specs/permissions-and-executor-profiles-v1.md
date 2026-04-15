# Permissions and Executor Profiles v1

## Permission model

Permissions are deny-by-default.

Each plugin declares requested permissions in its manifest.

The kernel validates and grants only allowed scopes.

## Permission categories

### Filesystem
- read scopes
- write scopes
- append scopes
- edit scopes
- delete scopes

### Shell
- executor profile
- command policy group

### Network
- allowed hosts
- allowed protocols
- blocked destinations

### Models
- local models
- remote models
- premium models
- embeddings access
- vision/audio access

### Odoo
- environment
- host
- model scopes
- operation scopes

### Memory
- readable scopes
- writable scopes

### Knowledge
- readable namespaces
- writable namespaces
- ingestion rights

### Audit
- emit structured events
- read audit views or not

## Executor profiles

### `read_only`
- no shell
- no writes

### `workspace_safe`
- shell allowed
- workspace only
- no host writes

### `workspace_dev`
- shell allowed
- tests allowed
- patch generation allowed
- no git push
- no host delete

### `bounded_live_write`
- append/edit inside approved scopes
- approval required by policy

## Rules

- plugins request profiles
- kernel grants profiles
- runtime enforces profile constraints
- profile violations are audited and blocked

