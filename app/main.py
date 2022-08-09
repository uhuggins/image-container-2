# 1. Library imports
import pandas as pd
from fastapi import FastAPI
import uvicorn
import numpy as np

import logging

from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json


import tensorflow as tf
tf_version = int(tf.__version__.split(".")[0])

#------------------------------

if tf_version == 2:
	import logging
	tf.get_logger().setLevel(logging.ERROR)

#------------------------------

from deepface import DeepFace
import time
from typing import List, Optional
import uuid


# 2. Create the app object
app = FastAPI()


# Define predict function

class Item(BaseModel):
    img: str
    actions: List[str] = []


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analyze/")
async def analyze(item: Item):
 
    global graph

    tic = time.time()
    trx_id = uuid.uuid4()

	#---------------------------
    if tf_version == 1:
        with graph.as_default():
            resp_obj = analyzeWrapper(item, trx_id)
    elif tf_version == 2:
        resp_obj = analyzeWrapper(item, trx_id)

	#---------------------------

    toc = time.time()

    return resp_obj

def analyzeWrapper(item, trx_id = 0):
    image = item.img
 
    results = item.actions
    print(results)
    print(type(results))
    


	# resp_obj = jsonify({'success': False})
    instances = []
	# if "img" in list(req.keys()):
    raw_content = item.img #list

    for item in raw_content: #item is in type of dict
        instances.append(item)

	#if len(instances) == 0:
	# 	return jsonify({'success': False, 'error': 'you must pass at least one img object in your request'}), 205

    # print("Analyzing ", len(instances)," instances")
    # detector_backend = 'opencv'
 
 
    obj = DeepFace.analyze(img_path = image, actions = results)
   # print(obj)

    return obj
	# #---------------------------


	# if "actions" in list(req.keys()):
	# 	actions = req["actions"]

	# if "detector_backend" in list(req.keys()):
	# 	detector_backend = req["detector_backend"]

	# #---------------------------

	# try:
	# 	resp_obj = DeepFace.analyze(instances, actions = actions)
	# except Exception as err:
	# 	print("Exception: ", str(err))
	# 	return jsonify({'success': False, 'error': str(err)}), 205

	#---------------
	#print(resp_obj)



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)