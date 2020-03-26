import boto3
import os
import mylogin as ml

def send_text_peg(text_msg):
    client = boto3.client('sns')
    client.publish(PhoneNumber= ml.get_peg_phone(), Message= text_msg)	


def send_text_leo(text_msg):
    client = boto3.client('sns')
    client.publish(PhoneNumber= ml.get_my_phone(), Message= text_msg)	


#Test
#send_text_leo('test text')