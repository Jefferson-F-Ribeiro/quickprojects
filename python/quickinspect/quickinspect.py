import psutil
import platform
import gpuinfo

def get_cpu_info():
    return f"Processador: {platform.processor()}, Arquitetura: {platform.architecture()[0]}, Núcleos: {psutil.cpu_count(logical=False)}, Threads: {psutil.cpu_count()}"

def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    return f"Memória RAM Total: {virtual_memory.total / (1024 ** 3):.2f} GB, Livre: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB disponíveis"

def get_gpu_info():
    try:
        gpus = gpuinfo.get_info()
        if gpus:
            return f"Placa de Vídeo: {gpus[0]['name']}"
    except Exception as e:
        return "Não foi possível obter informações da placa de vídeo"

if __name__ == "__main__":
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    gpu_info = get_gpu_info()

    print(cpu_info)
    print(memory_info)
    print(gpu_info)
