from loadotenv import load_env
load_env('/workspaces/fruit-classifier-mlops-class/.env')
import os
ORG = os.environ.get("WANDB_API_KEY")
print(ORG)



#from loadotenv import load_env
#load_env()
#import os
#KEY = os.environ.get("WANDB_API_KEY")
#print(KEY)