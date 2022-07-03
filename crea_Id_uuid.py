import uuid

# Generate a UUID from a host ID, sequence number, and the current time
print(uuid.uuid1())  # e.g: 308490b6-afe4-11eb-95f7-0c4de9a0c5af

# Generate a random UUID
print(uuid.uuid4())  # e.g: 93bc700b-253e-4081-a358-24b60591076a

print(uuid.uuid4().hex)
print(uuid.uuid4().is_safe)
print(uuid.uuid4().time_hi_version)
print(uuid.uuid4().time)
print(uuid.uuid4().node)
print(uuid.uuid4().int)
print(uuid.uuid4().clock_seq_hi_variant)
print(uuid.uuid4().fields)