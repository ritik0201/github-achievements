import dill
import os
p=os.path.join('artifacts','preprocessor.pkl')
mp=os.path.join('artifacts','model.pkl')
print('preprocessor file', p)
with open(p,'rb') as f:
    obj=dill.load(f)
    print('preprocessor type:', type(obj))
    print('preprocessor module:', obj.__class__.__module__)
    try:
        print('has attribute _name_to_fitted_passthrough?', hasattr(obj,'_name_to_fitted_passthrough'))
    except Exception as e:
        print('attr check error', e)

with open(mp,'rb') as f:
    m=dill.load(f)
    print('model type:', type(m))
    print('model module:', m.__class__.__module__)
