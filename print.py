print("Inference")
  
import sys
import os
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(os.getenv('test'))
print(os.getenv('test1'))

print('DATA_PATH',DATA_PATH) 
print('MODEL_PATH',MODEL_PATH)
print('OUTPUT_PATH',OUTPUT_PATH)
print('CODE_PATH',CODE_PATH)


f= open(os.getenv('MODEL_PATH') + "/DRS_Model.pl","w+")
f.write("sampleline")
f.close()
