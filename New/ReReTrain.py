import os
import logging
import tensorflow as tf  
# Must be above gpt2 import
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.ERROR)
import gpt_2_simple as gpt2

def train_model():
    new_training_data_path = 'Data/NewData/reformatted_data.txt'  
    
    with open(new_training_data_path, 'r', encoding='utf-8') as f:
        new_data = f.read()
    
    with open('temp_training_data.txt', 'w', encoding='utf-8') as f:
        f.write(new_data)
    
    with tf.compat.v1.variable_scope(tf.compat.v1.get_variable_scope(), reuse=tf.compat.v1.AUTO_REUSE):
        gpt2.finetune(sess,
                      dataset='temp_training_data.txt',
                      model_name='124M',  
                      steps=1000,  
                      restore_from='latest',  
                      run_name='AiName_new',
                      checkpoint_dir=checkpoint_dir,
                      overwrite=True)

checkpoint_dir = r"C:\Users\Namo\Documents\GitHub\Disc-Name\New\checkpoint\AiName"
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='AiName_new', checkpoint_dir=checkpoint_dir)

try:
    train_model()
    print("Model has been trained and saved successfully.")
except KeyboardInterrupt:
    print("\nExiting the program.")
