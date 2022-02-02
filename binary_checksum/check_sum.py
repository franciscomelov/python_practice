import hashlib

md5_hash = hashlib.md5()

a_file = open("sample.bin", "rb")
content = a_file.read()
md5_hash.update(content)

digest_1 = md5_hash.hexdigest()
print("first ", digest_1)


second_md5_hash = hashlib.md5()
b_file = open("second_sample.bin", "rb")
content = b_file.read()
second_md5_hash.update(content)

digest_2 = second_md5_hash.hedigest()
print("second", digest_2)

print(digest_2 == digest_1)