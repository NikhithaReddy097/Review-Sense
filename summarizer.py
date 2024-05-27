from langchain_community.llms import LlamaCpp

MODEL_PATH = "DL-model\summarizer_model.gguf"

def get_llm():
    llm = LlamaCpp(
        model_path=MODEL_PATH,
        n_gpu_layers=30,
        n_batch=256,
        verbose=True,
        n_ctx = 10000,
    )
    return llm