import json
import pickle
def dict_to_pkl(dict,file):
    with open(file, "wb") as tf:
        pickle.dump(dict,tf)
        # json.dump(dict,f,indent=2,sort_keys=True,ensure_ascii=False)
        # f.write(json.dumps(dict))
def pkl_to_dict(file):
    with open(file, "rb") as tf:
        new_dict = pickle.load(tf)
        return new_dict
