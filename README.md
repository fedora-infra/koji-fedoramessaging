# koji-fedoramessaging

Koji plugin to send messages on fedora-messaging

The messaging schemas are located at

https://github.com/fedora-infra/koji-fedoramessaging-messages/

## Configuration

The plugin reads its configuration from the
[fedora-messaging](https://fedora-messaging.readthedocs.io) configuration file, usually
`/etc/fedora-messaging/config.toml`:

```toml
[consumer_config]
# Name of this Koji instance, sent in the "instance" field of every message.
# It is what distinguishes messages from the primary hub and messages from the
# secondary hubs. Defaults to "primary".
koji_instance = "primary"
```

The configuration is loaded once per hub process, so restart the hub after changing it.
