import docker
client = docker.from_env()

def get_containers():
  for container in client.containers.list():
    print(container.attrs['NetworkSettings']['IPAddress'])
    print(container.attrs['NetworkSettings']['Ports'])
    print(container.attrs['State']['Running'])
    print(container.attrs['State']['StartedAt'])
    print(container.attrs['State']['FinishedAt'])
    print(container.name)


def get_images():
  for container in client.images.list():
    print(container)

def get_stopped_containers():
  for container in client.containers.list:
    print(container)

def get_container_info():
  container = client.containers.get("testdb")
  ip_add = container.attrs['NetworkSettings']['IPAddress']
  print(ip_add)

get_containers()

# container = client.containers.create("ubuntu", stdin_open=True)
# container.start()
# container.stop()
