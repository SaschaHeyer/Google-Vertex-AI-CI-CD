from typing import NamedTuple
from kfp.components import create_component_from_func

def reverse(a: str)->NamedTuple("outputs", [("before", str), ("after", str)]):
  return a, a[::-1]

if __name__ == '__main__':
    reverse_op = create_component_from_func(
        reverse,
        output_component_file='component.yaml',
        annotations={
            "author": "Sascha Heyer"
        }
    )