# Lifecycle and Compatibility v1

## Lifecycle hooks

Supported hooks:

- `on_install`
- `on_enable`
- `on_disable`
- `on_upgrade`
- `on_uninstall`

## Hook rules

- hooks run in a framework-managed context
- hooks are audited
- hooks have timeout policy
- failed `on_enable` blocks activation
- failed `on_upgrade` blocks upgrade and may trigger rollback or disabled state

## Compatibility model

### Platform API version

- plugin declares `api_version`
- kernel exposes supported versions
- unsupported version blocks load

### Framework version range

- plugin declares compatible framework range
- kernel validates at install/startup

### Dependency compatibility

- required dependency must exist and match version constraints
- optional dependency may be absent
- circular dependencies are forbidden

## Deprecation policy

- mark public API as deprecated first
- maintain compatibility through one major cycle where feasible
- remove later with migration notes

## Breaking change rule

Any breaking change to the public extension API requires:

- API version bump
- migration guidance
- explicit compatibility validation

