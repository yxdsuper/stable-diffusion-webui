import gradio as gr
from fastapi import FastAPI
from scripts.model_util import lora_models, MAX_MODEL_COUNT


def lora_api(_: gr.Blocks, app: FastAPI):
    @app.get("/lora/version")
    async def version():
        return {"version": '1'}

    @app.get("/lora/models")
    async def models():
        return {'count': MAX_MODEL_COUNT, 'list': list(lora_models.keys())}


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(lora_api)
except:
    pass
