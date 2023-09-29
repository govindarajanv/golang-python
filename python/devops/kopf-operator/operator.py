import os
import kopf
import kubernetes
import yaml

@kopf.on.create('ephemeralvolumeclaims')
def create_fn(spec, name, namespace, logger, **kwargs):
  
    size = spec.get('size')
    if not size:
        raise kopf.PermanentError(f"Size must be set. Got {size!r}.")
    
    path = os.path.join(os.path.dirname(__file__), 'pvc.yaml')
    tmpl = open(path, 'rt').read()
    text = tmpl.format(size=size, name=name)
    data = yaml.safe_load(text)
      
    # cascaded deletion
    kopf.adopt(data)
        
    api = kubernetes.client.CoreV1Api()
    obj = api.create_namespaced_persistent_volume_claim(
        namespace=namespace,
        body=data,
    )         
            
    logger.info(f"PVC child is created: {obj}")
              
    return {'pvc-name': obj.metadata.name}

@kopf.on.update('ephemeralvolumeclaims')
def update_fn(spec, status, namespace, logger, **kwargs):

    size = spec.get('size', None)
    if not size:
        raise kopf.PermanentError(f"Size must be set. Got {size!r}.")

    pvc_name = status['create_fn']['pvc-name']
    pvc_patch = {'spec': {'resources': {'requests': {'storage': size}}}}
    print (pvc_patch)

    api = kubernetes.client.CoreV1Api()
    obj = api.patch_namespaced_persistent_volume_claim(
        namespace=namespace,
        name=pvc_name,
        body=pvc_patch,
    )

    logger.info(f"PVC child is updated: {obj}")

@kopf.on.event('ephemeralvolumeclaims')
def update_fn(spec, status, namespace, logger, **kwargs):
    print ("update_fn")

@kopf.timer('ephemeralvolumeclaims', interval=5.0,initial_delay=5)
def timer_function(spec, **kwargs):
    print ("\ntimer at regular intervals\n")

@kopf.on.delete('ephemeralvolumeclaims')
def delete_fn(spec, status, namespace, logger, **kwargs):
    print ("delete_fn")

@kopf.on.field('podwrappers', field='spec.somefield')
def somefield_changed(old, new, **_):
    print (field,"changed ++++\n")