---
icon: package
label: json
---

### `json.loads(s)`

Decode a JSON string into a python object.

It is supported by the `eval()` function.

### `json.dumps(obj)`

Encode a python object into a JSON string.

It is supported by the compiler with `JSON_MODE` enabled.

!!!
There is a special method `__json__`.
If defined, it will be called when `json.dumps()` is called.
!!!