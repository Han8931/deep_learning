
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def print_args(args):
    """
    Print all arguments in argparser
    """

    if args.device == "cuda":
        current_gpu = torch.cuda.current_device()
        gpu_name = torch.cuda.get_device_name(current_gpu)

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    now = datetime.datetime.now()
    print(f"||Experiment Date:{now.year}-{now.month}-{now.day}||")

    print("Arguments List: \n")
    if args.device == "cuda":
        print(f"- Running on GPU: {gpu_name} || GPU Idx: {os.environ['CUDA_VISIBLE_DEVICES']}")
    else:
        print(f"- Running on CPU")
    for arg in vars(args):
        print(f"- {arg}: {getattr(args, arg)}")

    print("---------------------------------------------------------")
    print("---------------------------------------------------------\n")
