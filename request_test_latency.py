#!/usr/bin/env python
#
# // SPDX-License-Identifier: BSD-3-CLAUSE
#
# (C) Copyright 2018, Xilinx, Inc.
# request_test_latency.py， modified by Haoran

from __future__ import print_function

import os,sys,argparse

import requests
import json
import time

def request(rest_api_url="http://localhost:9001/predict", image_path="/home/mluser/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min/ILSVRC2012_val_00000001.JPEG"):

  image = open(image_path, "rb").read()
  payload = {"image": image}

  # submit the request
  r = requests.post(rest_api_url, files=payload).json()


  # ensure the request was sucessful
  if r["success"]:
    print(json.dumps(r, indent=4, sort_keys=True))

  # otherwise, the request failed
  else:
    print("Request failed")

def test_round_trip(rest_api_url="http://localhost:9001/predict", image_path="/home/mluser/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min/ILSVRC2012_val_00000001.JPEG", repeat=1):
  start = time.clock()
  for i in range(repeat):
    request(args["rest_api_url"], args["image_path"])
  elapsed=(time.clock() - start)
  print("total round-trip time:{} ms".format(elapsed*1000))
  print("averge round-trip time:{} ms".format(elapsed*1000/repeat))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='pyXFDNN')
  parser.add_argument('--rest_api_url', default="", help='Url to the REST API eg: http://localhost:9000/predict')
  parser.add_argument('--image_path', default="", help='Path to the image eg: /home/mluser/CK-TOOLS/dataset-imagenet-ilsvrc2012-val-min/ILSVRC2012_val_00000001.JPEG')
  parser.add_argument('--repeat', type = int, default=1, help='repeated requests')

  args = vars(parser.parse_args())

  if args["rest_api_url"] and args["image_path"] :
    #request(args["rest_api_url"], args["image_path"])
    test_round_trip(args["rest_api_url"], args["image_path"], args["repeat"])
  else:
    print("Missing arguments, provide --rest_api url <>  and --image_path <>")

