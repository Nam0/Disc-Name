import gpt_2_simple as gpt2

data_file = r"C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\CombinedDataset.txt"

checkpoint_dir = r"C:\Users\Namo\Documents\GitHub\Disc-Name\New\checkpoint\AiName"

sess = gpt2.start_tf_sess()

gpt2.finetune(
    sess=sess,
    dataset= data_file, 
    model_name='124M',
    steps=1000,  
    restore_from='AiName_new', 
    checkpoint_dir=checkpoint_dir, 
    run_name='AiName_new', 
    print_every=10,
    sample_every=200,
    save_every=500,
    overwrite=True 
)
