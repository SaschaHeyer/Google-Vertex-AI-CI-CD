from kfp.v2.dsl import pipeline
from kfp.v2 import compiler

import kfp.components as comp

@pipeline(name="basic-pipeline",
description="A simple intro pipeline", 
              pipeline_root='gs://doit-vertex-ai-demo/basic-pipeine')
def basic_pipeline(a: str='stres', b: str='sed'):
    reverse_op = comp.load_component_from_file("../components/reverse/component.yaml")
    reverse_task = reverse_op("aabb")

if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=basic_pipeline, package_path="basic_pipeline.json"
    )