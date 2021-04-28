import json
from io import StringIO
import time

if __name__ == "__main__":
    import os.path
    from os import path

    file= os.path.join(os.getenv('MODEL_PATH'),'DRS_Model.pl')
    print ("Is model file exists?" + str(path.isfile('DRS_Model.pl')))
    prediction_input_list = []
    with open(os.path.join(os.environ['INPUT_PATH'], 'input.csv')) as input_fd:
        prediction_input_list = input_fd.readlines()

    with open(os.path.join(os.environ['OUTPUT_PATH'], 'output.csv'), 'w') as output_fd:
        for prediction_input in prediction_input_list:
            prediction_obj = [{'body': prediction_input.encode('utf-8')}]

            output_fd.write(str("output.........."))
            output_fd.write('\n')
