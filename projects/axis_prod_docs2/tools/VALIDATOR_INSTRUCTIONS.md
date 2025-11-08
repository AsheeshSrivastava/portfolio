# Validator
To validate CanonicalContent JSON locally:
1) `pip install jsonschema`
2) Run a snippet similar to:

```python
from jsonschema import Draft202012Validator
import json
schema = json.load(open('contracts/canonical_content.schema.json'))
doc = json.load(open('canonical/numpy-broadcasting-basics@1.0.0.json'))
Draft202012Validator(schema).validate(doc)
print('VALID')
```
