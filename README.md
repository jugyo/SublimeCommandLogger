CommandLogger
====

Sublime Text Plugin for command logging.

## Keymap

```javascript
[
  { "keys": ["super+k", "super+c"], "command": "command_log"},
]
```

## Setting

i.e.

```javascript
{
  "command_logger_ignore_pattern": "^(move|drag_select|command_log)$",
  "command_logger_history_size": 1000
}
```
